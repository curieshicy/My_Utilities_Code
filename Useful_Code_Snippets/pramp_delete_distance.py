def delete_distance(str1, str2):
    # dp solution
    # let dp[i][j] = min number of delete operations needed to
    # make a1.....ai and b1.....bj equal
    # dp[i][j] = dp[i-1][j-1] if ai == bj
    #          = min(dp[i-1][j], dp[i][j-1]) + 1
    
    m = len(str1) # rows
    n = len(str2) # cols
    dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for i in range(n + 1):
        dp[0][i] = i
        
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j])
    return dp[m][n]
    
    
str1 = 'dog'
str2 = 'frog'
str3 = 'some'
str4 = 'some'
str5 = 'some'
str6 = 'thing'
str7 = ''
str8 = ''
print (delete_distance(str1, str2))
print (delete_distance(str3, str4))
print (delete_distance(str5, str6))
print (delete_distance(str7, str8))
