import os
import platform
import subprocess
import time

import can


class CANTesting:
    def __init__(self):
        self.bus = None
        self.interface = None
        self.channel = None
        self.bitrate = None
        self.auto_reset = True
        self.recovery_delay_s = 0.5
        self.max_reconnect_attempts = 3

    def initialize_can_channel(self, channel, bitrate, interface=None, auto_reset=True):
        self.channel = channel
        self.bitrate = bitrate
        self.interface = interface or self._guess_interface(channel)
        self.auto_reset = auto_reset

        if self.interface == "socketcan":
            self._ensure_socketcan_ready()

        self.bus = self._open_bus_with_fallback()
        print(
            f"CAN channel {self.channel} successfully initialized "
            f"using {self.interface} at {self.bitrate} bps."
        )
        return self.bus

    def _guess_interface(self, channel):
        if platform.system() == "Linux":
            return os.getenv("CAN_INTERFACE", "socketcan")
        if isinstance(channel, str) and channel.upper().startswith("PCAN_"):
            return "pcan"
        return os.getenv("CAN_INTERFACE", "socketcan")

    def _open_bus(self):
        bus_kwargs = {
            "interface": self.interface,
            "channel": self.channel,
            "bitrate": self.bitrate,
        }

        if self.interface == "pcan":
            bus_kwargs["auto_reset"] = self.auto_reset

        return can.Bus(**bus_kwargs)

    def _socketcan_channel_exists(self, channel="can0"):
        return os.path.exists(f"/sys/class/net/{channel}")

    def _socketcan_channel_is_up(self):
        operstate_path = f"/sys/class/net/{self.channel}/operstate"
        try:
            with open(operstate_path, "r", encoding="ascii") as operstate_file:
                return operstate_file.read().strip() == "up"
        except OSError:
            return False

    def _ensure_socketcan_ready(self):
        if not self._socketcan_channel_exists(self.channel):
            raise RuntimeError(
                f"SocketCAN interface {self.channel} does not exist. "
                "Ensure the PEAK adapter is bound and the CAN netdevice is created."
            )

        if self._socketcan_channel_is_up():
            return

        restart_ms = os.getenv("CAN_RESTART_MS", "100")
        commands = [
            ["ip", "link", "set", self.channel, "down"],
            [
                "ip",
                "link",
                "set",
                self.channel,
                "up",
                "type",
                "can",
                "bitrate",
                str(self.bitrate),
                "restart-ms",
                restart_ms,
            ],
        ]

        for command in commands:
            try:
                subprocess.run(command, check=True, capture_output=True, text=True)
            except PermissionError as error:
                raise RuntimeError(
                    f"Insufficient privileges to configure {self.channel}. "
                    "Run the script with CAP_NET_ADMIN/root, or configure can0 "
                    "once via systemd/udev."
                ) from error
            except subprocess.CalledProcessError as error:
                stderr = (error.stderr or "").strip()
                raise RuntimeError(
                    f"Failed to configure SocketCAN interface {self.channel}: {stderr}"
                ) from error

    def _open_bus_with_fallback(self):
        try:
            return self._open_bus()
        except OSError as error:
            error_message = str(error)
            if self.interface == "pcan" and "pcanbasic library not found" in error_message.lower():
                fallback_channel = os.getenv("CAN_SOCKETCAN_CHANNEL", "can0")
                if self._socketcan_channel_exists(fallback_channel):
                    print(
                        "PCANBasic library is not installed. "
                        f"Falling back to socketcan/{fallback_channel}."
                    )
                    self.interface = "socketcan"
                    self.channel = fallback_channel
                    return self._open_bus()

                raise RuntimeError(
                    "PCAN backend requested, but the PCANBasic library is not installed. "
                    "No SocketCAN interface was found either. "
                    "Install the PEAK PCANBasic library for python-can 'pcan', "
                    "or bring up a SocketCAN interface such as can0 and run with "
                    "CAN_INTERFACE=socketcan."
                ) from error
            raise
        except can.CanInitializationError as error:
            raise RuntimeError(
                f"Failed to initialize {self.interface}/{self.channel}: {error}"
            ) from error

    def _shutdown_bus(self, bus):
        if bus is None:
            return

        try:
            bus.shutdown()
        except Exception:
            pass

    def recover_bus(self, bus=None):
        active_bus = bus or self.bus

        if (
            self.interface == "pcan"
            and active_bus is not None
            and hasattr(active_bus, "reset")
        ):
            try:
                if active_bus.reset():
                    time.sleep(self.recovery_delay_s)
                    self.bus = active_bus
                    return active_bus
            except can.CanError:
                pass

        self._shutdown_bus(active_bus)

        last_error = None
        for attempt in range(1, self.max_reconnect_attempts + 1):
            try:
                self.bus = self._open_bus_with_fallback()
                print(
                    f"Recovered CAN interface on attempt {attempt}: "
                    f"{self.interface}/{self.channel}"
                )
                return self.bus
            except Exception as error:
                last_error = error
                print(
                    f"CAN recovery attempt {attempt} failed for "
                    f"{self.interface}/{self.channel}: {error}"
                )
                time.sleep(self.recovery_delay_s)

        raise RuntimeError(
            f"Unable to recover CAN interface {self.interface}/{self.channel}"
        ) from last_error

    def close_bus(self, bus=None):
        active_bus = bus or self.bus
        self._shutdown_bus(active_bus)
        if active_bus is self.bus:
            self.bus = None

    def split_two_bytes(self, word):
        high_byte = (word >> 8) & 0xFF
        low_byte = word & 0xFF
        return high_byte, low_byte

    def send_message(self, bus, arbitration_id, data, is_extended_id=False):
        message = can.Message(
            arbitration_id=arbitration_id,
            data=data,
            dlc=len(data),
            is_extended_id=is_extended_id,
        )

        last_error = None
        for attempt in range(1, self.max_reconnect_attempts + 1):
            try:
                bus.send(message)
                self.bus = bus
                print(f"Message sent on {bus.channel_info} payload is {list(data)}")
                return bus
            except (can.CanError, OSError) as error:
                last_error = error
                print(
                    f"CAN send failed on attempt {attempt} for "
                    f"{self.interface}/{self.channel}: {error}"
                )
                bus = self.recover_bus(bus)

        raise RuntimeError(
            f"Unable to send CAN frame on {self.interface}/{self.channel}"
        ) from last_error

    def send_ignAdvance_test(self, bus):
        arbitration_id = 0x5E9
        data = [0x00] * 8

        for i in range(1000):
            data[6], data[7] = self.split_two_bytes(i)
            bus = self.send_message(bus, arbitration_id, data)
            time.sleep(0.02)

        return bus

    def send_iat_test(self, bus):
        arbitration_id = 0x5E9
        data = [0x00] * 8

        for i in range(1000):
            data[4], data[5] = self.split_two_bytes(i)
            bus = self.send_message(bus, arbitration_id, data)
            time.sleep(0.02)

        return bus

    def send_map_test(self, bus):
        arbitration_id = 0x5E8
        data = [0x00] * 8

        for i in range(1000):
            data[0], data[1] = self.split_two_bytes(i)
            bus = self.send_message(bus, arbitration_id, data)
            time.sleep(0.02)

        return bus

    def send_vbat_test(self, bus):
        arbitration_id = 0x5EB
        data = [0x00] * 8

        for i in range(1000):
            data[0], data[1] = self.split_two_bytes(i)
            bus = self.send_message(bus, arbitration_id, data)
            time.sleep(0.02)

        return bus

    def send_rpm_test(self, bus):
        arbitration_id = 0x5E8
        data = [0x00] * 8

        for i in range(1000):
            data[2], data[3] = self.split_two_bytes(i)
            bus = self.send_message(bus, arbitration_id, data)
            time.sleep(0.02)

        return bus

    def set_rpm_test(self, bus, rpm_value):
        arbitration_id = 0x5E8
        data = [0x00] * 8
        data[2], data[3] = self.split_two_bytes(rpm_value)

        bus = self.send_message(bus, arbitration_id, data)
        time.sleep(0.02)
        return bus
