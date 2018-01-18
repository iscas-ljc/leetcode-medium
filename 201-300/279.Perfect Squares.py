class Solution(object):
    _dp = [0]
    def numSquares(self, n):
    	#动态规划+数学问题
        dp = self._dp
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]