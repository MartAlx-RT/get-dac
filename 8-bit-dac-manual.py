import RPi.GPIO as GPIO
#import time
GPIO.setmode(GPIO.BCM)

dynamic_range = 3.3
pinout = [16, 20, 21, 25, 26, 17, 27, 22]
GPIO.setup(pinout, GPIO.OUT)

def voltage_to_number(voltage):
    if(not(0.0 <= voltage <= dynamic_range)):
        print(f"Voltage is out of range (0.0 ... {dynamic_range:.2f} V)")
        print("Set zero.")
        return 0
    return int(voltage / dynamic_range * 255)

def number_to_dac(number, pinout):
    GPIO.output(pinout, [int(element) for element in bin(number)[2:].zfill(8)])

voltage = 0
number = 0
try:
    while True:
        try:
            voltage = float(input("Enter voltage (V): "))
            number = voltage_to_number(voltage)
            number_to_dac(number, pinout)
        
        except ValueError:
            print("This is NAN, try again")
finally:
    GPIO.output(pinout, 0)
    GPIO.cleanup()
