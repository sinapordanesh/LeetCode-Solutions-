
public class Solution {

    private HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

    public static void main(String[] args) {

     }

    public boolean containsDuplicate(int[] nums) {
        for (int i: nums){
            if (map.containsKey(i))
                return true;
            map.put(i, i);
        }
        return false;
    }
}