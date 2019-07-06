class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        sign = 1
        if x == -2147483648: # x = 2^31
            return 0
        elif x < 0:
            x = -x
            sign = -1
            
        while(x!=0):
            res = res * 10 + x % 10
            x = x / 10
            if res >= pow(2,31):
                return 0
        return res*sign