//http://projecteuler.net/problem=3


#include <stdio.h>
#include <math.h>



int main(void)
{
  int number = 600851475;
  int array[number];
  
  for (unsigned long int i = 2; i <= number; i += 1)
  {
    array[i]=1;
  }
  
  
  for (i = 2; i <= sqrt(number) ; i += 1)
  {
    if (array[i]==1)
    {
      for (unsigned long int j = 2; j <=number += 1)
      {
        array[j*i]=0;
      }
      
    }
  }
 
  unsigned long int largest =0;
  
  for (i = 2; i <= numb; i += 1)
  {
    if (array[i]==1)
    {
      largest= i;
    } 
  }
  
  printf("largest: %u",largest)
  

 






return 0;
}
