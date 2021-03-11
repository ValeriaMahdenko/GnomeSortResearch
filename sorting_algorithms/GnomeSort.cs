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
