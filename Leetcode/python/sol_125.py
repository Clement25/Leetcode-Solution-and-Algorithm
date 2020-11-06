class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        
        l = 0
        r = len(s) - 1
        
        s = s.lower()
        
        while l < r:
            if not s[l].isalnum():
                l += 1
            if not s[r].isalnum():
                r -= 1
            if s[l].isalnum() and s[r].isalnum():
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
        return True