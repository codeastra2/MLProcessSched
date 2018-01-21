// Bubble sort - O(n^2)

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <inttypes.h>

long long INPUTSIZE, arr[1000000];
int64_t start,end;

void bub() {
    long long i,j,temp;
    bool swapped = false;

    for(i = 0; i < INPUTSIZE-1; i++) {
        swapped = false;
        for(j = 0; j < INPUTSIZE-1-i; j++) {
            if(arr[j] > arr[j+1]) {
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
                swapped = true;
            }
        }
        if(!swapped) {
            break;
        }
    }
}

int64_t getTime() {
    struct timespec tms;
    if (clock_gettime(CLOCK_MONOTONIC,&tms))
        return -1;
    int64_t micros = tms.tv_sec * 1000000;
    micros += tms.tv_nsec/1000;
    if (tms.tv_nsec % 1000 >= 500)
        ++micros;
    return micros;
}

void main(int argc, char *argv[]) {
    INPUTSIZE = atoi(argv[1]);
    nice(atoi(argv[2]));

    for (long long i=0; i< INPUTSIZE; i++)
        arr[i] = rand() % 1000000;

    start = getTime();
    bub();
    end = getTime();

    printf("bub,%lld,%"PRId64",%"PRId64",%"PRId64"\n",INPUTSIZE,start,end,end - start);
}