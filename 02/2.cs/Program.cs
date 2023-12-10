using System;
using System.IO;

namespace _2.cs
{
    class Program
    {
        const int MAXRED = 12, MAXGREEN = 13, MAXBLUE = 14;
        static int curID = 0;
        static void Main(string[] args)
        {
            StreamReader reader = new StreamReader("Input.txt");
            String[] lines = reader.ReadToEnd().Split("\n");

            int IDsum = 0;

            foreach (String line in lines) {
                String holder = line;
                holder = holder.Substring(holder.IndexOf(":")+2);
                curID++;  
                int i = holder.IndexOf(";");
                
                while (i > -1) {
                    //Console.WriteLine(holder);
                    int result = PartitionedCheck(holder.Substring(0, i), ref IDsum);
                    if (result == 0) goto end_of_loop;
                    holder = holder.Substring(i+1, holder.Length - (i+1));
                    i = holder.IndexOf(";");
                }         
                if (PartitionedCheck(holder.Substring(0, holder.Length), ref IDsum) == 0) continue;
                IDsum += curID;
                Console.WriteLine(curID);
                end_of_loop:;
            }
            
            Console.WriteLine(IDsum);
        }
        public static int PartitionedCheck(String str, ref int IDSum) {
            int reds = 0, blues = 0, greens = 0;
            //Console.WriteLine(str);
            for (int i = 0; i < str.Length; i++) {
                int num = 0;
                int space = 2;
                if (str[i] > 47 && str[i] < 58) {
                    num = str[i] - '0';
                    if (str[i+1] > 47 && str[i+1] < 58) {
                        num = (str[i] - '0')*10 + (str[i+1] - '0');
                        space = 3;
                    }
                    //Console.Write(num + " ");
                    switch(str[i+space]) {
                        case 'r':
                            reds += num;
                            break;
                        case 'g':
                            greens += num;
                            break;
                        case 'b':
                            blues += num;
                            break;
                    }  
                    if (reds > MAXRED || greens > MAXGREEN || blues > MAXBLUE)
                        return 0;              
                    
                }
            }
            return 1;
        }
    }
}