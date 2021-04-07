# L'Exprimante
an open-source old newspapers distributor based on [Lectura+ database](https://www.lectura.plus/Presse/). 📃

this project was
  - initiated by Auvergne-Rhône-Alpes Livre et Lecture (Alizé Buisse and Priscille Legros)
  - created, designed and developed by Léa Belzunces, Esther Bouquet and Déborah-Loïs Séry

All of the next steps have been developed for a raspberry pi 3 B+ running [Stretch Version 9](https://downloads.raspberrypi.org/raspbian/images/raspbian-2019-04-09/) and an Epson TM-T20III. The articles that you want to print need to be .txt files. The content needs to be in markdown with the following order: 

- '#' → name of the newspaper 
- '##' → title (h1)
- '#####' → subtitle (h2)
- '######' → subtitle (h3)
- '###' → text 
- '####' → URL to the online article (to generate a qrCode)
- '#######' → category

You can link a .jpg or a .JPEG file to the corresponding .txt file (if the article contains an illustration for instance) by giving it the same name.

![how codes and components are intertwined](https://github.com/estherbouquet/lectura-plus/blob/master/electrogif.gif)


## 💿 install [python-escpos - Python library to manipulate ESC/POS Printers](https://python-escpos.readthedocs.io/en/latest/user/installation.html)
  
  - open your terminal
  
  - install dependencies: `sudo apt-get install python3 python3-setuptools python3-pip libjpeg8-dev`
  
  - write `sudo pip3 install python-escpos`
    - if you have a MemoryError, try to run `pip3` with `--no-cache-dir` such as `pip3 --no-cache-dir install python-escpos` but you should not need it
    - NB: sudo is very important if you want to run your script with systemd, otherwise you can't communicate to the usb with the root priviledge
    
  - plug the usb cable of the thermal printer into the raspberry and turn the thermal printer on

  - get the Product ID and Vendor ID using `lsusb` command
    - you should have something like: `Bus 001 Device 007: ID 04b8:0e28 Seiko Epson Corp.` <br>
      The part that interests us is `ID 04b8:0e28` where `04b8` is the vendor ID and `0e28` is the product ID
    
  - create the `udev` rule file with `sudo nano /etc/udev/rules.d/99-escpos.rules` 
    - write `SUBSYSTEM=="usb", ATTRS{idVendor}=="04b8", ATTRS{idProduct}=="0e28", MODE="0664", GROUP="dialout"` where you replace `04b8` and `0e28` by your own ID
    
  - use the `groups` command line to check which groups you're part of
    - and add your username to the `dialout` group if you're not. <br>
      `echo $USER` <br>
      `sudo adduser $USER dialout` where `$USER` is the name that appeared when you did the previous command
      
  - restart `udev` with the command `sudo udevadm control --reload` (or) `sudo service udev restart`
  - reboot your raspberry

## 📠 test your printer <> raspberry connection

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

## 🔘 install the button controlling the printer

Because the code that launches the printer is linked to a physical button being pushed or not, we need to physically connect the button to the raspberry. We added at LED and resistor as there is no GUI involved in this project so it tells people that the print is being processed and they don't need to push the button again.

  - Materials:
    - 1 breadboard
    - 1 [pushed button](https://www.ag-electronique.fr/boutons-poussoirs-avec-anneau-a-led-plat-acier-inoxydable/10004-bouton-poussoir-plat-acier-inoxydable-dpst-1no-1nf-velr2000-5410329406189.html?search_query=R2000&results=6)
    - 1 RTC (RealTime Clock - we chose the DS3231)
    - 4 LED (1 yellow, 1 green, 1 red, 1 blue)
    - 4 resistors (XX for the blue LED and XX for the yellow, red and green LED)
    - 11 female-male cables

![how to connect](https://raw.githubusercontent.com/estherbouquet/lectura-plus/master/doc/connectique.JPG)

## 🕐 install the RTC (Real Time Clock)

The Raspberry Pi is designed to be an ultra-low cost computer, so a lot of things we are used to on a computer have been left out. For example, your laptop and computer have a little coin-battery-powered 'Real Time Clock' (RTC) module, which keeps time even when the power is off, or the battery removed. To keep costs low and the size small, an RTC is not included with the Raspberry Pi. Instead, the Pi is intended to be connected to the Internet via Ethernet or WiFi, updating the time automatically from the global ntp (network time protocol) servers.

For this project, the raspberry has no network connection, so it will not be able to keep the time when the power goes out. This will lead to an error when we want to print an article at a specific date. To fix this problem you need to connect and install a RTC by following the steps on [Adafruit's website](https://learn.adafruit.com/adding-a-real-time-clock-to-raspberry-pi/overview). Don't forget to do `sudo hwclock -s` when you are done in order to write the RTC time back to the system time.

## 💻 try the code

  - open your terminal
  
  - check for updates `sudo apt-get update`
  
  - install dependencies: `sudo apt-get install python3-markdown` and ~~`sudo apt-get install wkhtmltopdf`~~ and `pip3 install imgkit`

  - install dependency `pip3 install pyqrcode` and module `pip3 install pypng`
  
  - clone this repository using git in ./Documents/ and your ssh key OR download it on your raspberry in ./Documents/ with `git clone https://github.com/estherbouquet/lectura-plus`
  - Once it is cloned, go to ./lectura-plus/
  - install bash dependency `sudo apt-get install recode` and allow privileges by copying `chmod u=rwx encoding.sh` in the terminal and then `chmod u=rwx listeningForPushedButton.sh` and `chmod u=rwx copy_from_usb.sh` and finally `chmod u=rwx delete_from_usb.sh`
 
- Render the fonts in the output result:
    - open the file explorer and go to `home/pi`
    - create a new folder named `.fonts`
    - make it visible with `ctrl+h`
    - copy the fonts in `home/pi/Documents/lectura-plus/assets/` to `home/pi/Documents/.fonts`.
 
  - if you want to check manually that the program works first before running it independently when the raspberry starts:
    - be sure to be in the `lectura-plus` folder.
    - write `python3 listeningForUSB.py` in the terminal. It will start listening for a USB named 'ajout' being plugged into the raspberry
    - plug the usb drive with a folder named `articles` (inside of which you will have the articles you want to copy to the raspberry for a later print)
      - `python3 listeningForUSB.py` is now supposed to launch `./copy_from_usb.sh` (will copy the content of ./articles/ and convert it)
        - if the red led is blinking eight times quickly, it means that there is no folder named `articles` detected
        - if the green led is turning on it means that the program is working
          - the blue led will turn on when all the files are copied (you can remove safely your usb at this moment)
          - when the conversion is done, the green and blue led will turn off and the green led will blink one last time
    - open a new terminal window, go back to `./Documents/lectura-plus/`
    - write `./listeningForPushedButton.sh` in the terminal and press the physical button whenever you feel ready
      - the led will blink twice if the program can find articles to print through the printer
    - whenever you want to stop/quit, just close the 2 terminal windows.

  - after you have checked that the two programs work when they are launched manually, you can run them automatically when the raspberry starts following the instructions below.

## 💻 automatize!

It is important that you check if your programs run flowlessly when you launch them manually before starting automatizing them. 
We are going to start by creating `.service` files because we are going to use `systemd`.

- Do `cd /etc/systemd/system`
- `sudo nano printer.service`
  - copy paste the content of `printer.service` that you can find in the `/home/pi/Documents/lectura-plus/systemdfiles` folder inside
  - `ctrl + o` to write then press `enter` to valid the modifications then `ctrl + x` to exit
  - you can check if it worked by using the command `cat printer.service`
- `sudo systemctl start printer.service`
- you can check the status of the service (i.e. if it works) by typing `systemctl status printer.service` (and use `ctrl + c` to exit)
  - if it works correctly, a green "active" should appear
  - you can use `sudo journalctl -u printer.service` to log errors
  - you can try to press the button. The blue led should blink twice and the printer print
  - if no errors are raised in the status mode when you push the button, it means that the program is working. Congrats!
 - now, we can enable the service so it will run our program as soon as the raspberry boots. To do so:
  - `sudo systemctl enable printer.service`
  - `sudo reboot` and try to press the button when the raspberry starts up!
  - Know that if one day you want to disable the `printer.service`, nothing simpler than `sudo systemctl disable printer.service`
