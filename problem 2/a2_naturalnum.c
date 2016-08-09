//http://projecteuler.net/problem=2


#include <stdio.h>


int main(void)
{
  long int num, prev_num, fibonacci[40000];
  long int i=2, j, result=0;


  fibonacci[0]=1;
  fibonacci[1]=1;
  printf("\nFibbonacci <number: 0 is: %ld", fibonacci[0]);
  printf("\nFibbonacci <number: 1 is: %ld", fibonacci[1]);
  while ((fibonacci[i-1] + fibonacci[i-2])<=4000000 && (fibonacci[i-1] + fibonacci[i-2])>0)
  {
    fibonacci[i] = fibonacci[i-1] + fibonacci[i-2];
    printf("\nFibbonacci <number: %ld is: %ld", i, fibonacci[i]);
     
    i++;
  }


  for (j=0;j<i;j++)
  {
  
  if ((fibonacci[j]%2)==0)
  {
    printf("\n j is: %ld", j);
    result +=fibonacci[j];
  }
  
  }

  printf("\n sum of even fib numbers: %ld", result);

return 0;
}
