// Fibonacci numbers using dynamic programming - O(n)

#include <stdio.h>
#include <inttypes.h>
#include <stdlib.h>
#include <sys/time.h>
#include <unistd.h>

#define INPUT_SIZE 2362
#define NICE_VALUE -12

#define METHOD_1 15, 17
#define METHOD_2 18, 20
#define METHOD_3 21, 23, 25, 27
/*
static long long res[20000];
*/
/*
long long res[20000];
*/

long long *res;

void allocate(){

    res = malloc(20000 * sizeof(long long));

}

struct timeval time;
int64_t start,end;

long long multiply(long long x, long long res[], long long res_size){
    long long carry = 0;
    for (long long i=0; i<res_size; i++){
        long long prod = res[i] * x + carry;
        res[i] = prod % 10;
        carry  = prod/10;
    }
    while (carry){
        res[res_size] = carry%10;
        carry = carry/10;
        res_size++;
    }
    return res_size;
}

void fac(long long n){
    res[0] = 1;
    long long res_size = 1, i;
 
    for (long long i=2; i<n; i++)
        res_size = multiply(i, res, res_size);

    //Result
    //for (long long i=res_size-1; i>=0; i--)
    //    printf("%lld", res[i]);
}

int64_t getTime() {
    gettimeofday(&time, NULL);
    return time.tv_sec * 1000000 + time.tv_usec;
}

int main (){
    nice(NICE_VALUE);

    allocate();
    
    start = getTime();
    fac(INPUT_SIZE+1);
    end = getTime();

    printf("fac,%"PRId64",%"PRId64",%"PRId64"\n", start, end, end - start);
}