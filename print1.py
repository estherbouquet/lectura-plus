from printlib import pins, wake, reset, configure_printer, print_bitmap


#pins where the printer is plugged
TX = int(sys.argv[1])
RX = int(sys.argv[2])
baudrate = int(sys.argv[3])
width = int(sys.argv[4])

pins.set_mode(RX, pigpio.INPUT)
pins.set_mode(TX, pigpio.OUTPUT)


wake()
reset()
configure_printer(6, 80, 50)
print_bitmap(width, img13.img)
