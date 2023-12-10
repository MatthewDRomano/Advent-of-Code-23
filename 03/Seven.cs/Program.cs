using System;
using System.IO;
using System.Collections.Generic;
using System.Security.Cryptography.X509Certificates;
using System.Linq;
using System.Data;
using System.Numerics;

namespace Seven.cs
{
    class Program
    {
        static char[] symbols = {'@', '#', '$', '%', '&', '*', '-', '=', '+'};
        static List<String> grid = new List<String>();
        static void Main(string[] args)
        {
            StreamReader reader = new StreamReader("Input.txt");
            while (!reader.EndOfStream)
                grid.Add(reader.ReadLine());
                
            int total = 0;
            for (int i = 0; i < grid.Count; i++) {
                for (int q = 0; q < grid[i].Length; q++) {
                    if (isInt(grid[i][q])) {
                        int num = getNum((i,q));
                        if (isTouchingChar((i,q), (num + "").Length)) {
                            Console.WriteLine(num);
                            total+=num;
                            q += (num + " ").Length - 1;
                        }    
                    }       
                }
            }
            Console.WriteLine(total);
        }
        public static bool isInt(char c) { return c > 47 && c < 58; }

        public static int getNum((int row, int col) position) {
            int newCol = position.col;
            while (inBounds((position.row, newCol)) && isInt(grid[position.row][newCol])) 
                newCol++;
            //System.Console.WriteLine(grid[position.row].Substring(position.col, newCol - position.col));
            return Convert.ToInt32(grid[position.row].Substring(position.col, newCol-position.col));
        }
        public static bool isTouchingChar((int row, int col) position, int length) {
            int x = position.row-1;
            int y = position.col-1;
            
            if (inBounds((x,y+1)) && symbols.Contains(grid[x][y+1])) return true;
            else if (inBounds((x+length+1,y+1)) && symbols.Contains(grid[x+length+1][y+1])) return true;
            for (int i = 0; i < length+2; i++) {
                if (inBounds((x,y)) && symbols.Contains(grid[x][y])) return true;
                x++;
            }
            x = position.row-1;
            y = position.col+1;
            for (int i = 0; i < length+2; i++) {
                if (inBounds((x,y)) && symbols.Contains(grid[x][y])) return true;
                x++;
            }
            return false;
        }
        public static bool inBounds((int row, int col) position) {
            if (position.row < 0 || position.row >= grid.Count) return false;
            if (position.col < 0 || position.col >= grid[0].Length) return false;
            return true;
        }
        
    }
}