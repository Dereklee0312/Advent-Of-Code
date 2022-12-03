using System;

namespace AOC3
{
    class AssetTest
    {
        static void Main(string[] args)
        {
            Asset asset = new Asset();
            asset.ReadFile("test.txt");
            asset.CountPriority();
            Console.WriteLine(asset.SumPriority);
            Console.ReadKey();
        }
    }
}
