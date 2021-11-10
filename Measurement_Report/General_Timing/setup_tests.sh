#!/bin/bash

# Installs all dependencies that the slave requires and setup required configurations.

############################################################################
# Install and update standard packages
sudo apt-get update
sudo apt-get -y upgrade

# Add new packages to install in the list below
sudo apt-get -y install libasound2 libasound2-dev git

# Download files

wget https://github.com/NielsDyrberg/Wireless_sound_zones/raw/DacDriver_v1.0/Measurement_Report/General_Timing/General_Timing.zip

unzip General_Timing

cd General_Timing/

sudo chmod u+x ./Drift\ af\ DAC\ modul/test_dac_jitter
sudo chmod u+x ./Drift\ af\ tidstagning\ chrono/chronotest_10sek
sudo chmod u+x ./Tidstagning\ af\ funktion\ Python\ og\ C/randomwrite

# Install BCM2835 library

wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.70.tar.gz
tar zxvf bcm2835-1.70.tar.gz
cd bcm2835-1.70
./configure
make
sudo make check
sudo make install

sudo rm -rf bcm2835-1.70


# Setup DAC module

sudo mv -f config.txt /boot/
sync




