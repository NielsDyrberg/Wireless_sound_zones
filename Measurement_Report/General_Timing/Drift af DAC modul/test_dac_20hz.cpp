//
// Created by KlausHammer on 27-10-2021.
// g++ test_dac_20hz.cpp -o test_dac_jitter -lbcm2835 -lasound -lpthread
#include <iostream>
#include "alsa/asoundlib.h"
#include <thread>
#include <functional>
#include <bcm2835.h>

using namespace std;
bool run_on = false;

#define INPUT_PIN RPI_V2_GPIO_P1_37 // Define Input pin



void startstreaming(unsigned int sampling_rate, int channels, const char* bitformat) {

    snd_pcm_format_t format;
    snd_pcm_hw_params_t *params;
    snd_pcm_t *handle;
    snd_pcm_uframes_t frames;
    bool debug = true;
    int rc, dir;
    unsigned int val;
    char *buffer = nullptr;
    int buff_size;
    int readfd, readval = 0;
    const char* readbuffer = "firkant_100hz_mono_4k_5min.raw"; //"/home/pi/download/epic_sax_guy.raw";
//    CharToFormat(bitformat);
format = SND_PCM_FORMAT_S16_LE;

    /* Open PCM device for playback. */
    rc = snd_pcm_open(&handle, "default",SND_PCM_STREAM_PLAYBACK, 0);
    if (rc < 0) {
        fprintf(stderr,
                "unable to open pcm device: %s\n",
                snd_strerror(rc));
        exit(1);
    }

    /* Allocate a hardware parameters object. */
    snd_pcm_hw_params_alloca(&params);

    /* Fill it in with default values. */
    snd_pcm_hw_params_any(handle, params);

    /* Set the desired hardware parameters. */

    /* Interleaved mode */
    snd_pcm_hw_params_set_access(handle, params,SND_PCM_ACCESS_RW_INTERLEAVED);

    /* Set format  */
    snd_pcm_hw_params_set_format(handle, params, format);

    /* Set period size to 32 frames. */
    frames = 350; // 350 lavest den kan gå
    snd_pcm_hw_params_set_period_size_near(handle, params, &frames, &dir);



    /* Set number of channels */
    snd_pcm_hw_params_set_channels(handle, params, channels);



    /* Set the sampling rate */
    snd_pcm_hw_params_set_rate_near(handle, params, &sampling_rate, &dir);


    /* Write the parameters to the driver */
    rc = snd_pcm_hw_params(handle, params);
    if (rc < 0) {
        fprintf(stderr,
                "unable to set hw parameters: %s\n",
                snd_strerror(rc));
        exit(1);
    }

    /* Allocate buffer to hold single period */
    snd_pcm_hw_params_get_period_size(params, &frames, 0);
   // printf("frames: %d\n", (int)frames);

    buff_size = frames * channels * 2 /* 2 -> sample size */;
    buffer = (char *) malloc(buff_size);
    memset(buffer, 0, buff_size);


    readfd = open(readbuffer, O_RDONLY);
    if (readfd < 0) {
        printf("Error reading file");
        exit(1);
    }

    if (debug == 1) {


        printf("PCM name: '%s'\n", snd_pcm_name(handle));

        printf("PCM state: %s\n",  snd_pcm_state_name(snd_pcm_state(handle)));

        snd_pcm_hw_params_get_rate(params, &val, 0);
        printf("rate: %d bps\n", val);

        snd_pcm_hw_params_get_channels(params, &val);
        printf("channels: %i ", val);

        snd_pcm_hw_params_get_format(params, reinterpret_cast<snd_pcm_format_t *>(&val));
        printf("format = '%s' (%s)\n",
               snd_pcm_format_name((snd_pcm_format_t) val),
               snd_pcm_format_description(
                       (snd_pcm_format_t) val));

        printf("frames: %d\n", (int)frames);

        snd_pcm_hw_params_get_period_time(params, &val, NULL);
        printf("period time: %i ", val);


    }

    while (true) {
        while (run_on) {
            while ((readval = read(readfd, buffer, buff_size) > 0)) {
                if ((val = snd_pcm_writei(handle, buffer, frames) == -EPIPE)) {
                    fprintf(stderr, "Underrun!\n");
                    snd_pcm_prepare(handle);
                } else if (val < 0) {
                    fprintf(stderr, "Error writing to PCM device: %s\n", snd_strerror(val));
                }
            }
        }
    }
    snd_pcm_drain(handle);
    snd_pcm_close(handle);
    free(buffer);



}



int main() {
    bool firstrun = false;
    /* Starts a thread of alsadriver.startstreaming. Must have variables declared when called */
	thread t (startstreaming, 4000, 1, "SND_PCM_FORMAT_S16_LE");
        if (!bcm2835_init())return 1;
    { /* Initialize */
        bcm2835_gpio_fsel(INPUT_PIN, BCM2835_GPIO_FSEL_INPT); // Set INPUT_PIN to be an input
        bcm2835_gpio_set_pud(INPUT_PIN, BCM2835_GPIO_PUD_DOWN);  //  with a down
        //bcm2835_gpio_ren(INPUT_PIN);  // And a high detect enable
    }

    while (!firstrun) {
        while (bcm2835_gpio_lev(INPUT_PIN)) {
            if (!firstrun) {
                run_on = true;
                firstrun = true;
            }
        }

    }
    bcm2835_close();
    return 0;



}


