import RPi.GPIO as GPIO

# Bit banging class to control a shift register on a Raspberry Pi
class ShiftRegister:
  def __init__(self, data_pin=22, latch_pin=27, clock_pin=17, num_registers=1):
    GPIO.setmode(GPIO.BCM)
    self.data = 0x0
    self.num_registers = num_registers
    self.HIGH = 1
    self.LOW = 0
    self.PIN_DATA = data_pin
    self.PIN_LATCH = latch_pin
    self.PIN_CLOCK = clock_pin
    GPIO.setup(self.PIN_DATA,  GPIO.OUT)
    GPIO.setup(self.PIN_LATCH, GPIO.OUT)
    GPIO.setup(self.PIN_CLOCK, GPIO.OUT)
    self.allPinsLow()

  # Set desired pin(s) to either HIGH(1) or LOW(0)
  def digitalWrite(self, pin=None, mode=None):
    if pin is not None and mode is not None:
      if isinstance(pin, int):
        self._setPin(pin, mode)
      if isinstance(pin, list):
        for p in pin:
          self._setPin(p, mode)

    GPIO.output(self.PIN_LATCH, self.LOW)
    for x in range(self.num_registers*8):
      GPIO.output(self.PIN_CLOCK, self.LOW)
      GPIO.output(self.PIN_DATA, (self.data >> x) & 1)
      GPIO.output(self.PIN_CLOCK, self.HIGH)
    GPIO.output(self.PIN_LATCH, self.HIGH)

  # Set bit in the data byte to the desired mode
  def _setPin(self, pin, mode):
    if mode == 1:
      self.data = self.data | (0x1 << pin)
    if mode == 0:
      self.data = self.data & ~(0x1 << pin)

  # Get mode of desire pin
  def getPin(self, pin):
    return (self.data >> pin) & 1

  def allPinsLow(self):
    self.data = 0
    self.digitalWrite()

  def allPinsHigh(self):
    for x in range(1, self.num_registers*8 + 1):
      self._setPin(x, self.HIGH)
    self.digitalWrite()

  # Print current value of shift register data -- for debugging purposes
  def printData(self):
    for x in range(self.num_registers * 8, 0, -1):
      print((self.data >> x) & 1, end=" ")
    print("")
