// AoC template for Java

import java.util.*;
import java.io.*;

public class AoC{
    public static ArrayList<String> getInput(Scanner sc){
        ArrayList<String> input = new ArrayList<String>();
        while(sc.hasNextLine()){
            input.add(sc.nextLine());
        }
        sc.close();
        return input;
    }
    public static void main(String[] args) throws IOException{
        ArrayList<String> input = AoC.getInput(new Scanner("input.txt"));

        // Part 1
        System.out.println("Part 1:");

        // Part 2
        System.out.println("Part 2:");
    }
}
