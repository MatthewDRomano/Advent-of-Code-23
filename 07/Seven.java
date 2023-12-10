import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Seven {
    
    static HashMap<Character, Integer> table = new HashMap<>() {
    //#region
        {
            put('2', 2);
            put('3', 3);
            put('4', 4);
            put('5', 5);
            put('6', 6);
            put('7', 7);
            put('8', 8);
            put('9', 9);
            put('T', 10);
            put('J', 11);
            put('Q', 12);
            put('K', 13);
            put('A', 14);
        }
    };
    //#endregion
        
    static HashMap<String, Integer> map = new HashMap<>();
    public static void main(String[] args) throws FileNotFoundException {
        Scanner reader = new Scanner(new File("Input.txt"));
  
        while (reader.hasNextLine()) {
            String line = reader.nextLine();
            map.put(line.substring(0, 5), Integer.parseInt(line.substring(6)));
        }
        reader.close();

        Set<String> keys = map.keySet();
        String[] hands = Arrays.copyOf(keys.toArray(), keys.size(), String[].class);
        Integer[] scores = new Integer[hands.length];

        for (int i = 0; i < hands.length; i++) {
            char[] ltrs = hands[i].toCharArray();
            String curHand = "";
            for (int j = 0; j < ltrs.length; j++) {
                curHand += numberOfOccurances(ltrs, ltrs[j]);
            }
            scores[i] = classify(curHand);
        }
        for (int i = 0; i < scores.length; i++) // combine both sorts by making 'scores' identify table value of hands[i] chars 
            for (int j = 1; j < scores.length - i; j++) {
                if (scores[j-1] > scores[j]) {
                    swap(hands, j-1, j);
                    swap(scores, j-1, j);    
                }
                else if (scores[j-1] == scores[j]) {
                    char[] hand1 = hands[j-1].toCharArray();
                    char[] hand2 = hands[j].toCharArray();
                    int index = 0;
                    while (hand1[index] == hand2[index])
                        index++;
                    if (table.get(hand1[index]) > table.get(hand2[index])) {  
                        swap(hands, j-1, j);
                        swap(scores, j-1, j);
                    }
                }
            }
        int total = 0;
        for (int i = 1; i <= hands.length; i++)
            total += i * map.get(hands[i-1]);
        System.out.println(total);
    }

    public static <Type> void swap(Type[] arr, int i1, int i2) {
        Type temp = arr[i1];
        arr[i1] = arr[i2];
        arr[i2] = temp;
    }
    public static int classify(String hand) {
        if (hand.indexOf("5") > -1) return 6;
        if (hand.indexOf("4") > -1) return 5;
        if (hand.indexOf("3") > -1) {
            if (hand.indexOf("2") > -1) 
                return 4;
            return 3;
        }     
        if (numberOfOccurances(hand.toCharArray(), '2') == 4) return 2;
        if (hand.indexOf("2") > -1) return 1;
        return 0;
    }

    public static int numberOfOccurances(char[] ltrs, char c) {
        int amt = 0;
        for (int i = 0; i < ltrs.length; i++) 
            if (ltrs[i] == c) amt++;
        return amt;
    }
}