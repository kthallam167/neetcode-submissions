class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        curr = 0
        checking = 0
        count = 0
        while checking < len(nums):
            if nums[checking]==val:
                checking+=1
                count+=1
            else:
                nums[curr] = nums[checking]
                curr+=1
                checking+=1
        return len(nums)-count
