public class Solution {


    public static void main(String[] args) {

     }

    public int[] productExceptSelf(int[] nums) {

        int [] result = new int[nums.length];

        for (int i = 0, tmp = 1; i < nums.length; i++){
            result[i] = tmp;
            tmp *= nums[i];
        }
        for (int j = nums.length-1, tmp = 1; j >= 0; j--){
            result[j] *= tmp;
            tmp *= nums[j];
        }

        return result;
    }
}




//A slowr solution for this problem. Not recomended!

/*
import java.util.HashMap;

public class Solution {

    public HashMap<Integer, Integer> backMap = new HashMap<Integer, Integer>();
    public HashMap<Integer, Integer> frontMap = new HashMap<Integer, Integer>();

    public static void main(String[] args) {

     }

    public int[] productExceptSelf(int[] nums) {
        int back = 1;
        int front = 1;
        int [] result = new int[nums.length];
        for (int i = 0; i < nums.length; i++){
            if (i != 0){
                back = back * nums[i-1];
            }
            backMap.put(i, back);
        }

        for (int j = nums.length - 1; j >= 0; j--){
            if (j != nums.length - 1){
                front = front * nums[j+1];
            }
            frontMap.put(j, front);
        }

        for (int k = 0; k < nums.length; k++){
            result[k] = frontMap.get(k) * backMap.get(k);
        }

        return result;
    }
}
