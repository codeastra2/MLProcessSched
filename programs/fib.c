// Fibonacci Series - O(2^n)

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <inttypes.h>

long long INPUT_SIZE;
int64_t start,end;

int fib(int n) {
    if ( n == 0 )
        return 0;
    else if ( n == 1 )
        return 1;
    else
        return fib(n-1) + fib(n-2);
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
    INPUT_SIZE = atoi(argv[1]);
    nice(atoi(argv[2]));

    start = getTime();
    for (long long i = 1 ; i <= INPUT_SIZE ; i++ )
        fib(i);
    end = getTime();

    printf("fib,%"PRId64",%"PRId64",%"PRId64"\n",start,end,end - start);
}
