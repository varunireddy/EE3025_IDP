#include <assert.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#define q	3		      /* for 2^3 points */
#define N	(1<<q)		/* N-point FFT*/

typedef float real;
typedef struct{real Re; real Im;} complex;

#ifndef PI
# define PI	3.14159265358979323846264338327950288
#endif


/* Print a vector of complexes as ordered pairs. */
static void print_vector(const char *title, complex *x, int n)
{
  int i;
  printf("%s (dim=%d):", title, n);
  for(i=0; i<n; i++ ) printf(" %5.3f,%5.3f ", x[i].Re,x[i].Im);
  putchar('\n');
  return;
}

void fft( complex *v, int n, complex *tmp )
{
  if(n>1) {			             /* otherwise, do nothing and return */
    int k,m; complex z, w, *vo, *ve;
    ve = tmp; vo = tmp+n/2;
    for(k=0; k<n/2; k++) {
      ve[k] = v[2*k];
      vo[k] = v[2*k+1];
    }
    fft(ve, n/2, v);	 	/* FFT on even-indexed elements of v[] */
    fft(vo, n/2, v);		/* FFT on odd-indexed elements of v[] */
    for(m=0; m<n/2; m++) {
      w.Re = cos(2*PI*m/(double)n);
      w.Im = -sin(2*PI*m/(double)n);
      z.Re = w.Re*vo[m].Re - w.Im*vo[m].Im;	/* Re(w*vo[m]) */
      z.Im = w.Re*vo[m].Im + w.Im*vo[m].Re;	/* Im(w*vo[m]) */
      v[  m  ].Re = ve[m].Re + z.Re;
      v[  m  ].Im = ve[m].Im + z.Im;
      v[m+n/2].Re = ve[m].Re - z.Re;
      v[m+n/2].Im = ve[m].Im - z.Im;
    }
  }
  return;
}
int main(void)
{
  FILE *f = fopen("fft_values.dat", "wb");    
  complex v[N], temp[N];
  int k;
  float x[]= {1,2,3,4,4,3,2,1};
  for(k=0; k<N; k++) {
    v[k].Re = x[k];
    v[k].Im = 0;
  }
  print_vector("Orig", v, N);
  fft( v, N, temp);
  print_vector(" FFT", v, N);
  float realv[N];
  float imagv[N];
  for(int k=0;k<N;k++){
      realv[k] = v[k].Re;
      imagv[k] = v[k].Im;                  
  }
  fwrite(realv, sizeof(float), N, f);   /*Writing real and imaginary values in a .dat file*/
  fwrite(imagv, sizeof(float), N, f);
  fclose(f);
  exit(EXIT_SUCCESS);
}