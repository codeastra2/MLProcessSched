// Merge Sort - O(n log n)

#include <stdio.h>
#include <inttypes.h>
#include <stdlib.h>
#include <sys/time.h>
#include <unistd.h>

#define INPUT_SIZE 100000
#define NICE_VALUE 18

#define METHOD_1 15, 17
#define METHOD_2 18, 20
#define METHOD_3 21, 23, 25, 27
/*
static long long a[INPUT_SIZE];
*/

long long a[INPUT_SIZE];

/*
long long *a;
*/
void allocate(){
/*
    a = malloc (INPUT_SIZE * sizeof(long long));
*/
}

struct timeval time;
int64_t start,end;

void merge(long long l, long long m, long long r) {
    long long i, j, k, n1, n2;
    n1 = m - l + 1;
    n2 =  r - m;

    long long L[n1], R[n2];

    for (i = 0; i < n1; i++)
        L[i] = a[l + i];
    for (j = 0; j < n2; j++)
        R[j] = a[m + 1+ j];

    i = 0;
    j = 0;
    k = l;
    while (i < n1 && j < n2)
        if (L[i] <= R[j])
            a[k++] = L[i++];
        else
            a[k++] = R[j++];
    while (i < n1)
        a[k++] = L[i++];
    while (j < n2)
        a[k++] = R[j++];
}

void ms(long long l, long long r) {
    if (l < r) {
        long long m = l+(r-l)/2;
        ms(l, m);
        ms(m+1, r);
        merge(l, m, r);
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
    ms(0, INPUT_SIZE - 1);
    end = getTime();

    printf("ms,%"PRId64",%"PRId64",%"PRId64"\n",start,end,end - start);
}
