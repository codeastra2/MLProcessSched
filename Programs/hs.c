// Heap Sort - O(n log n)

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <inttypes.h>

long long INPUTSIZE, heap[1000000];
int64_t start,end;

void hs() {
    long long i, j, c, root, temp;
    for (i = 1; i < INPUTSIZE; i++) {
        c = i;
        do {
            root = (c - 1) / 2;
            if (heap[root] < heap[c]) {
                temp = heap[root];
                heap[root] = heap[c];
                heap[c] = temp;
            }
            c = root;
        } while (c != 0);
    }

    for (j = INPUTSIZE - 1; j >= 0; j--) {
        temp = heap[0];
        heap[0] = heap[j];
        heap[j] = temp;
        root = 0;
        do {
            c = 2 * root + 1;
            if ((heap[c] < heap[c + 1]) && c < j-1)
                c++;
            if (heap[root]<heap[c] && c<j)  {
                temp = heap[root];
                heap[root] = heap[c];
                heap[c] = temp;
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

void main(int argc, char *argv[]) {
    INPUTSIZE = atoi(argv[1]);
    nice(atoi(argv[2]));

    for (long long i = 0; i < INPUTSIZE; i++)
        heap[i] = rand() % 1000000;

    start = getTime();
    hs();
    end = getTime();

    printf("hs,%lld,%"PRId64",%"PRId64",%"PRId64"\n",INPUTSIZE,start,end,end - start);
}