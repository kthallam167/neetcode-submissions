class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr)==1:
            arr[0]=-1
            return arr
        greatest = arr[len(arr)-1]
        arr[len(arr)-1] = -1
        for i in range(len(arr)-2,-1,-1):
            org = arr[i]
            arr[i] = greatest
            if org > greatest:
                greatest = org
        return arr
        