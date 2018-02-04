// Heap Sort - O(n log n)

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <inttypes.h>

#define INPUT_SIZE 10
#define NICE_VALUE 0

long long *a;
int64_t start,end;

void hs() {
    long long i, j, c, root, temp;
    for (i = 1; i < INPUT_SIZE; i++) {
        c = i;
        do {
            root = (c - 1) / 2;
            if (a[root] < a[c]) {
                temp = a[root];
                a[root] = a[c];
                a[c] = temp;
            }
            c = root;
        } while (c != 0);
    }

    for (j = INPUT_SIZE - 1; j >= 0; j--) {
        temp = a[0];
        a[0] = a[j];
        a[j] = temp;
        root = 0;
        do {
            c = 2 * root + 1;
            if ((a[c] < a[c + 1]) && c < j-1)
                c++;
            if (a[root]<a[c] && c<j)  {
                temp = a[root];
                a[root] = a[c];
                a[c] = temp;
            }
            root = c;
        } while (c < j);
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

	a = malloc(INPUT_SIZE * sizeof(int));
    for (long long i = 0; i < INPUT_SIZE; i++)
        a[i] = rand() % 1000000;

    start = getTime();
    hs();
    end = getTime();

    printf("hs,%"PRId64",%"PRId64",%"PRId64"\n",start,end,end - start);
}
