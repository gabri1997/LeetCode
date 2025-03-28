"""
You are given a string s, which contains stars *.
In one operation, you can:
    Choose a star in s.
    Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.
Note:
    The input will be generated such that the operation is always possible.
    It can be shown that the resulting string will always be unique.
"""

class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        while '*' in s:
            lung = len(s)
            for l in range(lung):
                if s[l] == '*':
                    s = s[:l-1] + s[l+1:]
                    break
        return s
     

if __name__ == '__main__':
    s = "leet**cod*e"
    sol = Solution()
    out = sol.removeStars(s)
    print(out)


 
