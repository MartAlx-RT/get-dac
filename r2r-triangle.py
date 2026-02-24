import r2r_dac as r2r
import signal_generator as sg
import time
#import math

amplitude = 2.0
signal_frequency = 10
sampling_frequency = 1000
t = 0
start_t = time.time()

try:
    dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)
    
    while True:
        print(sg.get_triangle_wave_amplitude(signal_frequency, t)*amplitude)
        dac.set_voltage(sg.get_triangle_wave_amplitude(signal_frequency, t)*amplitude)
        t = time.time() - start_t
        sg.wait_for_sampling_period(sampling_frequency)
finally:
    dac.deinit()
