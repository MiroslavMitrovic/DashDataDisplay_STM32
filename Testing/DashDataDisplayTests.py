import os
import platform
from enum import Enum
from math import pi
from time import sleep

import serial
import time
import can
from JDS6600 import FunctionGenerator
from CANTests import CANTesting
#todo -- create class to be called from main file !

GEAR_RATIO_1:float = 5.034042
GEAR_RATIO_2:float = 3.199118
GEAR_RATIO_3:float = 2.357342
GEAR_RATIO_4:float = 1.92907
GEAR_RATIO_5:float = 1.678014
FINAL_DRIVE_RATIO:float = 3.875
DYNAMIC_ROLLING_RADIUS:float = 0.267 # in [m]
NUMBER_OF_PULSES_PER_ROTATION_VSS:int = 10
MPS_TO_KPH_RATIO:float = 3.6


class GearRatio(Enum):
    GEAR_1 = (1, 5.034042)
    GEAR_2 = (2, 3.199118)
    GEAR_3 = (3, 2.357342)
    GEAR_4 = (4, 1.92907)
    GEAR_5 = (5, 1.678014)

    def __new__(cls, gear_step:int, ratio:float):
        obj = object.__new__(cls)
        obj._value_ = gear_step
        obj.ratio = ratio
        return obj


def calculate_vehicle_speed(in_rpm:int , in_gear_ratio:float)->int:
    vehicle_speed: int = 0
    angular_wheel_speed:float = (in_rpm * 2.0 * pi * 60.0) / (in_gear_ratio * FINAL_DRIVE_RATIO)  # converted to rad/s
    vehicle_speed = int(angular_wheel_speed * DYNAMIC_ROLLING_RADIUS / 1000.0)

    return vehicle_speed

def calculate_gearshift_rpm_drop(in_current_rpm:int, in_current_gear:int)->tuple[int, int]:
    if in_current_gear < GearRatio.GEAR_1.value or in_current_gear >= GearRatio.GEAR_5.value:
        raise ValueError("RPM drop can only be calculated for upshifts from gear 1 to gear 4.")

    current_ratio:float = GearRatio(in_current_gear).ratio
    next_ratio:float = GearRatio(in_current_gear + 1).ratio
    rpm_after_shift:int = int(round(in_current_rpm * next_ratio / current_ratio))
    rpm_drop:int = in_current_rpm - rpm_after_shift

    return rpm_after_shift, rpm_drop

def calculate_downshift_rpm_rise(in_current_rpm:int, in_current_gear:int)->tuple[int, int]:
    if in_current_gear <= GearRatio.GEAR_1.value or in_current_gear > GearRatio.GEAR_5.value:
        raise ValueError("RPM rise can only be calculated for downshifts from gear 2 to gear 5.")

    current_ratio:float = GearRatio(in_current_gear).ratio
    previous_ratio:float = GearRatio(in_current_gear - 1).ratio
    rpm_after_shift:int = int(round(in_current_rpm * previous_ratio / current_ratio))
    rpm_rise:int = rpm_after_shift - in_current_rpm

    return rpm_after_shift, rpm_rise

def convert_vehicle_speed_to_signal(in_vehicle_speed:int)->int:
    wheel_circumference_m:float = 2.0 * pi * DYNAMIC_ROLLING_RADIUS
    sig_gen_frequency:int = int(
        in_vehicle_speed
        * NUMBER_OF_PULSES_PER_ROTATION_VSS
        / (wheel_circumference_m * MPS_TO_KPH_RATIO)
    )

    return sig_gen_frequency




arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=.1)
command = ""


def write_read(x):
    arduino.write(bytes(x, "utf-8"))

    data = arduino.readline()
    return data

def KL30_ON():
    value = write_read("R1_ON\n")

def KL30_OFF():
    value = write_read("R1_OFF\n")
def KL15_ON():
    value = write_read("R2_ON\n")

def KL15_OFF():
    value = write_read("R2_OFF\n")


def TurnSignalLeftON():
    value = write_read("R3_ON\n")

def TurnSignalLeftOFF():
    value = write_read("R3_OFF\n")

def TurnSignalRightON():
    value = write_read("R4_ON\n")

def TurnSignalRightOFF():
    value = write_read("R4_OFF\n")

def HighBeamON():
    value = write_read("R5_ON\n")

def HighBeamOFF():
    value = write_read("R5_OFF\n")

def LowBeamON():
    value = write_read("R6_ON\n")

def LowBeamOFF():
    value = write_read("R6_OFF\n")

def NeutralON():
    value = write_read("R7_ON\n")

def NeutralOFF():
    value = write_read("R7_OFF\n")


def TurnSignalLeftTest():
    for i in range(20):
        TurnSignalLeftON()
        time.sleep(0.5)
        TurnSignalLeftOFF()
        time.sleep(0.5)
