using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
namespace Gnome_sort
{
    class sharpy_data_generating
    {
        static void Swap(ref int item1, ref int item2)
        {
            var temp = item1;
            item1 = item2;
            item2 = temp;
        }

        static void GnomeSort(int[] unsortedArray)
        {
            var i = 1; 

            while (i < unsortedArray.Length)
            {
                if (i == 0)
                    i = 1;
                if (unsortedArray[i - 1] <= unsortedArray[i])
                    ++i; 
                else
                {
                    Swap(ref unsortedArray[i - 1], ref unsortedArray[i]);
                    --i;
                }
            }
        }
        static void Main(string[] args)
        {
            List<double> times = new List<double>();
            Stopwatch stopwatch = new Stopwatch();
            for (int size = 500; size <= 50000; size += 500)
            {
                int[] arr = new int[size];
                Random randNum = new Random();
                for (int i = 0; i < arr.Length; i++)
                    arr[i] = randNum.Next(0, 10000);
                stopwatch.Start();
                GnomeSort(arr);
                stopwatch.Stop();
                var rand_time = stopwatch.ElapsedMilliseconds;
                times.Add(rand_time);
            }
            using (var w = new StreamWriter(@"C:\Users\User\Desktop\С#\Gnome_sort\Gnome_sort\sharpy_data.csv"))
            {
                string line = "";
                foreach (var i in times)
                    line += string.Format("{0},", i);
                line += "\n";
                w.WriteLine(line);
                w.Flush();
            }
        }
    }
}
