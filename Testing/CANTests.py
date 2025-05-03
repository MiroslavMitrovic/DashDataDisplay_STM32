import can
import time
can.rc['interface'] = 'pcan'
can.rc['channel'] = 'PCAN_USBBUS1'
can.rc['bitrate'] = 500000

class CANTesting:

    def initialize_can_channel(self,channel, bitrate):

        try:
            bus = can.Bus(interface='pcan', channel=channel, bitrate=bitrate)
            print(f"CAN channel {channel} succesfully initialized with speed of {bitrate} bps.")
            return bus
        except Exception as e:
            print(f"Initialization error of CAN channel: {e}")
            return None





    def split_two_bytes(self,word):
        
        
        high_byte = (word >> 8) & 0xFF 
        low_byte = word & 0xFF 
        return high_byte, low_byte

    def send_ignAdvance_test(self,bus):

        l_arbitration_id = 0x5E9
        l_data = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        l_is_extended_id : bool = False

        dlc = 8
        for i in range(1000):
            l_data[6], l_data[7] = self.split_two_bytes(i)


            msg = can.Message(
                arbitration_id=l_arbitration_id,
                data=l_data,
                dlc=8,
                is_extended_id=l_is_extended_id
            )
            try:
                bus.send(msg)
                print(f"Message sent on {bus.channel_info} payload is {l_data}")
            except can.CanError:
                print("Message NOT sent")
            time.sleep(0.02)





    def send_iat_test(self,bus):

        l_arbitration_id = 0x5E9
        l_data = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        l_is_extended_id : bool = False

        dlc = 8
        for i in range(1000):
            l_data[4], l_data[5] = self.split_two_bytes(i)


            msg = can.Message(
                arbitration_id=l_arbitration_id,
                data=l_data,
                dlc=8,
                is_extended_id=l_is_extended_id
            )
            try:
                bus.send(msg)
                print(f"Message sent on {bus.channel_info} payload is {l_data}")
            except can.CanError:
                print("Message NOT sent")
            time.sleep(0.02)




    def send_map_test(self,bus):

        l_arbitration_id = 0x5E8
        l_data = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        l_is_extended_id : bool = False

        dlc = 8
        for i in range(1000):
            l_data[0], l_data[1] = self.split_two_bytes(i)


            msg = can.Message(
                arbitration_id=l_arbitration_id,
                data=l_data,
                dlc=8,
                is_extended_id=l_is_extended_id
            )
            try:
                bus.send(msg)
                print(f"Message sent on {bus.channel_info} payload is {l_data}")
            except can.CanError:
                print("Message NOT sent")
            time.sleep(0.02)



    def send_vbat_test(self,bus):

        l_arbitration_id = 0x5EB
        l_data = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        l_is_extended_id : bool = False

        dlc = 8
        for i in range(1000):
            l_data[0], l_data[1] = self.split_two_bytes(i)


            msg = can.Message(
                arbitration_id=l_arbitration_id,
                data=l_data,
                dlc=8,
                is_extended_id=l_is_extended_id
            )
            try:
                bus.send(msg)
                print(f"Message sent on {bus.channel_info} payload is {l_data}")
            except can.CanError:
                print("Message NOT sent")
            time.sleep(0.02)


    def send_rpm_test(self,bus):

        l_arbitration_id = 0x5E8
        l_data = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        l_is_extended_id : bool = False

        dlc = 8
        for i in range(1000):
            l_data[2], l_data[3] = self.split_two_bytes(i)


            msg = can.Message(
                arbitration_id=l_arbitration_id,
                data=l_data,
                dlc=8,
                is_extended_id=l_is_extended_id
            )
            try:
                bus.send(msg)
                print(f"Message sent on {bus.channel_info} payload is {l_data}")
            except can.CanError:
                print("Message NOT sent")
            time.sleep(0.02)
    def set_rpm_test(self,bus,rpm_value):
        l_arbitration_id = 0x5E8
        l_data = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        l_is_extended_id: bool = False

        dlc = 8
        l_data[2], l_data[3] = self.split_two_bytes(rpm_value)

        msg = can.Message(
            arbitration_id=l_arbitration_id,
            data=l_data,
            dlc=8,
            is_extended_id=l_is_extended_id
        )
        try:
            bus.send(msg)
            print(f"Message sent on {bus.channel_info} payload is {l_data}")
        except can.CanError:
            print("Message NOT sent")
        time.sleep(0.02)