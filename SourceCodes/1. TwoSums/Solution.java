
import java.util.ArrayList;
import java.util.HashMap;

public class Solution {

    public static void main(String[] args) {
	// write your code here
    }

    public int[] twoSum(int[] nums, int target) {

        HashMap<Integer, Integer> keyOfValue = new HashMap<Integer, Integer>();
        int[] result = new int[2];

        for (int i=0; i < nums.length; i++){
            keyOfValue.put(nums[i], i);
        }

        for (int i=0; i < nums.length; i++){
            int complement = target - nums[i];
            if(keyOfValue.containsKey(complement) && keyOfValue.get(complement) != i){
                return new int[] {i, keyOfValue.get(complement)};
            }
        }

        return null;
    }
}
