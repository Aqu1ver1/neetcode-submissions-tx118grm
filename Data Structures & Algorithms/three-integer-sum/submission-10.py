class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortNums = sorted(nums)
        res = []
        for i in range(len(sortNums)-2):
            if(i > 0 and sortNums[i] == sortNums[i-1]):
                continue
            left = i+1
            right = len(sortNums)-1
            while left < right:
                threeSum = sortNums[i] + sortNums[left] + sortNums[right]
                if threeSum > 0:
                    right-=1
                elif threeSum < 0:
                    left+=1
                else: 
                    res.append([sortNums[i],sortNums[left],sortNums[right]])
                    left+= 1
                    while sortNums[left] == sortNums[left-1] and left < right:
                        left+=1

        return res
