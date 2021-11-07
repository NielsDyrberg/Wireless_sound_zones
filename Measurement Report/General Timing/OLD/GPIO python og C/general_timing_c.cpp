// file input.c
// sudo g++ general_timing_c.c -o generaltiming  -lbcm2835 // Compiles program
// chmod +x myfirstcprogram // Make program executable
// sudo nice -n -20 ./generaltiming // Use to run high priority

/* INSTALL BCM2835
cd /home/pi/
wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.70.tar.gz
tar zxvf bcm2835-1.70.tar.gz
cd bcm2835-1.70
./configure
make
sudo make check
sudo make install
*/




/*
     RPI_V2_GPIO_P1_03     =  2,
     RPI_V2_GPIO_P1_05     =  3,
     RPI_V2_GPIO_P1_07     =  4,
     RPI_V2_GPIO_P1_08     = 14,
     RPI_V2_GPIO_P1_10     = 15,
     RPI_V2_GPIO_P1_11     = 17,
     RPI_V2_GPIO_P1_12     = 18,
     RPI_V2_GPIO_P1_13     = 27,
     RPI_V2_GPIO_P1_15     = 22,
     RPI_V2_GPIO_P1_16     = 23,
     RPI_V2_GPIO_P1_18     = 24,
     RPI_V2_GPIO_P1_19     = 10,
     RPI_V2_GPIO_P1_21     =  9,
     RPI_V2_GPIO_P1_22     = 25,
     RPI_V2_GPIO_P1_23     = 11,
     RPI_V2_GPIO_P1_24     =  8,
     RPI_V2_GPIO_P1_26     =  7,
     RPI_V2_GPIO_P1_29     =  5,
     RPI_V2_GPIO_P1_31     =  6,
     RPI_V2_GPIO_P1_32     = 12,
     RPI_V2_GPIO_P1_33     = 13,
     RPI_V2_GPIO_P1_35     = 19,
     RPI_V2_GPIO_P1_36     = 16,
     RPI_V2_GPIO_P1_37     = 26,
     RPI_V2_GPIO_P1_38     = 20,
     RPI_V2_GPIO_P1_40     = 21,

*/




#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <chrono>
#include <bcm2835.h>

using namespace std;
bool state = 0;



#define OUTPUT_PIN RPI_V2_GPIO_P1_40 // Define output pin
#define INPUT_PIN RPI_V2_GPIO_P1_37 // Define Input pin


int main(){
	if(!bcm2835_init())return 1;{ /* Initialize */
	bcm2835_gpio_fsel(OUTPUT_PIN, BCM2835_GPIO_FSEL_OUTP); /*Sets OUTPUT_PIN to output*/
    bcm2835_gpio_fsel(INPUT_PIN, BCM2835_GPIO_FSEL_INPT); // Set INPUT_PIN to be an input
    bcm2835_gpio_set_pud(INPUT_PIN, BCM2835_GPIO_PUD_DOWN);  //  with a down
    bcm2835_gpio_ren(INPUT_PIN);  // And a high detect enable
	}
    bcm2835_gpio_clr(OUTPUT_PIN);

    while (1)
    {
        if (bcm2835_gpio_eds(INPUT_PIN))
        {
            // Now clear the eds flag by setting it to 1
            bcm2835_gpio_set_eds(INPUT_PIN);
            state =! state;
            if (state)
                bcm2835_gpio_set(OUTPUT_PIN);
            else
                bcm2835_gpio_clr(OUTPUT_PIN);

        }

    }

    bcm2835_close();
    return 0;

}