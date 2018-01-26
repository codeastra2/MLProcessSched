// Matrix multiplication - O(n^3)

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <stdint.h>
#include <inttypes.h>

long INPUT_SIZE;
int64_t start,end;

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

void mat() {
    long i, j, k;

	long **m1 = (long **)malloc(INPUT_SIZE * sizeof(long *));
	long **m2 = (long **)malloc(INPUT_SIZE * sizeof(long *));
	long **m3 = (long **)malloc(INPUT_SIZE * sizeof(long *));
	
	for (i=0; i<INPUT_SIZE; i++){
		m1[i] = (long *)malloc(INPUT_SIZE * sizeof(long));
        m2[i] = (long *)malloc(INPUT_SIZE * sizeof(long));
		m3[i] = (long *)malloc(INPUT_SIZE * sizeof(long));
	}
	
	for(i = 0 ; i < INPUT_SIZE ; i++){
		for(j =0 ; j < INPUT_SIZE ; j++){
			m1[i][j] = rand() % 1000000;
			m2[i][j] = rand() % 1000000;
		}
	}

	start = getTime();
    for (i = 0; i < INPUT_SIZE; i++) {
        for (j = 0; j < INPUT_SIZE; j++) {
			m3[i][j] = 0;
            for (k = 0; k < INPUT_SIZE; k++) {                
                m3[i][j] += m1[i][j] + m2[i][j];
            }
        }
    }
	end = getTime();
}

void main(int argc, char *argv[]) {
    INPUT_SIZE = atoi(argv[1]);
    nice(atoi(argv[2]));

    mat();

    printf("mat,%"PRId64",%"PRId64",%"PRId64"\n",start,end,end - start);
}
