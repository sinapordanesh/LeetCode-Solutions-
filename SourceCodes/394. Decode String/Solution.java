package com.sina.leetCode;

import java.lang.reflect.Array;
import java.util.*;

class Solution {

    public int i = 0;
    public String decodeString(String s) {

        if (s.length() == 0){
            return "";
        } else if (s.length() == 1){
            if (Character.isDigit(s.charAt(i)))
                return "";
            else
                return s;
        }

        String result = "";

        for ( ; i < s.length();){
            if (Character.isDigit(s.charAt(i))){
                String repeatedPart = repeater(s);
                result += repeatedPart;
            } else {
                result += s.charAt(i);
                i++;
            }
        }
        return result;
    }

    public String repeater (String s){

        String result = "";

        String iteration = "";
        while (Character.isDigit(s.charAt(i))){
            iteration += s.charAt(i);
            i++; // pass the number
        }

        int nIteration = 0;
        if (s.charAt(i) == '['){
            nIteration = Integer.parseInt(iteration);
        }

        i++; // passing '['
        String repeating = "";

        while (s.charAt(i) != ']'){
            if (Character.isDigit(s.charAt(i))){
                String insideIteration = repeater(s);
                repeating += insideIteration;
            } else {
                repeating += s.charAt(i);
                i++; // pass the character
            }
        }

        i++; //passing ']';

        for (int j = 0; j < nIteration; j++){
            result += repeating;
        }

        return result;
    }
}