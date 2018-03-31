// Bubble sort - O(n^2)

#include <stdio.h>
#include <inttypes.h>
#include <stdlib.h>
#include <sys/time.h>
#include <unistd.h>

#define INPUT_SIZE 6666
#define NICE_VALUE -10

#define METHOD_1 15, 17
#define METHOD_2 18, 20
#define METHOD_3 21, 23, 25, 27
/*
static long long a[INPUT_SIZE];
*/
/*
long long a[INPUT_SIZE];
*/

long long *a;

void allocate(){

    a = malloc (INPUT_SIZE * sizeof(long long));

}

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

    allocate();

    for (long long i=0; i< INPUT_SIZE; i++)
        a[i] = rand() % 1000000;

    start = getTime();
    bub();
    end = getTime();

    printf("bub,%"PRId64",%"PRId64",%"PRId64"\n", start, end, end - start);
}