#!/bin/bash

# Installs all dependencies that the master requires and setup required configurations.

############################################################################
# Install and update standard packages
sudo apt update
sudo apt -y upgrade

# Add new packages to install in the list below
sudo apt -y install git hostapd 

echo "Finished installing packages"

############################################################################
# Setup new hostname
sudo printf "\n127.0.1.1      soundzone-master" >> /etc/hosts
sudo hostnamectl set-hostname soundzone-master

echo "Finished setting up hostname"

############################################################################
# Setup the Access point from ethernet

sudo systemctl unmask hostapd
sudo systemctl enable hostapd

# Add a network device called br0
sudo printf "[NetDev]\n Name=br0\n Kind=bridge" > /etc/systemd/network/bridge-br0.netdev

# Add ethernet as a bridge member
sudo printf "[Match] \nName=eth0 \n \n[Network] \nBridge=br0" > /etc/systemd/network/br0-member-eth0.network

# Create service to auto start bridge on boot
sudo systemctl enable systemd-networkd

# Configure the DHCP
sudo sed -i "1i denyinterfaces wlan0 eth0" /etc/dhcpcd.conf # append to line 1 of file
sudo printf "interface br0" >> /etc/dhcpcd.conf # end of file

# Makes sure WiFi is not blocked
sudo rfkill unblock wlan

# Configure AP
sudo mv ./Setup_files/hostapd.conf /etc/hostapd/


echo "Finished setting up Access Point"










############################################################################
# Ask if the user wants to restart pi to finish install
while true; do
    read -p "Do you wish to restart to finish configuration? y/n" yn
    case $yn in
        [Yy]* ) sudo systemctl reboot; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done



