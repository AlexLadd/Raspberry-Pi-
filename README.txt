Python implementation for a shift register, such as the 74hc595, using a Raspberry Pi

Usage: 
sr = ShiftRegister() 
or optionally, 
sr = ShiftRegister(data_pin = 22, latch_pin = 27, clock_pin = 17, num_register = 1)

To write data to a specific pin: 
sr.digitalWrite(pin = 1, mode = 1) or sr.digitalWrite(pin = 1, mode = sr.HIGH)

To write data to multiple pins at once: 
sr.digitalWrite(pin = [1,2,3], mode = sr.HIGH)

All pin can be written to HIGH or LOW at once: 
sr.allPinsHigh() and sr.allPinsLow()
