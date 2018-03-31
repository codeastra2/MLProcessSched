// Matrix multiplication - O(n^3)

#include <stdio.h>
#include <inttypes.h>
#include <stdlib.h>
#include <sys/time.h>
#include <unistd.h>

#define INPUT_SIZE 100
#define NICE_VALUE -18

struct timeval time;
int64_t start,end;

int64_t getTime() {
    gettimeofday(&time, NULL);
    return time.tv_sec * 1000000 + time.tv_usec;
}

void mat() {
    long i, j, k;

    long **m1 = (long **)malloc(INPUT_SIZE * sizeof(long *));
    long **m2 = (long **)malloc(INPUT_SIZE * sizeof(long *));
    long **m3 = (long **)malloc(INPUT_SIZE * sizeof(long *));

    for (i=0; i<INPUT_SIZE; i++) {
        m1[i] = (long *)malloc(INPUT_SIZE * sizeof(long));
        m2[i] = (long *)malloc(INPUT_SIZE * sizeof(long));
        m3[i] = (long *)malloc(INPUT_SIZE * sizeof(long));
    }

    for(i = 0 ; i < INPUT_SIZE ; i++) {
        for(j =0 ; j < INPUT_SIZE ; j++) {
            m1[i][j] = rand() % 1000000;
            m2[i][j] = rand() % 1000000;
        }
    }

    start = getTime();
    for (i = 0; i < INPUT_SIZE; i++) {
        for (j = 0; j < INPUT_SIZE; j++) {
            m3[i][j] = 0;
            for (k = 0; k < INPUT_SIZE; k++) {
                m3[i][j] += m1[i][k] + m2[k][j];
            }
        }
    }
    end = getTime();
}

void main() {
    nice(NICE_VALUE);

    mat();

    printf("mat,%"PRId64",%"PRId64",%"PRId64"\n", start, end, end - start);
}
