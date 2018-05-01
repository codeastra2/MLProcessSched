// Matrix multiplication - O(n^3)

#include <stdio.h>
#include <inttypes.h>
#include <stdlib.h>
#include <sys/time.h>
#include <unistd.h>

#define INPUT_SIZE 308
#define NICE_VALUE -13

#define METHOD_1 15, 17
#define METHOD_2 18, 20
#define METHOD_3 21, 23, 25, 29

static long m3[INPUT_SIZE][INPUT_SIZE];

/*
long m3[INPUT_SIZE][INPUT_SIZE];
*/
/*
long **m3;
*/
void allocate(){
/*
    m3 = (long **)malloc(INPUT_SIZE * sizeof(long *));
    for (int i=0; i<INPUT_SIZE; i++) 
        m3[i] = (long *)malloc(INPUT_SIZE * sizeof(long));
*/
}

long m1[INPUT_SIZE][INPUT_SIZE];
long m2[INPUT_SIZE][INPUT_SIZE];

struct timeval time;
int64_t start,end;

int64_t getTime() {
    gettimeofday(&time, NULL);
    return time.tv_sec * 1000000 + time.tv_usec;
}

void mat() {
    long i, j, k;
    
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
    
    allocate();

    mat();

    printf("mat,%"PRId64",%"PRId64",%"PRId64"\n", start, end, end - start);
}
