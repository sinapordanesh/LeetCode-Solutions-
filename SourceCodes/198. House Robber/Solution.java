package com.sina.leetCode;

import java.beans.PropertyEditorSupport;
import java.lang.reflect.Array;
import java.util.*;

class Solution {

    public int rob(int[] nums) {
        int notRob = 0;
        int rob = 0;

        for (int i = 0; i < nums.length; i++) {
            int current = nums[i] + notRob;
            notRob = Math.max(notRob, rob);
            rob = current;
        }

        return Math.max(rob, notRob);
    }
}