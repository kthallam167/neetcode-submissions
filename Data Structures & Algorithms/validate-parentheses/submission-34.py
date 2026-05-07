class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {"}":"{",")":"(","]":"["}
        for i in s:
            if stack and i in closeToOpen:
                if closeToOpen[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if stack:
            return False
        return True
            

            