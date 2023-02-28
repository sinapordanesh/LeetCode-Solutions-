package com.sina.leetCode;

import java.lang.reflect.Array;
import java.util.*;

class Solution {

    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> result = new LinkedList<>();
        int i = 0;
        // add all the intervals ending before newInterval starts
        while (i < intervals.length && intervals[i][1] < newInterval[0]){
            result.add(intervals[i]);
            i++;
        }

        // merge all overlapping intervals to one considering newInterval
        while (i < intervals.length && intervals[i][0] <= newInterval[1]) {
            // we could mutate newInterval here also
            newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
            newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
            i++;
        }

        // add the union of intervals we got
        result.add(newInterval);

        // add all the rest
        while (i < intervals.length){
            result.add(intervals[i]);
            i++;
        }

        return result.toArray(new int[result.size()][]);
    }

    /*     my solution (has some bugs)
    public int[][] insert(int[][] intervals, int[] newInterval) {

        if (intervals.length == 0){
            int[][] newIntervals = new int[1][2];
            newIntervals[0][0] = newInterval[0];
            newIntervals[0][1] = newInterval[1];

            return newIntervals;
        }

        int i = 0;
        int j = intervals.length - 1;

        if (i < j){
            while (newInterval[0] > intervals[i][1]){i++;}
            while (newInterval[1] < intervals[j][0]){j--;}
        }

        ArrayList<ArrayList<Integer>> newIntervalsList = new ArrayList<>();

        if ((j - i) == -1){

            for (int[] interval : intervals) {
                ArrayList<Integer> newItem = new ArrayList<>();
                newItem.add(interval[0]);
                newItem.add(interval[1]);
                newIntervalsList.add(newItem);
            }

            ArrayList<Integer> newItem = new ArrayList<>();
            newItem.add(newInterval[0]);
            newItem.add(newInterval[1]);

            if (newInterval[0] > intervals[intervals.length - 1][1]){
                newIntervalsList.add(newItem);
            }else if (newInterval[1] < intervals[0][0]){
                newIntervalsList.add(0, newItem);
            }

        } else {

            for (int k = 0; k < i; k++){
                ArrayList<Integer> newItem1 = new ArrayList<>();
                newItem1.add(intervals[k][0]);
                newItem1.add(intervals[k][1]);
                newIntervalsList.add(newItem1);

            }

            int start = Math.min(newInterval[0], intervals[i][0]);
            int end = Math.max(newInterval[1], intervals[j][1]);
            ArrayList<Integer> newItem2 = new ArrayList<>();
            newItem2.add(start);
            newItem2.add(end);
            newIntervalsList.add(newItem2);

            for (int l = intervals.length - 1; l > j; l--){
                ArrayList<Integer> newItem3 = new ArrayList<>();
                newItem3.add(intervals[l][0]);
                newItem3.add(intervals[l][1]);
                newIntervalsList.add(newItem3);
            }
        }

        return newIntervalsList.toArray(new int[newIntervalsList.size()][2]);
    }

 */

}