import numpy as np
import time

def get_sin_wave_amplitude(freq, time):
    return (math.sin(2*freq*math.pi) + 1)/2


def wait_for_sampling_period(sampling_freq):
    time.sleep(sampling_freq)


