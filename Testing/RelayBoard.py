

import serial
import time

class RelayBoard:
    def __init__(self):
        self.arduino = serial.Serial(port='/dev/RELAY_BOARD', baudrate=115200, timeout=.1)
        self.command = ""
        print("Initializing Relay Board...")


    def write_read(self, x):
        self.arduino.write(bytes(x, "utf-8"))

        data = self.arduino.readline()
        return data

    def KL30_ON(self):
        value = self.write_read("R1_ON\n")

    def KL30_OFF(self):
        value = self.write_read("R1_OFF\n")
    def KL15_ON(self):
        value = self.write_read("R2_ON\n")

    def KL15_OFF(self):
        value = self.write_read("R2_OFF\n")


    def TurnSignalLeftON(self):
        value = self.write_read("R3_ON\n")

    def TurnSignalLeftOFF(self):
        value = self.write_read("R3_OFF\n")

    def TurnSignalRightON(self):
        value = self.write_read("R4_ON\n")

    def TurnSignalRightOFF(self):
        value = self.write_read("R4_OFF\n")

    def HighBeamON(self):
        value = self.write_read("R5_ON\n")

    def HighBeamOFF(self):
        value = self.write_read("R5_OFF\n")

    def LowBeamON(self):
        value = self.write_read("R6_ON\n")

    def LowBeamOFF(self):
        value = self.write_read("R6_OFF\n")

    def NeutralON(self):
        value = self.write_read("R7_ON\n")

    def NeutralOFF(self):
        value = self.write_read("R7_OFF\n")


    def TurnSignalLeftTest(self):
        for i in range(20):
            self.TurnSignalLeftON()
            time.sleep(0.5)
            self.TurnSignalLeftOFF()
            time.sleep(0.5)
    def TurnSignalRightTest(self):
        for i in range(20):
            self.TurnSignalRightON()
            time.sleep(0.5)
            self.TurnSignalRightOFF()
            time.sleep(0.5)

    def FaultyTurnSignalLeftTest(self):
        for i in range(20):
            self.TurnSignalLeftON()
            time.sleep(0.25)
            self.TurnSignalLeftOFF()
            time.sleep(0.25)
    def FaultyTurnSignalRightTest(self):
        for i in range(20):
            self.TurnSignalRightON()
            time.sleep(0.25)
            self.TurnSignalRightOFF()
            time.sleep(0.25)



    def HazardWarningTest(self):
        for i in range(20):
            self.TurnSignalLeftON()
            self.TurnSignalRightON()
            time.sleep(0.5)
            self.TurnSignalLeftOFF()
            self.TurnSignalRightOFF()
            time.sleep(0.5)

    def HiBeamTest(self):
        for i in range(20):
            self.HighBeamON()
            time.sleep(0.5)
            self.HighBeamOFF()
            time.sleep(0.5)

    def LowBeamTest(self):
        for i in range(20):
            self.LowBeamON()
            time.sleep(0.5)
            self.LowBeamOFF()
            time.sleep(0.5)