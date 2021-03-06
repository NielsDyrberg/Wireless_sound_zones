#include <iostream>
#include <chrono>
#include <bcm2835.h>






#define OUTPUT_PIN RPI_V2_GPIO_P1_40 // Define output pin
#define INPUT_PIN RPI_V2_GPIO_P1_37 // Define Input pin




int main() {
	if(!bcm2835_init())return 1;{ /* Initialize */
		bcm2835_gpio_fsel(OUTPUT_PIN, BCM2835_GPIO_FSEL_OUTP); /*Sets OUTPUT_PIN to output*/
		bcm2835_gpio_fsel(INPUT_PIN, BCM2835_GPIO_FSEL_INPT); // Set INPUT_PIN to be an input
		bcm2835_gpio_set_pud(INPUT_PIN, BCM2835_GPIO_PUD_DOWN); // with a down
		//bcm2835_gpio_ren(INPUT_PIN); // And a high detect enable
	}
	bcm2835_gpio_clr(OUTPUT_PIN);



	std::cout << "Nyeste version kører" << std::endl;




	int ticksNow = 0;
	bool sleep = false;
	auto start = std::chrono::steady_clock::now();
	auto slut = std::chrono::steady_clock::now();
	int timesrun = 0;
	bool toggle = false;



	auto resul = std::chrono::duration_cast<std::chrono::microseconds>(slut - start);
	while (true) {
		while (bcm2835_gpio_lev(INPUT_PIN)) {
			timesrun = 1;
			//timesrun++;
			// std::cout << "Pin lav" << std::endl;
			sleep = true;
			start = std::chrono::steady_clock::now();
			while (sleep) {
			slut = std::chrono::steady_clock::now();
			resul = std::chrono::duration_cast<std::chrono::microseconds>(slut - start);
			if (resul.count() > 5000000)
			sleep = false;
			}
			toggle = !toggle;
			// std::cout << toggle << std::endl;
			if (toggle)
			bcm2835_gpio_set(OUTPUT_PIN);
			else
			bcm2835_gpio_clr(OUTPUT_PIN);
			// std::cout << timesrun;
			//std::cout<<resul.count();
			//std::cout << "TEST DONE" << std::endl;
		}
		if (timesrun == 1)
		bcm2835_close();
	}
	return 0;
	bcm2835_close();
}
