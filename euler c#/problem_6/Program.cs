using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace problem_6
{
  internal class Program
  {
    private static void Main(string[] args)
    {
      Console.WriteLine(diff_Sum(1000));
      Console.Read();
    }

    static private long diff_Sum(long numbers)
    {
      long sqAll = 0, sqOne = 0, result = 0;
      for (long i = 0; i <= numbers; i++)
      {
        sqAll += i;
        sqOne += (long)Math.Pow((double)i, (double)2);
      }

      sqAll = (long)Math.Pow((double)sqAll, (double)2);

      result = sqAll - sqOne;

      return result;
    }
  }
}