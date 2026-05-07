import copy
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        initList = copy.copy(nums)
        ans = len(set(nums))
        curr = 1
        first = 0
        second = 1
        while second<len(nums):
            if initList[first] == initList[second]:
                second+=1
            else:
                nums[curr] = initList[second]
                first, second = second, second+1
                curr+=1
        return ans


