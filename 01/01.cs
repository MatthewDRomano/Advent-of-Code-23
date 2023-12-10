using System;
using System.IO;
using System.Linq.Expressions;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            StreamReader reader = new StreamReader("Input.txt");
            String[] lines = reader.ReadToEnd().Split("\n");   

            int total = 0;
            String holder;

            foreach(String line in lines) {
                holder = "";
                for (int i = 0; i < line.Length; i++) {
                    if (isInteger(line[i])) {
                        holder += line[i];
                        break;
                    }
                    String temp = ifSpelledNum(line, i); //part Two
                    if (temp != "") { //part Two
                        holder += temp; //part Two
                        break; //part Two
                    } //part Two
                }
                for (int i = line.Length-1; i >= 0; i--) {
                    if (isInteger(line[i])) {
                        holder += line[i];
                        break;
                    }
                    String temp = ifSpelledNum(line, i); //part Two
                    if (temp != "") { //part Two 
                        holder += temp; //part Two
                        break; //part Two
                    } //part Two
                }
                total += Convert.ToInt32(holder);
            }
            
            Console.WriteLine(total);
        }

        public static bool isInteger(char c) {
            return (c > 47 && c < 58) ? true : false;
        }

        public static String ifSpelledNum(String str, int index) {
            String[] nums = { "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", };
            
            foreach(String num in nums) if (num.Length + index <= str.Length) {
                if (str.Substring(index, num.Length).Equals(num)) {
                    switch (num) {
                        case "one": return "1";
                        case "two": return "2";
                        case "three": return "3";
                        case "four": return "4";
                        case "five": return "5";
                        case "six": return "6";
                        case "seven": return "7";
                        case "eight": return "8";
                        case "nine": return "9";
                    }
                }
            }
            return "";
        }
    }
}