//
// Created by KlausHammer on 27-10-2021.
//
#include <iostream>
#include "../../include/alsadriver.h"
#include <thread>
#include <functional>
#include <bcm2835.h>

using namespace std;
alsadriver * dacdriver = new alsadriver; // Vigtigt at der laves en pointer til objected, da ellers er det ikke muligt at opdatere en object variable udenfor tråden.

#define INPUT_PIN RPI_V2_GPIO_P1_37 // Define Input pin


int main() {
    bool firstrun = false;
    /* Starts a thread of alsadriver.startstreaming. Must have variables declared when called */
    thread t (&alsadriver::startstreaming, dacdriver, 2000, 1, "SND_PCM_FORMAT_S16_LE");
    if (!bcm2835_init())return 1;
    { /* Initialize */
        bcm2835_gpio_fsel(INPUT_PIN, BCM2835_GPIO_FSEL_INPT); // Set INPUT_PIN to be an input
        bcm2835_gpio_set_pud(INPUT_PIN, BCM2835_GPIO_PUD_DOWN);  //  with a down
        //bcm2835_gpio_ren(INPUT_PIN);  // And a high detect enable
    }

    while (!firstrun) {
        while (bcm2835_gpio_lev(INPUT_PIN)) {
            if (!firstrun) {
                dacdriver->run_on = true;

                firstrun = true;
            }
        }

    }
    bcm2835_close();
    return 0;



}

// OLD (creates a new instance of the thread when pin is high)
//int main() {
//    bool firstrun = false;
//    thread t;
//    if (!bcm2835_init())return 1;
//    { /* Initialize */
//        bcm2835_gpio_fsel(INPUT_PIN, BCM2835_GPIO_FSEL_INPT); // Set INPUT_PIN to be an input
//        bcm2835_gpio_set_pud(INPUT_PIN, BCM2835_GPIO_PUD_DOWN);  //  with a down
//        //bcm2835_gpio_ren(INPUT_PIN);  // And a high detect enable
//    }
//
//    while (!firstrun) {
//        while (bcm2835_gpio_lev(INPUT_PIN)) {
//
//            /* Starts a thread of alsadriver.startstreaming. Must have variables declared when called */
//            if (!firstrun)
//                t = thread(&alsadriver::startstreaming, dacdriver, 2000, 1, "SND_PCM_FORMAT_S16_LE");
//
//            firstrun = true;
//        }
//
//    }
//    bcm2835_close();
//    return 0;
//
//
//    //thread t(&alsadriver::startstreaming, dacdriver, 2000, 1, "SND_PCM_FORMAT_S16_LE");
//    //this_thread::sleep_for(std::chrono::milliseconds(5000));
//
//
//    //t.join();
//
//
//}
