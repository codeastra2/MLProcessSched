#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <stdint.h>
#include <inttypes.h>
int INPUTSIZE = 1500;

  long long m, n, p, q, c, d, k, sum = 0;
  long long mat1_row, mat1_col, mat2_row, mat2_col = 0;
  long long randomNumber = 0;
  long long first[2000][2000], second[2000][2000], multiply[2000][2000];
  int64_t start, end;

  int64_t timeElapsed;



void MatrixMultiplication()
{
  mat1_row = mat1_col = mat2_row = mat2_col = INPUTSIZE;

    for (c = 0; c < mat1_row; c++) {
      for (d = 0; d < mat2_col; d++) {

        for (k = 0; k < mat2_row; k++) {
            randomNumber = rand() % 1000;
          sum = sum + randomNumber * randomNumber;
        }

        multiply[c][d] = sum;
        sum = 0;
      }
    }
}

int64_t printMatrixTime()
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

double main(int argc , char *argv[])
{

  INPUTSIZE = atoi(argv[1]);
  nice(atoi(argv[2]));
  printf("Start Matrix Mul ");
  start = printMatrixTime();

  MatrixMultiplication();

  printf("End Matrix Mul ");
  end = printMatrixTime();


  timeElapsed =  end - start;
  printf("Matrix total : %"PRId64" microseconds , %f seconds\n", timeElapsed, (double)timeElapsed/1000000);

  return 0;

}
