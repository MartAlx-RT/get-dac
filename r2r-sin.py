import r2r_dac as r2r
import signal_generator as sg
import time
import math

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000
t = 0

try:
    dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)

    while True:
        dac.set_voltage(sg.get_sin_wave_amplitude(signal_frequency, t))
        t += 1/signal_frequency
finally:
    dac.deinit()
