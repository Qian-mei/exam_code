arr = [2,1,3]
n = len(arr)
dp = [[1]*n for _ in range(n)]
res = 0
for i in range(n):
    dp[i][i] = arr[i]
for L in range(2,n+1):
    for i in range(n):
        j = i+L-1
        if j>=n: break
        dp[i][j] = dp[i][j-1] & arr[j]
        if not dp[i][j]:
            res += i+1
print(res)
