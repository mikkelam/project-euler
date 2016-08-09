using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace problem_12
{
  internal class Program
  {
    private static void Main(string[] args)
    {
      Console.WriteLine(triangle(3));
      Console.Read();
    }

    private static long triangle(long divisors)
    {
      List<long> divArray = new List<long>();

      long triangle = 0;
      for (long i = 1; ; i++)
      {
        triangle += i;

        for (long j = 1; j <= triangle; j++)
        {
          if (triangle % j == 0)
          {
            divArray.Add(j);
          }
        }
        if (divArray.Count() > divisors)
        {
          break;
        }
        divArray.Clear();
      }
      return triangle;
    }
  }
}