class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if not s:
            return 0
        if not s and not t:
            return 1
        
        dp = [[0]*(len(s)+1) for _ in range(len(t)+1)]
        dp[0][0] = int(s[0] == t[0])
        for i in range(len(t)+1):
            for j in range(len(s)+1):
                if i == 0:
                    dp[0][j] = 0
                elif j == 0:
                    dp[i][0] = 0
                else:
                    dp[i][j] = dp[i][j-1]+dp[i-1][j-1]*(t[i-1] == s[j-1])
        
        print(dp)
        return dp[-1][-1]