#!/bin/bash

# Install and setup required dependencies to test the UDP connection

############################################################################
# Install and update standard packages
sudo apt update
sudo apt -y upgrade

# Add new packages to install in the list below
sudo apt -y install git iperf

echo "Finished installing packages"

############################################################################
# Setup new hostname
read -p "Enter new hostname for slave (soundzone-udptestx)" x

sudo printf "\n127.0.1.1      ${x}" >> /etc/hosts
sudo hostnamectl set-hostname "${x}"

echo "Finished setting up hostname"

############################################################################
# Connect to WiFi

sudo sed -i "3i country=DK" /etc/wpa_supplicant/wpa_supplicant.conf # Set country code

echo "Connect to server WiFi"
echo "Input SSID"
read y
sudo printf "\n network={ \n         ssid="$y"\n         psk="SuperSejtPassword"\n}" >> /etc/wpa_supplicant/wpa_supplicant.conf




echo "Done setting up soundzone client :)"

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
