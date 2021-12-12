class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        
        for item in s:
            if item == "(" or item == "{" or item == "[":
                brackets.append(item)
            else:
                if brackets:
                    if item == ")" and brackets[-1] == "(":
                        brackets.pop()
                    elif item == "}" and brackets[-1] == "{":
                        brackets.pop()
                    elif item == "]" and brackets[-1] == "[":
                        brackets.pop()
                    else:
                        return False
                else:
                    return False
        
        if not brackets:
            return True
        else:
            return False