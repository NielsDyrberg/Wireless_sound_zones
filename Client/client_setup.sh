#!/bin/bash

# Installs all dependencies that the slave requires and setup required configurations.

############################################################################
# Install and update standard packages
sudo apt-get update
sudo apt-get -y upgrade


# Add new packages to install in the list below
sudo apt -y install python3-pip 

# Install python packages
sudo pip install virtualenv

echo "Finished installing packages"

############################################################################
# Setup new hostname
read -p "Enter new hostname for slave (soundzone-slavex)" x

sudo printf "\n127.0.1.1      ${x}" | sudo tee -a /etc/hosts
sudo hostnamectl set-hostname "${x}"

echo "Finished setting up hostname"

############################################################################
# Connect to WiFi




PS3='How do you wish to configure the WiFi '
wifi_setup=("Connect to soundzone network" "Input Wifi SSID/password" "Do not configures")
select fav in "${wifi_setup[@]}"; do
    case $fav in
        "Connect to soundzone network")
            echo "Inserting sounzone network setup"
            sudo printf "\n network={ \n         ssid="SoundZone"\n         psk="SuperSejtPassword"\n}" | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf
            break
            ;; 
        "Input Wifi SSID/password")
            read -p "Input Wifi SSID" SSID
            read -p "Input Wifi password" psk
            sudo printf "\n network={ \n         ssid="$SSID"\n         psk="$psk"\n}" | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf
            break
            ;;
        "Do not configures")
            echo "User requested exit"
            break
            ;;
            *) echo "invalid option $REPLY";;
    esac
done

sudo sed -i "3i country=DK" /etc/wpa_supplicant/wpa_supplicant.conf # Set country code

sudo rfkill unblock 0 # Enables the wifi, should not have to be used for this to work, but it does not work without.




echo "Done setting up soundzone slave :)"

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
