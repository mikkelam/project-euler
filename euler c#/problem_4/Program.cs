using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace problem_4
{
  internal class Program
  {
    private static void Main(string[] args)
    {
      Console.WriteLine(ProductPalindrome(100));

      Console.Read();
    }

    private static bool ispalindrome(int x, int y)
    {
      int xy = x * y;

      string xys = xy.ToString();
      int len = xys.Count();
      bool result = false;

      for (int i = 0, j = len - 1; i <= j; i++, j--)
      {
        if (xys[i] != xys[j])
        {
          result = false;
          break;
        }

        else
        {
          result = true;
        }
      }

      return result;
    }

    //input: Largest number in the digit range e.g. 3 digits, length=999
    private static int ProductPalindrome(int length)
    {
      int result = 0;
      int j, i;

      for (i = 1; i <= length; i++)
      {
        for (j = 1; j <= length; j++)
        {
          if (ispalindrome(i, j) == true)
          {
            if (j * i > result)
            {
              result = j * i;
            }
          }
        }
      }

      return result;
    }
  }
}