from owon_psu import OwonPSU
import time



PORT = "/dev/POWER_SUPPLY"


class PowerSupply(OwonPSU):
    def __init__(self):
        OwonPSU.__init__(self, PORT)
        OwonPSU.open(self)
        OwonPSU.set_output(self,True)

    def ps_set_low_charging_voltage(self):
        OwonPSU.set_voltage(self,13.0)

    def ps_set_low_battery_voltage(self):
        OwonPSU.set_voltage(self,11.0)

    def ps_set_normal_charging_voltage(self):
        OwonPSU.set_voltage(self,14.6)

    def ps_set_normal_battery_voltage(self):
        OwonPSU.set_voltage(self,12.7)