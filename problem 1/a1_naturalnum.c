//http://projecteuler.net/problem=1


#include <stdio.h>
#define count 1000

int main(void)
{
  long int num, mult[500];
  long int i, j=0, result=0;



for (i = 0; i < count; i += 1)
{
  if (i%3==0 || i%5==0)
  {
    mult[j]= i;
    j++;
  }
}

for (i = 0; i < j; i += 1)
{
  result += mult[i];
}

  
  

  printf("\n sum of multiples of 3 and 5 below 1000 is %ld", result);

return 0;
}
