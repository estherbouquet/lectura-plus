# lectura-plus
an open-source old newspapers distributor 

All of the next steps have been developed for a raspberry pi 3 B+ Version 9 of stretch

Install [python-escpos - Python library to manipulate ESC/POS Printers](https://python-escpos.readthedocs.io/en/latest/user/installation.html)
  
1. open your terminal
  
2. `pip install python-escpos`
    - if you have a MemoryError, try to run `pip` with `--no-cache-dir` such as `pip --no-cache-dir install python-escpos`

3. get the Product ID and Vendor ID from the `lsusb` command
    - you should have something like: `Bus 001 Device 007: ID 04b8:0e28 Seiko Epson Corp.` <br>
      The part that interests us is `ID 04b8:0e28` where `04b8` is the vendor ID and `0e28` is the product ID
    
4. create the `udev` rule file with `sudo nano /etc/udev/rules.d/99-escpos.rules` 

    - write the line: `SUBSYSTEM=="usb", ATTRS{idVendor}=="04b8", ATTRS{idProduct}=="0e28", MODE="0664", GROUP="dialout"` where you replace `04b8` and `0e28` by your own ID
    
5. use the `groups`command line to check which groups you're part of
    - and add yourself to the `dialout` group if you're not. <br>
      `echo $USER` <br>
      `sudo adduser $USER dialout` where `$USER` is the name that appeared when you did the previous command
      
6. restart `udev` with the command `sudo udevadm control --reload` (or) `sudo service udev restart`
7. reboot your raspberry
