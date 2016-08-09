using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace problem_3
{
  internal class Program
  {
    private static void Main(string[] args)
    {
      Console.WriteLine(largest_prime_factor(600851475143));
      Console.Read();
    }

    private static long largest_prime_factor(long composite)
    {
      long result = 0;

      for (long i = (long)Math.Sqrt((double)composite); i >= 0; i--)
      {
        if (isPrime(i) == true)
        {
          if (composite % i == 0)
          {
            result = i;
            break;
          }
        }
      }

      return result;
    }

    //determine if prime
    private static bool isPrime(long num)
    {
      long length = (long)Math.Sqrt((double)num);

      for (long i = 2; i <= length; i++)
      {
        if (num % i == 0)
          return false;
      }
      return true;
    }
  }
}