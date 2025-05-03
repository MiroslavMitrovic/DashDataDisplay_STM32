import jds6600
import time

class FunctionGenerator:

    def FunctionGenerator_Init(self):
        fg = jds6600.JDS6600(port="COM14")
        fg.connect()
        print("Connected!")
        print(fg.get_channels())
        return fg

    def FunctionGenerator_DeInit(self,fg):
        fg.close()

    def FunctionGenerator_ActivateChannels(self,fg,channel1,channel2):
        fg.set_channels(channel1=channel1, channel2=channel2)
    def FunctionGenerator_SetWaveformChannel1(self,fg,waveform):
        fg.set_waveform(channel=1, value=waveform)

    def FunctionGenerator_SetWaveformChannel2(self,fg,waveform):
        fg.set_waveform(channel=2, value=waveform)

    def FunctionGenerator_SetFrequencyChannel1(self,fg,frequency):
        fg.set_frequency(channel=1, value=frequency)

    def FunctionGenerator_SetFrequencyChannel2(self,fg,frequency):
        fg.set_frequency(channel=2, value=frequency)

    def FunctionGenerator_SetAmplitudeChannel1(self,fg,amplitude):
        fg.set_amplitude(channel=1, value=amplitude)

    def FunctionGenerator_SetAmplitudeChannel2(self,fg,amplitude):
        fg.set_amplitude(channel=2, value=amplitude)


    def FunctionGenerator_SetOffsetChannel1(self,fg,offset):
        fg.set_offset(channel=1, value=offset)

    def FunctionGenerator_SetOffsetChannel2(self,fg,offset):
        fg.set_offset(channel=2, value=offset)

    def FunctionGenerator_SetDutyCycleChannel1(self,fg,dytyCycle):
        fg.set_dutycycle(channel=1, value=dytyCycle)

    def FunctionGenerator_SetDutyCycleChannel2(self,fg,dytyCycle):
        fg.set_amplitude(channel=2, value=dytyCycle)

