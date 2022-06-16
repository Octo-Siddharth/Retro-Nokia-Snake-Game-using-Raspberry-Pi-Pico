import machine
from machine import Pin, I2C, ADC
sda1=machine.Pin(2)
scl1=machine.Pin(3)
i2c=machine.I2C(1,sda=sda1, scl=scl1, freq=400000)

print('Scan i2c bus...')
devices = i2c.scan()

if len(devices) == 0:
  print("No i2c device !")
else:
  print('i2c devices found:',len(devices))

  for device in devices:
    print("Decimal address: ",device," | Hexa address: ",hex(device))