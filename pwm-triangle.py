#import r2r_dac as r2r
import pwm_dac as pwm
import signal_generator as sg
import time
#import math

amplitude = 2.0
signal_frequency = 10
sampling_frequency = 1000
t = 0
start_t = time.time()

try:
    dac = pwm.R2R_PWM(12, 500, 3.29, True)
    
    while True:
        print(sg.get_triangle_wave_amplitude(signal_frequency, t)*amplitude)
        dac.set_voltage(sg.get_triangle_wave_amplitude(signal_frequency, t)*amplitude)
        t = time.time() - start_t
        sg.wait_for_sampling_period(sampling_frequency)
finally:
    dac.deinit()
