#!/bin/bash

# Installs all dependencies that the master requires and setup required configurations.

############################################################################
# Install and update standard packages
sudo apt-get update
sudo apt-get -y upgrade

# Add new packages to install in the list below
sudo apt-get -y install hostapd python3-pip 

# Install python packages
sudo pip3 install virtualenv

echo "Finished installing packages"

############################################################################
# Setup new hostname
sudo printf "\n127.0.1.1      soundzone-master" | sudo tee -a /etc/hosts
sudo hostnamectl set-hostname soundzone-master

echo "Finished setting up hostname"

############################################################################
# Setup the Access point from ethernet

sudo systemctl unmask hostapd
sudo systemctl enable hostapd

# Add a network device called br0
sudo printf "[NetDev]\n Name=br0\n Kind=bridge" | sudo tee -a /etc/systemd/network/bridge-br0.netdev

# Add ethernet as a bridge member
sudo printf "[Match] \nName=eth0 \n \n[Network] \nBridge=br0" | sudo tee -a /etc/systemd/network/br0-member-eth0.network

# Create service to auto start bridge on boot
sudo systemctl enable systemd-networkd

# Configure the DHCP
sudo sed -i "1i denyinterfaces wlan0 eth0" /etc/dhcpcd.conf # append to line 1 of file
sudo printf "interface br0" | sudo tee -a /etc/dhcpcd.conf # end of file



# Configure AP


sudo mv ./Setup_files/hostapd.conf /etc/hostapd/

# Makes sure WiFi is not blocked
sudo rfkill unblock 0


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



