class Solution:

    def longestPalindrome(self, s):

        if len(s) < 2:
            return s

        # edge case
        n = len(s)
        dp = [[0 for i in range(n)] for i in range(n)]

        start, end, length = 0, 0, 0
        for k in range(n):
            for i, j in zip(range(n-k), range(k,n)):
                if i == j:
                    dp[i][j] = 1
                elif i + 1 == j and s[i] == s[j]:
                    dp[i][j] = 1
                elif j - i > 1 and s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]

                if dp[i][j] == 1 and j - i + 1 > length:
                    length = j - i + 1
                    start = i
                    end = j

        return s[start: end + 1]


test = Solution().longestPalindrome('ababa')
print (test)
