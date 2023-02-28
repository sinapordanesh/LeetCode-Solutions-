package com.sina.leetCode;

import java.lang.reflect.Array;
import java.util.*;

class Solution {
    public int pivotIndex(int[] nums) {


        for (int i = 0; i < nums.length ; i++){
            int leftSum = 0;
            int rightSum = 0;

            int k = 0;
            int j = nums.length - 1;

            if (i == 0)
                leftSum = 0;
            else
                while (k < i){
                    leftSum += nums[k];
                    k++;
                }
            if (i == nums.length - 1)
                rightSum = 0;
            else
                while (j > i){
                    rightSum += nums[j];
                    j--;
                }

            if (rightSum == leftSum) {
                return i;
            }
        }
        return -1;
    }
}