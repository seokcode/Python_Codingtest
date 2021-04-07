# Valid Palindrome

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.findall('[a-zA-Z0-9+]', s)
        s = ''.join(s).lower()
        if len(s) == 1:
            return True
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - 1 - i]:
                return False

        return True

