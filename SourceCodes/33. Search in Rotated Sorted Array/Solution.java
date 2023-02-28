package com.sinaCode;

import java.awt.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

class Solution {

    public int search(int[] nums, int target) {
        if (nums == null | nums.length == 0){
            return 0;
        }
        if (nums.length == 1){
            if (nums[0] == target){
                return 0;
            } else {
                return -1;
            }
        }

        int start = 0;
        int end = nums.length - 1;

        while (start < end){
            int mid = (start + end)/2;
            if (nums[mid] == target) return mid;

            if (nums[mid] >= nums[start]){
                if (target >= nums[start] && target < nums[mid]){
                    end = mid - 1;
                } else{
                    start = mid + 1;
                }
            } else {
                if (target > nums[mid] && target <= nums[end]){
                    start = mid + 1;
                } else{
                    end = mid - 1;
                }
            }
        }

        return nums[start] == target ? start : -1;
    }
}