// Bubble sort - O(n^2)

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <inttypes.h>

#define INPUT_SIZE 10
#define NICE_VALUE 0

long long *a;
int64_t start,end;

void bub() {
    long long i,j,temp;
    bool swapped = false;

    for(i = 0; i < INPUT_SIZE-1; i++) {
        swapped = false;
        for(j = 0; j < INPUT_SIZE-1-i; j++) {
            if(a[j] > a[j+1]) {
                temp = a[j];
                a[j] = a[j+1];
                a[j+1] = temp;
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

void main() {
    nice(NICE_VALUE);

	a = malloc (INPUT_SIZE * sizeof(int));
    for (long long i=0; i< INPUT_SIZE; i++)
        a[i] = rand() % 1000000;

    start = getTime();
    bub();
    end = getTime();

    printf("bub,%"PRId64",%"PRId64",%"PRId64"\n",start,end,end - start);
}
