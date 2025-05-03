import serial
import time
import can
from JDS6600 import FunctionGenerator
from CANTests import CANTesting
#todo -- create class to be called from main file !


arduino = serial.Serial(port='COM15', baudrate=115200, timeout=.1)
command = ""


def write_read(x):
    arduino.write(bytes(x, "utf-8"))

    data = arduino.readline()
    return data

def TurnONIgnition():
    value = write_read("R1_ON\n")

def TurnOFFIgnition():
    value = write_read("R1_OFF\n")

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

def driveSimulation():
    channel_name = 'PCAN_USBBUS1'  # Na primer, 'can0' za Linux ili 'PCAN_USBBUS1' za Windows
    bitrate = 500000  # 500 kbps
    CanTest = CANTesting()
    can_bus = CanTest.initialize_can_channel(channel_name, bitrate)
    fg = FunctionGenerator()
    fgObj = fg.FunctionGenerator_Init()
    for i in range(370):
        CanTest.set_rpm_test(can_bus,1200)
        fg.FunctionGenerator_ActivateChannels(fgObj, True, False)
        fg.FunctionGenerator_SetWaveformChannel1(fgObj, "cmos")
        fg.FunctionGenerator_SetAmplitudeChannel1(fgObj, 5.0)
        fg.FunctionGenerator_SetDutyCycleChannel1(fgObj, 50.0)
        fg.FunctionGenerator_SetFrequencyChannel1(fgObj, i)

def main():


    time.sleep(3)
    TurnONIgnition()
    time.sleep(3)
    write_read("R2_ON\n")
    time.sleep(1)
    TurnSignalLeftTest()
    time.sleep(1)
    TurnSignalRightTest()
    time.sleep(1)
    FaultyTurnSignalLeftTest()
    time.sleep(1)
    FaultyTurnSignalRightTest()
    time.sleep(1)
    HazardWarningTest()
    time.sleep(1)
    TurnOFFIgnition()
    time.sleep(3)
    channel_name = 'PCAN_USBBUS1'
    bitrate = 500000  # 500 kbps



    fg = FunctionGenerator()
    CanTest = CANTesting()
    can_bus = CanTest.initialize_can_channel(channel_name, bitrate)
    bus = can.interface.Bus(interface='pcan', channel='PCAN_USBBUS1', bitrate=500000)
    CanTest.send_rpm_test(can_bus)
    time.sleep(1)
    CanTest.send_vbat_test(can_bus)
    time.sleep(1)
    CanTest.send_map_test(can_bus)
    time.sleep(1)
    CanTest.send_iat_test(can_bus)
    time.sleep(1)
    CanTest.send_ignAdvance_test(can_bus)
    time.sleep(1)

    fgObj=fg.FunctionGenerator_Init()
    fg.FunctionGenerator_ActivateChannels(fgObj, True, False)
    fg.FunctionGenerator_SetWaveformChannel1(fgObj, "cmos")
    fg.FunctionGenerator_SetAmplitudeChannel1(fgObj, 5.0)
    fg.FunctionGenerator_SetDutyCycleChannel1(fgObj, 50.0)
    for i in range(370):
        fg.FunctionGenerator_SetFrequencyChannel1(fgObj, i)
        time.sleep(0.5)
    driveSimulation()
    time.sleep(5)
    fg.FunctionGenerator_ActivateChannels(fgObj, False, False)
    fg.FunctionGenerator_DeInit(fgObj)
    TurnOFFIgnition()


while True:
    main()