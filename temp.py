from escpos.printer import Usb # import Usb class

p = Usb(0x04b8, 0x0e28, 0) 
p.image('/home/pi/Documents/lectura-plus/images/2-2.jpg')
p.cut()
