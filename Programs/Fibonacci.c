#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <inttypes.h>
int INPUTSIZE = 20;

int64_t start, end;
int64_t timeElapsed;
double i = 0, c;


double Fibonacci(double n)
{
   if ( n == 0 )
      return 0;
   else if ( n == 1 )
      return 1;
   else
   {
      return ( Fibonacci(n-1) + Fibonacci(n-2) );
   }
}

int64_t printFibonacciTime()
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

double main(int argc, char *argv[])
{
   INPUTSIZE = atoi(argv[1]);
   nice(atoi(argv[2]));

   printf("Start Fibo ");
   start = printFibonacciTime();
   for ( c = 1 ; c <= INPUTSIZE ; c++ )
   {
      Fibonacci(i);
      i++;
   }

   printf("End Fibo ");
   end = printFibonacciTime();

   timeElapsed =  end - start;
   printf("Fibo total : %"PRId64" microseconds , %f seconds\n", timeElapsed, (double)timeElapsed/1000000);
    return 0;

}