def TurnSignalRightTest():
    for i in range(20):
        TurnSignalRightON()
        time.sleep(0.5)
        TurnSignalRightOFF()
        time.sleep(0.5)

def FaultyTurnSignalLeftTest():
    for i in range(20):
        TurnSignalLeftON()
        time.sleep(0.25)
        TurnSignalLeftOFF()
        time.sleep(0.25)
def FaultyTurnSignalRightTest():
    for i in range(20):
        TurnSignalRightON()
        time.sleep(0.25)
        TurnSignalRightOFF()
        time.sleep(0.25)



def HazardWarningTest():
    for i in range(20):
        TurnSignalLeftON()
        TurnSignalRightON()
        time.sleep(0.5)
        TurnSignalLeftOFF()
        TurnSignalRightOFF()
        time.sleep(0.5)

def HiBeamTest():
    for i in range(20):
        HighBeamON()
        time.sleep(0.5)
        HighBeamOFF()
        time.sleep(0.5)

def LowBeamTest():
    for i in range(20):
        LowBeamON()
        time.sleep(0.5)
        LowBeamOFF()
        time.sleep(0.5)

def driveSimulation():
    default_interface = "socketcan" if platform.system() == "Linux" else "pcan"
    can_interface = os.getenv("CAN_INTERFACE", default_interface)
    default_channel = "PCAN_USBBUS1" if can_interface == "pcan" else "can0"
    channel_name = os.getenv("CAN_CHANNEL", default_channel)
    bitrate = int(os.getenv("CAN_BITRATE", "500000"))
    CanTest = CANTesting()
    can_bus = None
    fg = FunctionGenerator()
    fgObj = fg.FunctionGenerator_Init()
    rpm_offset_drop:tuple[int, int] = (0, 0)
    try:
        can_bus = CanTest.initialize_can_channel(
            channel=channel_name,
            bitrate=bitrate,
            interface=can_interface,
            auto_reset=True,
        )
        fg.FunctionGenerator_ActivateChannels(fgObj, True, False)
        fg.FunctionGenerator_SetWaveformChannel1(fgObj, "cmos")
        fg.FunctionGenerator_SetAmplitudeChannel1(fgObj, 5.0)
        fg.FunctionGenerator_SetDutyCycleChannel1(fgObj, 50.0)
        NeutralON()
        sleep(5.0)
        NeutralOFF()
        for i in range(1,6):
            ratio = GearRatio(i).ratio

            current_rpm: int = 0
            for j in range(180):
                current_rpm = rpm_offset_drop[0] + j * 100
                if current_rpm >= 9000:
                    break
                can_bus = CanTest.set_rpm_test(can_bus, current_rpm)
                vehicle_speed = calculate_vehicle_speed(current_rpm, ratio)
                fg_frequency = convert_vehicle_speed_to_signal(vehicle_speed)
                fg.FunctionGenerator_SetFrequencyChannel1(fgObj, fg_frequency)
                sleep(0.25)
            if i < GearRatio.GEAR_5.value:
                rpm_offset_drop = calculate_gearshift_rpm_drop(current_rpm,i)
            print("Upshift Performed!")
        downshift_rpm_threshold:int = 2500
        rpm_offset_rise:tuple[int, int] = (current_rpm, 0)
        for i in range(GearRatio.GEAR_5.value, GearRatio.GEAR_1.value - 1, -1):
            ratio = GearRatio(i).ratio

            current_rpm: int = 0
            for j in range(180):
                current_rpm = rpm_offset_rise[0] - j * 100
                if current_rpm <= downshift_rpm_threshold:
                    break
                can_bus = CanTest.set_rpm_test(can_bus, current_rpm)
                vehicle_speed = calculate_vehicle_speed(current_rpm, ratio)
                fg_frequency = convert_vehicle_speed_to_signal(vehicle_speed)
                fg.FunctionGenerator_SetFrequencyChannel1(fgObj, fg_frequency)
                sleep(0.25)

            if i > GearRatio.GEAR_1.value:
                rpm_offset_rise = calculate_downshift_rpm_rise(current_rpm,i)
            print("Downshift Performed!")

    finally:
        fg.FunctionGenerator_SetFrequencyChannel1(fgObj, 0)
        fg.FunctionGenerator_ActivateChannels(fgObj, False, False)
        CanTest.close_bus(can_bus)

def main():

    time.sleep(3)
    KL30_ON()
    time.sleep(5)
    KL15_ON()
    time.sleep(1)
    driveSimulation()
    #HiBeamTest()
    #LowBeamTest()
    #HazardWarningTest()
    KL15_OFF()
    time.sleep(7)
    KL15_ON()
    time.sleep(10)
    KL15_OFF()
    time.sleep(5)
    KL30_OFF()



while True:
    main()
