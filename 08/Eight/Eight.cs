using System;
using System.Collections.Generic;
using System.IO;

namespace Eight
{
    class Program
    {
        static Dictionary<String, (String, String)> nodes = new Dictionary<String, (String, String)>();
        static char[] directions = 
        ("LRRLRRRLRRRLLRRLRRLRLRLRRLLRRLRRLRRRLLLRRRLRRRLRRRLLRRRLRRLLRRLRRLRLRRRLRRLRLRRLRRRLLRRLLRLRRRLLRRLRRLLLRLRRRLRLRLRLLRRRLRLL" +
        "RRRLRLRRRLRRRLLRRLRRRLLRRLRLLRLRRLLLRRLRRLLLRLLRLRRRLRLRLRRRLRRLLRRRLRLRLRRLRRRLRLRRLRRLRRRLRRRLRRRLRRRLRRLLRRLRLLRRLLRRRLRLL" +
        "RLRLRRLRRLRLRLRRRLRLRLRRLRLRRLRRRR").ToCharArray();
        static void Main(string[] args)
        {
            StreamReader reader = new StreamReader("Input.txt");
            while (!reader.EndOfStream) {
                String line = reader.ReadLine();
                nodes.Add(line.Substring(0,3), (line.Substring(7, 3), line.Substring(12, 3)));
            }
            reader.Close();
   
            int currentStep = 0;
            int totalSteps = 0;
            String currentNode = "AAA";
            
            while (!currentNode.Equals("ZZZ")) {
                (String, String) newNodes;
                if (nodes.TryGetValue(currentNode, out newNodes)) {
                    currentNode = (directions[currentStep] == 'L') ? newNodes.Item1 : newNodes.Item2;
                    currentStep = (currentStep < directions.Length - 1) ? currentStep + 1 : 0;
                    totalSteps++;
                }
            }

            Console.WriteLine(totalSteps);
        }
    }
}