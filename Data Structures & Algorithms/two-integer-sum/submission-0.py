class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        for i in range(len(nums)):
            num = nums[i]
            for j in range(i+1, len(nums)):
                if (num + nums[j]) == target:
                    return [i,j]