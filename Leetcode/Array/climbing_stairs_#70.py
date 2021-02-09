# 1 阶： 1种
# 2 阶： 2种
# 3 阶： 3种
# 通项公式 ：f(n) = f(n-1) + f(n-2)
def climbStairs(self, n: int) -> int:
        dp = {}
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]