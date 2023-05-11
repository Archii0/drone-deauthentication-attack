# drone-deauthentication-attack

A script to carry out deauthentication attacks on Tello drones. This was made as part of a two day ethical hacking session using Linux, led by the Defence Science and Technology Laboratory.

It works best using a WiFi adapter so that the program has a wider range of network detection.

The WiFi adapter I used was the ALFA network adapter on Kali Linux

Driver installation
Kali
STEP 1 : Open Terminal Emulator

STEP 2 : Run commands

``` bash
sudo apt update
sudo apt install realtek-rtl88xxau-dkms
```

STEP 3 (Optional): Check driver existance

Run commands below:

find /lib/modules/`uname -r`/ -name "88XXau.ko"
There should be a file in search result if driver was successfully installed.


