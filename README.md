# lectura-plus
an open-source old newspapers distributor 

All of the next steps have been developed for a raspberry pi 3 B+ Version 9 of stretch and an Epson TM-T20III

### 1. install [python-escpos - Python library to manipulate ESC/POS Printers](https://python-escpos.readthedocs.io/en/latest/user/installation.html)
  
  - open your terminal
  
  - write `pip3 install python-escpos`
    - if you have a MemoryError, try to run `pip3` with `--no-cache-dir` such as `pip3 --no-cache-dir install python-escpos` but you should not need it.

  - get the Product ID and Vendor ID using `lsusb` command
    - you should have something like: `Bus 001 Device 007: ID 04b8:0e28 Seiko Epson Corp.` <br>
      The part that interests us is `ID 04b8:0e28` where `04b8` is the vendor ID and `0e28` is the product ID
    
  - create the `udev` rule file with `sudo nano /etc/udev/rules.d/99-escpos.rules` 
    - write `SUBSYSTEM=="usb", ATTRS{idVendor}=="04b8", ATTRS{idProduct}=="0e28", MODE="0664", GROUP="dialout"` where you replace `04b8` and `0e28` by your own ID
    
  - use the `groups` command line to check which groups you're part of
    - and add yourself to the `dialout` group if you're not. <br>
      `echo $USER` <br>
      `sudo adduser $USER dialout` where `$USER` is the name that appeared when you did the previous command
      
  - restart `udev` with the command `sudo udevadm control --reload` (or) `sudo service udev restart`
  - reboot your raspberry

### 2. test your installation
  - open your terminal
  - create a new project folder using `mkdir nameofyourfolder`
  - go inside using `cd nameofyourfolder`
  - when you are in, write `touch nameofyourfile.py`
  - and write `sudo nano nameofyourfile.py` (will open the file and let you write inside of it) 
    - inside the file, you can copy paste this snippet of code: <br>
      ```
      from escpos.printer import Usb 
      
      p = Usb(0x04b8,0x0e28,0)
      p.text("Hello World\n")
      p.barcode('1324354657687','EAN13',64,2,'','')
      p.cut() 
      ``` 
    
    

