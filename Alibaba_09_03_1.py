# A选择区间反转最少次数变成B
# CMP记录了字符是否相同，相同的字符需要反转偶数次，否则需要反转奇数次,尽可能的反转最大的长度区间
A = '010'
B = '101'
n = len(A)
CMP = [A[i]==B[i] for i in range(n)]
i,j = 0,n-1
res = 0
#去除两边不需要反转0次的相同字符
while i<n and CMP[i]:
    i += 1
while i<=j and CMP[j]:
    j -= 1
while i<=j:
    while i<=j and not CMP[i]:
        i += 1
    while i<=j and not CMP[j]:
        j -= 1
#反转奇数次+1
    res += 1
    if i>j:break
    while i<=j and CMP[i]:
        i += 1
    while i<=j and CMP[j]:
        j -= 1
#反转偶数次+1
    res += 1
print(res)

