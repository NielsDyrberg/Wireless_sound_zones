#!/bin/bash

# Compiles RT kernel and install it on the system

############################################################################

# Add new packages to install in the list below
sudo apt install git bc bison flex libssl-dev make libncurses5-dev

# Download files and apply patch

git clone --depth=1 https://github.com/raspberrypi/linux

cd linux

wget https://mirrors.edge.kernel.org/pub/linux/kernel/projects/rt/5.10/patch-5.10.73-rt54.patch.gz

zcat patch-5.10.73-rt54.patch.gz | patch -p1

# Open menu and select General setup --> Preemption model --> Fully preemptible Kernel

make menuconfig

# Compile the kernel

KERNEL=kernel7l
make bcm2711_defconfig
make -j4 zImage modules dtbs
sudo make modules_install
sudo cp arch/arm/boot/dts/*.dtb /boot/
sudo cp arch/arm/boot/dts/overlays/*.dtb* /boot/overlays/
sudo cp arch/arm/boot/dts/overlays/README /boot/overlays/
sudo cp arch/arm/boot/zImage /boot/$KERNEL.img