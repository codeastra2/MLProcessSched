// Matrix multiplication - O(n^3)

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <stdint.h>
#include <inttypes.h>

long long INPUTSIZE, first[10000][10000], second[10000][10000], multiply[10000][10000];
int64_t start,end;

void mat() {
    long long m, n, p, q, c, d, k, sum = 0;
    long long randomNumber = 0;

    for (c = 0; c < INPUTSIZE; c++) {
        for (d = 0; d < INPUTSIZE; d++) {
            for (k = 0; k < INPUTSIZE; k++) {
                randomNumber = rand() % 1000000;
                sum = sum + randomNumber * randomNumber;
            }
            multiply[c][d] = sum;
            sum = 0;
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

    start = getTime();
    mat();
    end = getTime();

    printf("mat,%lld,%"PRId64",%"PRId64",%"PRId64"\n",INPUTSIZE,start,end,end - start);
}