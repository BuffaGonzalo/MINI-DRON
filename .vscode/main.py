from machine import Pin, PWM
from utime import sleep

led_pin = Pin("LED", Pin.OUT)  # Use the correct pin number for the LED

FRE = PWM(Pin(2))
FRE.freq(1000)

"""
for duty_cycle in range(0, 8128, 1000):  # Duty cycle: 0 to 65535
    
    sleep(0.01)  # 10 ms delay
    """
FRE.duty_u16(16256*2)
    
print("LED starts flashing...")
while True:
    try:
        led_pin.toggle()
        sleep(0.1) # sleep 1sec
        
        # Increase brightness


        # Decrease brightness
        """
        for duty_cycle in range(65535, 0, -1000):  # Duty cycle: 65535 to 0
            FRE.duty_u16(duty_cycle)
            sleep(0.01)  # 10 ms delay
        """
    except KeyboardInterrupt:
        break
led_pin.off()
print("Finished.")