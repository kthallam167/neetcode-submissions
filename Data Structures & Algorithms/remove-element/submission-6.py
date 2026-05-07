class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        temp = 0
        for x in range(0,len(nums)):
            if(nums[x]!=val):
                temp = nums[k]
                nums[k] = nums[x]
                nums[x] = temp
                k+=1
        return k

