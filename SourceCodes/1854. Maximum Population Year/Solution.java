package com.sina.leetCode;

import java.lang.reflect.Array;
import java.util.*;

class Solution {

    public int maximumPopulation(int[][] logs) {

        int[] pair = new int[] {0, 1950};
        for (int i = 1950 ; i <= 2050; i++){
            int count = 0;
            for (int k = 0 ; k < logs.length; k++){
                if (i >= logs[k][0] && i < logs[k][1]){
                    count++;
                }
            }

            if (count > pair[0]){
                pair[0] = count;
                pair[1] = i;
            }
        }

        return pair[1];
    }
}