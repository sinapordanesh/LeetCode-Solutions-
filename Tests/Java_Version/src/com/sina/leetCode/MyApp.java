package com.sina.leetCode;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Scanner;

public class MyApp {
    HashMap<String, Integer> wordCount = new HashMap<>();

    public void app(String[] args) {


        try {
            File myObj = new File("/Users/sina/Library/CloudStorage/OneDrive-UniversityofCalgary/Backup/Documents/Programing/LeetCode-Solutions-/Tests/Java_Version/src/com/sina/leetCode/test.txt");
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                Scanner s2 = new Scanner(myReader.nextLine());
                while (s2.hasNext()) {
                    String s = s2.next();
                    if (wordCount.get(s.toLowerCase()) != null){
                        int current = wordCount.get(s.toLowerCase());
                        current++;
                        wordCount.put(s.toLowerCase(), current);
                    }else {
                        wordCount.put(s.toLowerCase(), 1);
                    }
                }
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }

        if (args.length == 0){
            Iterator it = wordCount.entrySet().iterator();
            while (it.hasNext()) {
                Map.Entry pair = (Map.Entry)it.next();
                System.out.println(pair.getKey() + " = " + pair.getValue());
                it.remove(); // avoids a ConcurrentModificationException
            }
        } else {
            arg(args[0].toLowerCase());
        }
    }

    private String noArg(){

    }

    private int arg(String arg){
        if (wordCount.get(args[0].toLowerCase()) != null){
            System.out.println(wordCount.get(args[0].toLowerCase()));
        } else {
            System.out.println(0);
        }
    }

}
