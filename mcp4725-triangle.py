import mcp4725_driver as mcp
import signal_generator as sg

import time
#import math

amplitude = 3.0
signal_frequency = 10
sampling_frequency = 1000
t = 0
start_t = time.time()

try:
    dac = mcp.MCP4725(5.1)
    while True:
        dac.set_voltage(sg.get_triangle_wave_amplitude(signal_frequency, t)*amplitude)
        t = time.time() - start_t
        sg.wait_for_sampling_period(sampling_frequency)
finally:
    dac.deinit()

