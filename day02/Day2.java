import java.util.*;
import java.io.*;

/**
 * forward X increases the horizontal position by X units.
 * down X increases the depth by X units.
 * up X decreases the depth by X units.
 */

public class Day2 {
    
    public static void main(String[] args) throws IOException {
        long horizontal = 0;
        long depth = 0;
        long aim = 0;

        Scanner sc = new Scanner(new File("input.txt"));
        ArrayList<String[]> input = new ArrayList<>();
        while (sc.hasNextLine()) {
            input.add(sc.nextLine().split(" "));
        }
        sc.close();

        // PART 1
        for (String[] line : input){
            if (line[0].equals("forward")) {
                long x = Long.parseLong(line[1]);
                horizontal += x;
            } else if (line[0].equals("down")) {
                long x = Long.parseLong(line[1]);
                depth += x;
            } else if (line[0].equals("up")) {
                long x = Long.parseLong(line[1]);
                depth -= x;
            }
        }

        System.out.println("Part 1: " + (horizontal * depth));

        // PART 2

        // reset
        horizontal = 0;
        depth = 0;
        aim = 0;
        for (String[] line : input){
            if (line[0].equals("forward")) {
                long x = Long.parseLong(line[1]);
                horizontal += x;
                depth += aim * x;
            } else if (line[0].equals("down")) {
                long x = Long.parseLong(line[1]);
                aim += x;
            } else if (line[0].equals("up")) {
                long x = Long.parseLong(line[1]);
                aim -= x;
            }
        }

        System.out.println("Part 2: " + (horizontal * depth));
    }
}