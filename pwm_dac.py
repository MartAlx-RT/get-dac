import RPi.GPIO as GPIO

class R2R_PWM:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.pwm_frequency = pwm_frequency
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT, initial = 0)
        self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_frequency)
        self.pwm.start(0)
    
    def deinit(self):
        GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup()
    
    def set_number(self, number):
        coef = number / self.dynamic_range * 100.0
        self.pwm.ChangeDutyCycle(coef)
        
    def set_voltage(self, voltage):
        if(not(0.0 <= voltage <= self.dynamic_range)):
            print(f"Voltage is out of range (0.0 ... {self.dynamic_range:.2f} V)")
            print("Set zero.")
            self.set_number(0)
        else: self.set_number(voltage)

    
if __name__ == "__main__":
    try:
        dac = R2R_PWM(12, 500, 3.29, True)
               
        while True:
            try:
                voltage = float(input("Input voltage (V): "))
                dac.set_voltage(voltage)
        
            except ValueError:
                print("This is NAN, try again\n")
        
    finally:
        dac.deinit()