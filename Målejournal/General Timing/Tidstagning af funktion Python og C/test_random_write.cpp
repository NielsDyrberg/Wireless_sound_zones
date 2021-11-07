#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <chrono>

using namespace std;

// g++ test_random_write_c.c -o randomwrite // Compiles program
// chmod +x myfirstcprogram // Make program executable
// sudo nice -n -20 ./randomwrite // Use to run high priority

int random_array[100000];


void fillsarray_random() { // Ikke pålidelig da det meget forskelligt hvor langt tid det tager at udregne tale
    int arraysize = sizeof(random_array)/sizeof(random_array[0]);
    //cout << "Size of array is: " << arraysize;

    for (int i = 0; i <= arraysize; i++) {

        random_array[i] = rand();

      // cout << "Random number is: " << random_array[i];

    }

}

void fillsarray() {
    int arraysize = sizeof(random_array)/sizeof(random_array[0]);

    for (int i = 0; i <= arraysize; i++) {

        random_array[i] = (12345*(0.1*i)+(23*i));

      // cout << "Random number is: " << random_array[i];

    }

}


int main(){

    for (int i = 0; i <= 100; i++) {
        std::chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();
        for (int j = 0; j <= 100; j++) {
            fillsarray();
        }
        std::chrono::steady_clock::time_point end = std::chrono::steady_clock::now();
        cout << "\n " << std::chrono::duration_cast<std::chrono::microseconds>(end - begin).count();
    }
}
