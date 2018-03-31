// Fibonacci Series - O(2^n)

#include <stdio.h>
#include <inttypes.h>
#include <stdlib.h>
#include <sys/time.h>
#include <unistd.h>

#define INPUT_SIZE 35
#define NICE_VALUE 18

#define METHOD_1 15, 17
#define METHOD_2 18, 20
#define METHOD_3 21, 23, 25, 27



/*

*/
/*

*/
void allocate(){
/*

*/
}

struct timeval time;
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
    gettimeofday(&time, NULL);
    return time.tv_sec * 1000000 + time.tv_usec;
}

void main() {
    nice(NICE_VALUE);

    start = getTime();
    for (long long i = 1 ; i <= INPUT_SIZE ; i++ )
        fib(i);
    end = getTime();

    printf("fib,%"PRId64",%"PRId64",%"PRId64"\n", start, end, end - start);
}
