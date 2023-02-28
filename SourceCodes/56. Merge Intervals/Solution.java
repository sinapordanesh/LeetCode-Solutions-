package com.sina.leetCode;

import java.lang.reflect.Array;
import java.util.*;

class Solution {

/*  my own code (has problem, in addition complicated)
    public int[][] merge(int[][] intervals) {

        Arrays.sort(intervals, Comparator.comparingInt(o -> o[0]));

        if ((intervals.length == 0) || (intervals.length == 1)){
            return intervals;
        }

        List<int[]> result = new ArrayList<>();

        int i = 0;
        boolean interval = false;

        while (i < intervals.length - 1){

            while (i < intervals.length - 1 && intervals[i][1] < intervals[i+1][0]){
                result.add(intervals[i]);
                i++;
                interval = false;
            }

            int[] newInterval = new int[2];
            newInterval[0] = intervals[i][0];
            newInterval[1] = intervals[i][1];
            while (i < intervals.length - 1 && intervals[i+1][0] <= intervals[i][1]){
                int start = Math.min(intervals[i][0], intervals[i+1][0]);
                if (start < newInterval[0])
                    newInterval[0] = start;

                int end = Math.max(intervals[i][1], intervals[i+1][1]);
                if (end > newInterval[1])
                    newInterval[1] = end;
                i++;
                interval = true;
            }

            if (interval){
                result.add(newInterval);
                i++;
            }

            if (i == intervals.length - 1){
                if (interval)
                    break;
                else {
                    result.add(intervals[i]);
                }
            }
        }

        return result.toArray(new int[result.size()][2]);
    }

 */

    public int[][] merge(int[][] intervals) {

        Arrays.sort(intervals, Comparator.comparingInt(o -> o[0]));

        if ((intervals.length == 0) || (intervals.length == 1)){
            return intervals;
        }

        List<int[]> result = new ArrayList<>();

        int i = 1;
        int start = intervals[0][0];
        int end = intervals[0][1];

        while (i < intervals.length){

            int s = intervals[i][0];
            int e = intervals[i][1];

            if (intervals[i][0] <= end){
                end = Math.max(end, e);
            } else {
                result.add(new int[]{start, end});
                start = s;
                end = e;
            }

            i++;
        }
        
        result.add(new int[]{start, end});

        return result.toArray(new int[result.size()][2]);
    }
}