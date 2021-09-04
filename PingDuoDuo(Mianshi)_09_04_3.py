# 题目描述：找到每个数据index之后的第一个大于他的数，若无，返回-1
# 例题 [3,3,1,5,7,3,8,9] --->[5,5,5,7,8,8,9,-1]
nums = [10,3,1,5,7,3,8,9]
n = len(nums)
# nex存储了第一个比index i大的数的index j
nex = [0]*n
for i in range(n-2,-1,-1):
    j = i+1
    while j and nums[i]>= nums[j]:
        j = nex[j]
    nex[i] = j
res = []
for i in range(n):
    res.append(nums[nex[i]] if nex[i] else -1)
print(res)


