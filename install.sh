#!/bin/bash

 #Open the Raspberry Pi terminal and run the following command
 wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.68.tar.gz
 tar zxvf bcm2835-1.68.tar.gz
 cd bcm2835-1.68/
 sudo ./configure && sudo make && sudo make check && sudo make install
 # For more information, please refer to the official website: http://www.airspayce.com/mikem/bcm2835/
 
 #Open the Raspberry Pi terminal and run the following command
sudo apt-get install wiringpi
#For Raspberry Pi systems after May 2019 (earlier than before, you may not need to execute), you may need to upgrade:
wget https://project-downloads.drogon.net/wiringpi-latest.deb
sudo dpkg -i wiringpi-latest.deb
gpio -v
# Run gpio -v and version 2.52 will appear. If it does not appear, the installation is wrong
#Bullseye branch system use the following command:
git clone https://github.com/WiringPi/WiringPi
cd WiringPi
./build
gpio -v
# Run gpio -v and version 2.60 will appear. If it does not appear, it means that there is an installation error

sudo apt-get update
sudo apt-get install python-pip
sudo apt-get install python-pil
sudo apt-get install python-numpy
sudo pip install RPi.GPIO
sudo pip install spidev
 
sudo apt-get install python3-pip
sudo apt-get install python3-pil
sudo apt-get install python3-numpy
sudo pip3 install RPi.GPIO
sudo pip3 install spidev

sudo apt-get install imagemagick -y
sudo cp ~/pictoor/wpa_supplicant.conf /etc/wpa_supplicant/
sudo chmod u+x ~/pictoor/RaspberryPi_JetsonNano/python/examples/boot.py
sudo chmod u+x ~/pictoor/RaspberryPi_JetsonNano/python/examples/test.py
sudo chmod u+x ~/pictoor/RaspberryPi_JetsonNano/python/examples/blerp.py

crontab -l > mycron
echo @reboot sleep 30 && /home/nox/pictoor/RaspberryPi_JetsonNano/python/examples/boot.py >> mycron
echo @reboot sleep 60 && /home/nox/pictoor/RaspberryPi_JetsonNano/python/examples/blerp.py >> mycron
crontab mycron
rm mycron

sudo pip3 install bottle
