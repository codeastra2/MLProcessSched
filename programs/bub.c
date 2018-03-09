// Bubble sort - O(n^2)

#include <stdio.h>
#include <inttypes.h>
#include <stdlib.h>
#include <sys/time.h>
#include <unistd.h>

#define INPUT_SIZE 1000
#define NICE_VALUE -18

long long *a;
struct timeval time;
int64_t start,end;

void bub() {
    long long i, j, temp;
    short swapped;

    for(i = 0; i < INPUT_SIZE-1; i++) {
        swapped = 0;
        for(j = 0; j < INPUT_SIZE-1-i; j++) {
            if(a[j] > a[j+1]) {
                temp = a[j];
                a[j] = a[j+1];
                a[j+1] = temp;
                swapped = 1;
            }
        }
        if(swapped == 0)
            return;
    }
}

int64_t getTime() {
    gettimeofday(&time, NULL);
    return time.tv_sec * 1000000 + time.tv_usec;
}

void main() {
    nice(NICE_VALUE);

    a = malloc (INPUT_SIZE * sizeof(long long));
    for (long long i=0; i< INPUT_SIZE; i++)
        a[i] = rand() % 1000000;

    start = getTime();
    bub();
    end = getTime();

    printf("bub,%"PRId64",%"PRId64",%"PRId64"\n", start, end, end - start);
}
