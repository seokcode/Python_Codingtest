class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        shortestWord = min(strs,key=len)
        for i, ch in enumerate(shortestWord):
            for other in strs:
                if other[i] != ch:
                    return shortestWord[:i]
        return shortestWord 