class Solution:
    def reverseWords(self, s: str) -> str:
        split_list = s.split(" ")
        split_list = [i[::-1] for i in split_list]
        return " ".join(split_list)