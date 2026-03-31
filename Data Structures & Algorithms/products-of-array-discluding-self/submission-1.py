class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0 for _ in range(len(nums)+1)]
        postfix = [0 for _ in range(len(nums)+1)]
        prefix[0] = 1
        postfix[len(postfix)-1] = 1

        index = 1;
        for n in nums:
            prefix[index] = n * prefix[index-1]
            index+=1
        index = len(postfix)-2;
        for n in reversed(nums):
            postfix[index] = n * postfix[index+1]
            index -=1
        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * postfix[i+1])
        return res