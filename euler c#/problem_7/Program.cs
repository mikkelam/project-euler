using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace problem_7
{
  internal class Program
  {
    private static void Main(string[] args)
    {
      Console.WriteLine(nr_prime(10001));
      Console.Read();
    }

    static private int nr_prime(int num)
    {
      int[] primes = new int[num];
      int i, j;

      for (i = 2, j = 0; j <= num - 1; i++)
      {
        if (isPrime(i) == true)
        {
          primes[j] = i;
          j++;
        }
      }
      return primes[j - 1];
    }

    //determine if prime
    private static bool isPrime(int num)
    {
      int length = (int)Math.Sqrt((double)num);

      for (int i = 2; i <= length; i++)
      {
        if (num % i == 0)
          return false;
      }
      return true;
    }
  }
}