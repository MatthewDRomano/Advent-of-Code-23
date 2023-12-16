using System;
using System.Collections.Generic;
using System.IO;

namespace _14
{
    class Program
    {
        static void Main(string[] args)
        {
            StreamReader reader = new StreamReader("Input.txt");
            String[] lines = reader.ReadToEnd().Split("\n");

            slideNorth(ref lines);

            int totalLoad = 0;
            for (int i = 0; i < lines.Length; i++)
                for (int q = 0; q < lines[i].Length; q++) {
                    if (lines[i][q] == 'O')
                        totalLoad += lines.Length - i;
                }
            System.Console.WriteLine(totalLoad);
        }
        public static void slideNorth(ref String[] lines) {
            for (int row = 1; row < lines.Length; row++)
                for (int col = 0; col < lines[row].Length; col++) {
                    int y = row;
                    while (y > 0 && lines[y][col] == 'O' && lines[y-1][col] == '.') {
                        lines[y] = lines[y].Substring(0, col) + "." + lines[y].Substring(col+1);
                        lines[y-1] = lines[y-1].Substring(0, col) + "O" + lines[y-1].Substring(col+1);
                        y--;
                    }
                }
        }
    }
}
