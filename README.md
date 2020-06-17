# lectura+
an open-source old newspapers distributor based on [Lectura+ database](https://www.lectura.plus/Presse/). 📃

this project was
  - initiated by Auvergne-Rhône-Alpes Livre et Lecture
  - created, designed and developed by Léa Belzunces, Esther Bouquet and Déborah-Loïs Séry

All of the next steps have been developed for a raspberry pi 3 B+ running Stretch Version 9 and an Epson TM-T20III.

![how codes and components are intertwined](https://github.com/estherbouquet/lectura-plus/blob/master/electrogif.gif)


## 💿 install [python-escpos - Python library to manipulate ESC/POS Printers](https://python-escpos.readthedocs.io/en/latest/user/installation.html)
  
  - open your terminal
  
  - install dependencies: `sudo apt-get install python3 python3-setuptools python3-pip libjpeg8-dev`
  
  - write `pip3 install python-escpos`
    - if you have a MemoryError, try to run `pip3` with `--no-cache-dir` such as `pip3 --no-cache-dir install python-escpos` but you should not need it
    
  - plug the usb cable of the thermal printer into the raspberry

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

## 📠 test your installation

  - open your terminal
  
  - create a new project folder using `mkdir nameofyourfolder`
  
  - go inside using `cd nameofyourfolder`
  
  - when you are in, write `touch nameofyourfile.py`
  
  - and write `sudo nano nameofyourfile.py` (will open the file and let you write inside of it) 
    - inside the file, you can copy paste this snippet of code: <br>
    
      ```python
      from escpos.printer import Usb 
      
      p = Usb(0x04b8, 0x0e28, 0)
      p.text("hello human, i wish u a nice day\n")
      p.cut() 
      ``` 
      📢 in `p = Usb(0x04b8, 0x0e28, 0)` you need to replace `04b8` and `0e28`by your own vendor and product ID.
  
  - save the file and exit it
  
  - make sure the printer is plugged correctly
  
  - run `python3 nameofyourfile.py`
  
  if the installation worked, you should now have a tiny printed paper greeting you 🔖 otherwise, you can find more information [here (raspi doc)](https://python-escpos.readthedocs.io/en/latest/user/raspi.html), or [here (original github repo)](https://github.com/python-escpos/python-escpos).
  
## 💻 customize print speed and density

- turn the printer on while pushing the feed button
  - it prints a test
- press the feed button again for more than 1 sec 
  - Mode Selection opens
  - press shortly (<1 sec)three times the feed button and one time long (>1 sec) the feed button
    - it opens Customize Value Settings
      - press three times to open the density options and one time long (>1 sec) the feed button
        - press three times to select density +2 and one time long (>1 sec) the feed button
      - press four times to open the speeed options and one time long (>1 sec) the feed button
        - press eleven times to select speed 11 and one time long (>1 sec) the feed button
- turn the printer off and restart it to use it

## 💻 try the code

  - open your terminal
  
  - install dependencies: `sudo apt-get install python3-markdown` and `sudo apt-get install wkhtmltopdf`

  - install dependency `pip3 install pyqrcode` and module `pip3 install pypng`

  - install bash dependency `apt-get install recode` and allow privileges by copying `chmod u=rwx encoding.sh` in the terminal
