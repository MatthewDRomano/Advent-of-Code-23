using System;
using System.Collections.Generic;
using System.IO;

namespace Eight_Part2
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
            StreamReader reader = new StreamReader("I:\\Aoc\\08\\Eight\\bin\\Debug\\net5.0\\Input.txt");
            List<String> currentNodes = new List<String>();

            while (!reader.EndOfStream) {
                String line = reader.ReadLine();
                nodes.Add(line.Substring(0,3), (line.Substring(7, 3), line.Substring(12, 3)));
                if (line.Substring(0,3)[2] == 'A') 
                    currentNodes.Add(line.Substring(0,3));
            }
            reader.Close();

            int currentStep;
            int totalSteps;
            List<Int32> steps = new List<Int32>(); 
            for (int i = 0; i < currentNodes.Count; i++) {
                currentStep = 0;
                totalSteps = 0;
                while (currentNodes[i][2] != 'Z') {
                    (String, String) newNodes;
                    if (nodes.TryGetValue(currentNodes[i], out newNodes)) {
                        currentNodes[i] = (directions[currentStep] == 'L') ? newNodes.Item1 : newNodes.Item2;                    
                    }
                    currentStep = (currentStep < directions.Length - 1) ? currentStep + 1 : 0;
                    totalSteps++;
                }
                steps.Add(totalSteps);
            }
            
            
            Console.WriteLine(lcm_of_array_elements(steps.ToArray()));
        }
        public static bool allNodesFinished(List<String> nodes)  {
            foreach (String node in nodes)
                if (node[2] != 'Z')
                    return false;          
            return true;
        }
        public static long lcm_of_array_elements(int[] element_array) {
            long lcm_of_array_elements = 1;
            int divisor = 2;
         
            while (true) {     
                int counter = 0;
                bool divisible = false;
                for (int i = 0; i < element_array.Length; i++) {

                    if (element_array[i] == 0) 
                        return 0;
                    else if (element_array[i] < 0) 
                        element_array[i] = element_array[i] * (-1);

                    if (element_array[i] == 1)
                        counter++;
 
                    if (element_array[i] % divisor == 0) {
                        divisible = true;
                        element_array[i] = element_array[i] / divisor;
                    }
                }
 
                if (divisible) {
                    lcm_of_array_elements = lcm_of_array_elements * divisor;
                }
                else divisor++;
 
                if (counter == element_array.Length)
                    return lcm_of_array_elements;
            }
        }
    }
}