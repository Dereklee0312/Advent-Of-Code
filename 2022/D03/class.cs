using System.Collections.Generic;

namespace AOC3
{
    class Asset
    {
        public int SumPriority { get; private set; }
        public Dictionary<string, int> Items { get; private set; }
        public string Common { get; private set; }

        private List<string> _alphabet = new List<string>()
        {
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z"
        };

        public Asset()
        {
            Common = "";
            SumPriority = 0;
            Items = new Dictionary<string, int>();
            for (int i = 1; i <= 52; i++)
            {
                Items.Add(_alphabet[i - 1], i);
            }
        }

        // Part 1:
        // public void ReadFile(string fileName)
        // {
        //     string[] lines = File.ReadAllLines(fileName);
        //         var first = line.Substring(0, (int)(line.Length / 2));
        //         var last = line.Substring((int)(line.Length / 2), (int)(line.Length / 2));
        //         Common += this.CheckCommon(first, last);
        //     }
        //     Console.WriteLine(Common);
        // }

        // public string CheckCommon(string first, string second, string third)
        // {
        //     string common = "";
        //     for (int i = 0; i < first.Length; i++)
        //     {
        //         if (second.IndexOf(first[i]) != -1)
        //         {
        //             common = first[i].ToString();
        //         }
        //     }
        //     return common;
        // }

        // Part 2:
        public void ReadFile(string fileName)
        {
            List<string> contents = new List<string>();
            int count = 0;
            string[] lines = File.ReadAllLines(fileName);
            foreach (var line in lines)
            {
                if (count % 3 == 0)
                {
                    if (count != 0)
                    {
                        Common += this.CheckCommon(contents[0], contents[1], contents[2]);
                    }
                    contents.Clear();
                    contents.Add(line);
                }
                else
                {
                    contents.Add(line);
                }
                count++;
            }
            Common += this.CheckCommon(contents[0], contents[1], contents[2]);
        }

        // Part 2:
        public string CheckCommon(string first, string second, string third)
        {
            string common = "";
            for (int i = 0; i < first.Length; i++)
            {
                if (second.IndexOf(first[i]) != -1 && third.IndexOf(first[i]) != -1)
                {
                    common = first[i].ToString();
                }
            }
            return common;
        }

        public void CountPriority()
        {
            foreach (var item in Common)
            {
                SumPriority += Items[item.ToString()];
            }
        }
    } // end of class
} // end of namespace
