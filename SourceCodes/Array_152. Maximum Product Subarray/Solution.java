package com.sinaCode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

class Solution {

    public int maxProduct(int[] nums) {
        int answer = nums[0];
        int n = nums.length;
        int left = 1, right = 1;

        for (int i = 0; i < n; i++){

            left = left==0 ? 1 : left;
            right = right==0 ? 1 : right;

            left *= nums[i];
            right *= nums[n-1-i];

            answer = Math.max(answer, Math.max(left, right));
        }
        return answer;
    }
}