#import r2r_dac as r2r
import pwm_dac as pwm
import signal_generator as sg
import time
#import math

amplitude = 3.0
signal_frequency = 10
sampling_frequency = 1000
t = 0
start_t = time.time()

try:
    dac = pwm.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)
    
    while True:
        dac.set_voltage(sg.get_sin_wave_amplitude(signal_frequency, t)*amplitude)
        t = time.time() - start_t
        sg.wait_for_sampling_period(sampling_frequency)
finally:
    dac.deinit()
