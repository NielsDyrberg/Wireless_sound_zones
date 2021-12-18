//
// Created by knham on 22-10-2021.
//
#ifndef C_SOUNDZONE_CLIENT_ALSADRIVER_H
#define C_SOUNDZONE_CLIENT_ALSADRIVER_H
#include "alsa/asoundlib.h"
#include "alsadriver.h"


class alsadriver {

    public:

        /*
         * Display the hardware setup if the alsa driver
         */
         void checksetup();
        /*
         * Starts playing music from FIFO buffer
         */
        void startstreaming(unsigned sampling_rate = 4000, int channels = 1, const char* bitformat = "SND_PCM_FORMAT_S16_LE");
        /*
         *  Used to define whether to read from buffer or not
         */
        volatile bool run_on = false;
        //std::atomic<bool> run_on = ATOMIC_VAR_INIT(true);

        void pause_play(int hw_pause);


    private:
        // Variables used for running the alsa driver
        snd_pcm_format_t format;
        snd_pcm_hw_params_t *params;
        snd_pcm_t *handle;
        snd_pcm_uframes_t frames;

        /*
         * Converts bitformat to corresponding enum
         */
        void CharToFormat(const char* bitformat);



};



#endif //C_SOUNDZONE_CLIENT_ALSADRIVER_H
