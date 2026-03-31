public class Solution {
    public bool hasDuplicate(int[] nums) {
        HashSet<int> newArr = new HashSet<int>(nums);
        return nums.Length != newArr.Count;
    }
}