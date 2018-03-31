// Heap Sort - O(n log n)

#include <stdio.h>
#include <inttypes.h>
#include <stdlib.h>
#include <sys/time.h>
#include <unistd.h>

#define INPUT_SIZE 30474
#define NICE_VALUE 14

#define METHOD_1 15, 17
#define METHOD_2 18, 20
#define METHOD_3 21, 23, 25, 27

static long long a[INPUT_SIZE];

/*
long long a[INPUT_SIZE];
*/
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

void heapify(long long n, long long i, long long a[]) {
    long long largest = i;
    long long l = 2*i + 1;
    long long r = 2*i + 2;

    if (l < n && a[l] > a[largest])
        largest = l;

    if (r < n && a[r] > a[largest])
        largest = r;

    if (largest != i) {
        long long temp = a[i];
        a[i] = a[largest];
        a[largest] = temp;
        heapify(n, largest, a);
    }
}

void hs(long long n, long long a[]) {
    long long i;

    for (i = n/2 - 1; i >= 0; i--)
        heapify(n, i, a);

    for (i = n - 1; i>=0; i--) {
        long long temp = a[0];
        a[0] = a[i];
        a[i] = temp;
        heapify(i, 0, a);
    }
}

int64_t getTime() {
    gettimeofday(&time, NULL);
    return time.tv_sec * 1000000 + time.tv_usec;
}

void main() {
    nice(NICE_VALUE);
    
    allocate();

    for (long long i = 0; i < INPUT_SIZE; i++)
        a[i] = rand() % 1000000;

    start = getTime();
    hs(INPUT_SIZE, a);
    end = getTime();

    printf("hs,%"PRId64",%"PRId64",%"PRId64"\n", start, end, end - start);
}
