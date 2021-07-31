# Runtime: 114 ms, faster than 26.35% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14.4 MB, less than 54.50% of Python3 online submissions for Longest Substring Without Repeating Characters.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subArr, compareArr = [], []
        for c in s:
            if not subArr or (c not in subArr):
                subArr.append(c)
            else:
                if not compareArr:
                    compareArr = subArr
                else:
                    if len(subArr) > len(compareArr):
                        compareArr = subArr
                
                if subArr[-1] != c:
                    subString = "".join(subArr)
                    idx = subString.find(c)
                    subArr = list(subString[idx+1:])
                else:
                    subArr = []
                subArr.append(c)
        
        return max(len(subArr), len(compareArr))