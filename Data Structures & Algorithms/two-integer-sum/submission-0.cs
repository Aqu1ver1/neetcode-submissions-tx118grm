public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int,int> prevNums = new Dictionary<int,int>(); //value,index
        for(int i = 0; i < nums.Length;i++){
            int diff = target - nums[i];
            if(prevNums.ContainsKey(diff)){
                return new int[] { prevNums[diff], i };
            }
            prevNums.Add(nums[i], i);

        }
        return new int[0];
    }
}
