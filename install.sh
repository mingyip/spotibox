#!/usr/bin/bash

# apt install basic software
sudo apt-get update
sudo apt-get install elpa-magit -y
sudo apt install git-all -y
sudo apt install ffmpeg -y
sudo apt-get install alsa-base alsa-utils -y
sudo apt install python3-pip -y

# pip install python packages
sudo pip install pyalsaaudio
sudo pip install spi
sudo pip install spidev
sudo pip install mfrc522
