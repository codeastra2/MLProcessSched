// Merge Sort - O(n log n)

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <inttypes.h>


#define INPUT_SIZE 10
#define NICE_VALUE 0

long long  *a;
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
    struct timespec tms;
    if (clock_gettime(CLOCK_MONOTONIC,&tms))
        return -1;
    int64_t micros = tms.tv_sec * 1000000;
    micros += tms.tv_nsec/1000;
    if (tms.tv_nsec % 1000 >= 500)
        ++micros;
    return micros;
}

void main() {
    nice(NICE_VALUE);

    a = malloc(INPUT_SIZE * sizeof(long long));

    for (long long i=0; i< INPUT_SIZE; i++)
        a[i] = rand() % 1000000;

    start = getTime();
    ms(0, INPUT_SIZE - 1);
    end = getTime();

    printf("ms,%"PRId64",%"PRId64",%"PRId64"\n",start,end,end - start);
}
