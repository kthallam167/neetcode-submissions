class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0
        greatest = 0
        for i in range(len(nums)):
            if nums[i]==1:
                current+=1
            else:
                if current>greatest:
                    greatest = current
                current = 0
        if current>greatest:
            return current
        else:
            return greatest
        