

import serial
import time

class SignalSimulator:
    def __init__(self):
        self.arduino = serial.Serial(port='/dev/ttyUSB1', baudrate=115200, timeout=.1)
        self.command = ""

    def check_if_sensor_id_is_valid(self, in_sensor_id: int)->bool:

        if in_sensor_id == range(0,7):
            return True
        return False

    def check_if_requested_voltage_is_valid(self,in_voltage: float)->bool:

        if 0.0 <= in_voltage <= 5.0:
            return True
        return False

    def write_read(self, x):
        self.arduino.write(bytes(x, "utf-8"))

        data = self.arduino.readline()
        return data

    def set_FI_low_voltage_on_sensor(self, in_sensor_id: int):

        out_string = f"S{in_sensor_id}0.30\n"
        self.arduino.write(bytes(out_string, "utf-8"))

    def set_FI_high_voltage_on_sensor(self, in_sensor_id: int):

        out_string = f"S{in_sensor_id}4.80\n"
        self.arduino.write(bytes(out_string, "utf-8"))


    def set_voltage_on_sensor(self, in_sensor_id: int, in_voltage: float):

        request_status: bool = True
        request_status &= self.check_if_sensor_id_is_valid(in_sensor_id)
        request_status &= self.check_if_requested_voltage_is_valid(in_voltage)

        if request_status:
            out_string = f"S{in_sensor_id}{in_voltage:.2f}\n"
            self.arduino.write(bytes(out_string, "utf-8"))

