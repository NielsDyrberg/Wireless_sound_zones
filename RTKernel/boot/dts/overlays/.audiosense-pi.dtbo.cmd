cmd_arch/arm/boot/dts/overlays/audiosense-pi.dtbo := mkdir -p arch/arm/boot/dts/overlays/ ; gcc -E -Wp,-MMD,arch/arm/boot/dts/overlays/.audiosense-pi.dtbo.d.pre.tmp -nostdinc -I./scripts/dtc/include-prefixes -undef -D__DTS__ -x assembler-with-cpp -o arch/arm/boot/dts/overlays/.audiosense-pi.dtbo.dts.tmp arch/arm/boot/dts/overlays/audiosense-pi-overlay.dts ; ./scripts/dtc/dtc -@ -H epapr -O dtb -o arch/arm/boot/dts/overlays/audiosense-pi.dtbo -b 0 -i arch/arm/boot/dts/overlays/ -Wno-interrupt_provider -Wno-unit_address_vs_reg -Wno-unit_address_format -Wno-gpios_property -Wno-avoid_unnecessary_addr_size -Wno-alias_paths -Wno-graph_child_address -Wno-simple_bus_reg -Wno-unique_unit_address -Wno-pci_device_reg  -Wno-interrupts_property -Wno-label_is_string -Wno-reg_format -Wno-pci_device_bus_num -Wno-i2c_bus_reg -Wno-spi_bus_reg -Wno-avoid_default_addr_size -d arch/arm/boot/dts/overlays/.audiosense-pi.dtbo.d.dtc.tmp arch/arm/boot/dts/overlays/.audiosense-pi.dtbo.dts.tmp ; cat arch/arm/boot/dts/overlays/.audiosense-pi.dtbo.d.pre.tmp arch/arm/boot/dts/overlays/.audiosense-pi.dtbo.d.dtc.tmp > arch/arm/boot/dts/overlays/.audiosense-pi.dtbo.d

source_arch/arm/boot/dts/overlays/audiosense-pi.dtbo := arch/arm/boot/dts/overlays/audiosense-pi-overlay.dts

deps_arch/arm/boot/dts/overlays/audiosense-pi.dtbo := \
  scripts/dtc/include-prefixes/dt-bindings/pinctrl/bcm2835.h \
  scripts/dtc/include-prefixes/dt-bindings/gpio/gpio.h \

arch/arm/boot/dts/overlays/audiosense-pi.dtbo: $(deps_arch/arm/boot/dts/overlays/audiosense-pi.dtbo)

$(deps_arch/arm/boot/dts/overlays/audiosense-pi.dtbo):
