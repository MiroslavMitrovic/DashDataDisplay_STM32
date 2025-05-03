import pyvisa


# test the communication with device
rm = pyvisa.ResourceManager()
print(rm.list_resources())
IdString = ["" for _ in range(6)]
# open the DM3058 resource
dmm = rm.open_resource('USB0::0x1AB1::0x09C4::DM3R260300123::INSTR')
print(rm)
#do a Query of instrument
IdString = dmm.query('*IDN?')
print(IdString)

# Do a voltage measurement
voltageString = [""]
voltageString = dmm.query(":MEASure:VOLTage:DC?")
decimalVoltage = float(voltageString)
print(voltageString)
print("Measured Voltage is: ", decimalVoltage, "VDC")


