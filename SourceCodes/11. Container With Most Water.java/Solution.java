package com.sina.leetCode;

import java.lang.reflect.Array;
import java.util.*;

class Solution {
    public int maxArea(int[] height) {
        int maxAmount = 0;

        if (height.length == 0){
            return 0;
        } else if (height.length == 1){
            return 0;
        }

        int i = 0;
        int j = height.length - 1;

        while (i < j){
            if (height[i] <= height[j]){
                int currentAmount = (j - i) * height[i];
                if (currentAmount > maxAmount)
                    maxAmount = currentAmount;
                i++;
            } else {
                int currentAmount = (j - i) * height[j];
                if (currentAmount > maxAmount)
                    maxAmount = currentAmount;
                j--;
            }
        }

        return maxAmount;
    }
}