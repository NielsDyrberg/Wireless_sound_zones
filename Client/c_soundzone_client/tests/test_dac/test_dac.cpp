//
// Created by KlausHammer on 27-10-2021.
//
#include <iostream>
#include "../../include/alsadriver.h"
#include <thread>
#include <functional>

using namespace std;
//alsadriver * dacdriver = new alsadriver;
alsadriver dacdriver;

int main(){
    /* Starts a thread of alsadriver.startstreaming. Must have variables declared when called */
    //thread t(&alsadriver::startstreaming, dacdriver,44100, 2, "SND_PCM_FORMAT_S16_LE");
    //thread t(bind(&alsadriver::startstreaming, dacdriver,44100, 2, "SND_PCM_FORMAT_S16_LE"));
    //&alsadriver::checksetup;
    //t.join();
    //delete dacdriver;
    //dacdriver.SetVolume();
    //dacdriver.checksetup();
    dacdriver.startstreaming();
    //dacdriver.SetVolume();




    return 0;
}