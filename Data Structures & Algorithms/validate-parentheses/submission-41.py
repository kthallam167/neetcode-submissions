class Solution:
    def isValid(self, s: str) -> bool:
        left = ["(", "{", "["]
        right = [")","}","]"]
        arrLeft = []
        arrRight = []
        for i in s:
            if i in left:
                arrLeft.append(i)
            if i in right:
                if arrLeft == []:
                    return False
                if i == ")":
                    if arrLeft[len(arrLeft)-1]!="(":
                        return False
                    else:
                        arrLeft.pop()
                if i == "]":
                    if arrLeft[len(arrLeft)-1]!="[":
                        return False
                    else:
                        arrLeft.pop()
                if i == "}":
                    if arrLeft[len(arrLeft)-1]!="{":
                        return False
                    else:
                        arrLeft.pop()
        return True if len(arrLeft)==0 else False