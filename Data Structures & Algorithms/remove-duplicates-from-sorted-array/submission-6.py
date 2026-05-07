class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        removed = set(nums)
        nums.clear()
        for x in removed:
            nums.append(x)
        nums.sort()
        return len(nums)
        
