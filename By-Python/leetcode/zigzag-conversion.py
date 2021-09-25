class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or len(s) <= numRows:
            return s
        
        groups = [""]*numRows
        idx, move = 0, 0
        
        for item in s:
            groups[idx] += item
            if idx == 0:
                move = 1
            elif idx == (numRows-1):
                move = -1
            idx += move
        
        return "".join(groups)