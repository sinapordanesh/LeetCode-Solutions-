package com.sina.leetCode;

import java.lang.reflect.Array;
import java.util.*;

class Solution {
    public boolean checkOnesSegment(String s) {

        if (s.length() == 1 && s.charAt(0) == '1'){
            return true;
        }

        int beforeZero = 0;

        for (int i = 1 ; i < s.length(); i++){

            if (s.charAt(i) == '0'){
                beforeZero = 1;
            }

            if (beforeZero == 1 && s.charAt(i) == '1'){
                return false;
            }
        }

        return true;
    }
}