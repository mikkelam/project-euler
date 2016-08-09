using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace problem_11
{
  internal class Program
  {
    private static void Main(string[] args)
    {
      int[,] array = new int[20, 20];
      int val = 0;
      string grid = "08022297381500400075040507785212507791084949994017811857608717409843694804566200814931735579142993714067538830034913366552709523046011426924685601325671370236912231167151676389419236542240402866331380244732609903450244753353783684203517125032988128642367102638406759547066183864706726206802621220956394396308409166499421245558056673992697177878968314883489637221362309750076442045351400613397343133957817532822753167159403800462161409535692163905429635314755588824001754243629855786560048357189070544443744602158515417581980816805944769287392138652177704895540045208839735991607975732162626793327986688366887576220720346336746551232639353690442167338253911249472180846293240627636206936417230238834629969826759857404361620733529783190017431497148868116235705540170547183515469169233486143520189196748";

      int l = 0, m = 0;
      for (int i = 0; i < 800; i += 2)
      {
        val = int.Parse(grid.Substring(i, 2));

        array[m, l] = val;
        l++;

        if (l == 20)
        {
          l = 0;
          if (m == 19)
            break;

          m++;
        }
      }
      Console.WriteLine(greatProd(array));
      Console.Read();
    }

    private static int greatProd(int[,] array)
    {
      int result = 0;
      int length = 20;
      int right = 0, down = 0, diaDownLeft = 0, diaDownRight = 0;

      for (int i = 0; i < length; i++)
      {
        for (int j = 0; j < length; j++)
        {
          //right
          if (j < 17)
          {
            right = array[i, j] * array[i, j + 1] * array[i, j + 2] * array[i, j + 3];
          }
          //down
          if (i < 17)
          {
            down = array[i, j] * array[i + 1, j] * array[i + 2, j] * array[i + 3, j];
          }
          //diagonal down left
          if (j > 2 && i < 17)
          {
            diaDownLeft = array[i, j] * array[i + 1, j - 1] * array[i + 2, j - 2] * array[i + 3, j - 3];
          }
          //diagonal down right
          if (j < 17 && i < 17)
          {
            diaDownRight = array[i, j] * array[i + 1, j + 1] * array[i + 2, j + 2] * array[i + 3, j + 3];
          }

          result = greatest(right, down, diaDownLeft, diaDownRight, result);
        }
      }

      return result;
    }

    private static int greatest(int a, int b, int c, int d, int result)
    {
      if (a > result)
      {
        result = a;
      }
      if (b > result)
      {
        result = b;
      }
      if (c > result)
      {
        result = c;
      }
      if (d > result)
      {
        result = d;
      }

      return result;
    }
  }
}