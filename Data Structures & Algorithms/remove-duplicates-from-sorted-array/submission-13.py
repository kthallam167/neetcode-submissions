import copy
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans = len(set(nums))
        curr = 1
        first = 0
        second = 1
        while second<len(nums):
            if nums[first] == nums[second]:
                second+=1
            else:
                nums[curr] = nums[second]
                first, second = second, second+1
                curr+=1
        return ans


