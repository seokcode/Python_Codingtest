# longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        i , l =0 ,0
        for j in range(len(s)):
            if s[ j -l: j+ 1] == s[j - l: j + 1][::-1]:
                i, l = j - l, l + 1

            elif j - l > 0 and s[j - l - 1: j + 1] == s[j - l - 1: j + 1][::-1]:
                i, l = j - l - 1, l + 2

        return s[i: i + l]



# 틀린 내 풀이(시간초과)
from itertools import permutations as permu


class Solution:
    def longestPalindrome(self, s: str) -> str:
        numbers = [i for i in range(len(s))]
        answer = []

        def isPalindrome(test) -> bool:
            if test == test[::-1]:
                return True
            else:
                return False

        everything = permu(numbers, 2)
        new_evry = sorted(everything, key=lambda x: abs(x[0] - x[1]), reverse=True)

        for first, second in new_evry:
            if s[first:second + 1] != '':
                if isPalindrome(s[first:second + 1]):
                    return s[first:second + 1]

        return s[0]