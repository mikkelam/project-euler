using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace problem_10
{
  internal class Program
  {
    private static void Main(string[] args)
    {
      Console.WriteLine(primesum(2000000));
      Console.Read();
    }

    private static long primesum(long num)
    {
      long result = 0;
      List<long> primes = new List<long>();

      for (long i = 2; i < num; i++)
      {
        if (isPrime(i) == true)
        {
          primes.Add(i);
        }
      }
      for (long i = 0; i < primes.Count(); i++)
      {
        result += primes[(int)i];
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