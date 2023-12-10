using System;
using System.IO;
using System.Collections.Generic;

namespace _2_Part2
{
    class Program
    {
        static void Main(string[] args)
        {
            List<String> games = new List<String>();
            StreamReader reader = new StreamReader("I:\\Advent of Code 23\\02\\2\\bin\\Debug\\net5.0\\Input.txt");
            while(!reader.EndOfStream) {
                String game = reader.ReadLine();
                game = game.Substring(game.IndexOf(":")+1);     
                games.Add(game);          
            }
            
            int answer = 0;

            for (int i = 0; i < games.Count; i++) {              
                
                int minRed = maxOfColorDrawn(games[i], "red");
                int minGreen = maxOfColorDrawn(games[i], "green");
                int minBlue = maxOfColorDrawn(games[i], "blue");

                answer += minGreen * minRed * minBlue; //answer = sumation of all 'Powers' (min of every color multipled) per game
            }

            Console.WriteLine(answer);
        }
        public static int maxOfColorDrawn(String s, String color) {
            int maxOfColor = 0;
            while (s.IndexOf(color) != -1) {
                int colorDrawn = Convert.ToInt32(s.Substring(s.IndexOf(color) - 3, 2).Trim());
                maxOfColor = Math.Max(colorDrawn, maxOfColor);
                s = s.Substring(s.IndexOf(color)+color.Length);
            }
            return maxOfColor;
        }
    }
}
