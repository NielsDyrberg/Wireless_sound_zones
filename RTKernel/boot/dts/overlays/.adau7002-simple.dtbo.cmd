cmd_arch/arm/boot/dts/overlays/adau7002-simple.dtbo := mkdir -p arch/arm/boot/dts/overlays/ ; gcc -E -Wp,-MMD,arch/arm/boot/dts/overlays/.adau7002-simple.dtbo.d.pre.tmp -nostdinc -I./scripts/dtc/include-prefixes -undef -D__DTS__ -x assembler-with-cpp -o arch/arm/boot/dts/overlays/.adau7002-simple.dtbo.dts.tmp arch/arm/boot/dts/overlays/adau7002-simple-overlay.dts ; ./scripts/dtc/dtc -@ -H epapr -O dtb -o arch/arm/boot/dts/overlays/adau7002-simple.dtbo -b 0 -i arch/arm/boot/dts/overlays/ -Wno-interrupt_provider -Wno-unit_address_vs_reg -Wno-unit_address_format -Wno-gpios_property -Wno-avoid_unnecessary_addr_size -Wno-alias_paths -Wno-graph_child_address -Wno-simple_bus_reg -Wno-unique_unit_address -Wno-pci_device_reg  -Wno-interrupts_property -Wno-label_is_string -Wno-reg_format -Wno-pci_device_bus_num -Wno-i2c_bus_reg -Wno-spi_bus_reg -Wno-avoid_default_addr_size -d arch/arm/boot/dts/overlays/.adau7002-simple.dtbo.d.dtc.tmp arch/arm/boot/dts/overlays/.adau7002-simple.dtbo.dts.tmp ; cat arch/arm/boot/dts/overlays/.adau7002-simple.dtbo.d.pre.tmp arch/arm/boot/dts/overlays/.adau7002-simple.dtbo.d.dtc.tmp > arch/arm/boot/dts/overlays/.adau7002-simple.dtbo.d

source_arch/arm/boot/dts/overlays/adau7002-simple.dtbo := arch/arm/boot/dts/overlays/adau7002-simple-overlay.dts

deps_arch/arm/boot/dts/overlays/adau7002-simple.dtbo := \

arch/arm/boot/dts/overlays/adau7002-simple.dtbo: $(deps_arch/arm/boot/dts/overlays/adau7002-simple.dtbo)

$(deps_arch/arm/boot/dts/overlays/adau7002-simple.dtbo):
