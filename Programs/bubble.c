#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <inttypes.h>

int  MAX =  79903;

int64_t start, end;
int64_t timeElapsed;

int list[100002];

void display() {
   int i;
   printf("[");

   for(i = 0; i < MAX; i++) {
      printf("%d ",list[i]);
   }

   printf("]\n");
}

void bubbleSort() {
   int temp;
   int i,j;

   bool swapped = false;


   for(i = 0; i < MAX-1; i++) {
      swapped = false;


      for(j = 0; j < MAX-1-i; j++) {

         if(list[j] > list[j+1]) {
            temp = list[j];
            list[j] = list[j+1];
            list[j+1] = temp;

            swapped = true;
         }

      }

      if(!swapped) {
         break;
      }

   }

}

int64_t printBubbleTime()
{
    struct timespec tms;


    if (clock_gettime(CLOCK_MONOTONIC,&tms)) {
        return -1;
    }

    int64_t micros = tms.tv_sec * 1000000;

    micros += tms.tv_nsec/1000;

    if (tms.tv_nsec % 1000 >= 500) {
        ++micros;
    }
    printf("Microseconds: %"PRId64"\n",micros);
    return micros;
}

int main(int argc , char *argv[]) {
    MAX = atoi(argv[1]);
    nice(atoi(argv[2]));
   int i;
   printf("Start Bubble ");
   start = printBubbleTime();
   for (i=0; i<MAX; i++)
   {
      list[i] = MAX - i;
   }

   bubbleSort();

   printf("End Bubble ");
   end = printBubbleTime();

   timeElapsed =  end - start;
   printf("bubble total : %"PRId64" microseconds , %f seconds\n", timeElapsed, (double)timeElapsed/1000000);

}
