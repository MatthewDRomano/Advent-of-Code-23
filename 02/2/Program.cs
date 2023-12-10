using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Reflection.Metadata;
using System.Runtime.InteropServices;

namespace _2
{
    class Program
    {
        const int MAXREDS = 12, MAXGREENS = 13, MAXBLUES = 14;
        public static void Main(string[] args) 
        {
            List<List<String>> games = new List<List<String>>();
            StreamReader reader = new StreamReader("Input.txt");
            while(!reader.EndOfStream) {
                String game = reader.ReadLine();
                game = game.Substring(game.IndexOf(":")+1);

                String[] draws = game.Split(";");

                games.Add(draws.ToList());                  
            }
                
            int IDsum = 0;
            for (int i = 0; i < games.Count; i++) {
                bool possible = true;
                for (int j = 0; j < games[i].Count; j++) {
                    int reds = 0, greens = 0, blues = 0;
                    if (games[i][j].IndexOf("red") != -1)
                        reds += Convert.ToInt32(games[i][j].Substring(games[i][j].IndexOf("red") - 3, 2).Trim());
                    if (games[i][j].IndexOf("green") != -1)
                        greens += Convert.ToInt32(games[i][j].Substring(games[i][j].IndexOf("green") - 3, 2).Trim());
                    if (games[i][j].IndexOf("blue") != -1)
                        blues += Convert.ToInt32(games[i][j].Substring(games[i][j].IndexOf("blue") - 3, 2).Trim());

                    if (reds > MAXREDS || blues > MAXBLUES || greens > MAXGREENS)
                        possible = false;
                }
                if (possible) IDsum += i+1;
            }

            Console.WriteLine(IDsum);
        }   
    }
}