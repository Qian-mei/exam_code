import sys
# n1,n2分别为两次从上一个节点收到的包的数量，i为节点的index，flag表示当前节点是否损坏
# r1,r2分别为两次从该节点发送出去的包的数量
def bfs(n1,n2,i,flag):
    global res
    if i==k:
        res = min(res,n1+n2)
        return
    elif not flag:
        bfs(n1,n2,i+1,True) 
# 此时r1,r2为节点发送和缓存的数量
    if n1 < S[i]:
        r1,r2 = n1,0
    elif n1 < S[i]+C[i]:
        r1,r2 = S[i],n1-S[i]
    else:
        r1,r2 = S[i],C[i]
# 暂存r1的值，此时r1/temp即为第一次转发出去的数目
    temp = r1
    n1 = n2+r2
    r1 = n1 if n1 < S[i] else S[i]
# 更新r1,r2的值
    r1,r2 = temp,r1
    bfs(r1,r2,i+1,True)
    bfs(r1,r2,i+1,False)   

# 输入，nums为初始包数，S为节点send的数量，C为节点cache的数量
k = int(input())
value = input().split()
S,C = [0]*k,[0]*k
for i in range(k):
    S[i],C[i] = list(map(int, value[i].split(',')))
nums = int(input())
res = nums
bfs(nums,0,0,True)
bfs(nums,0,0,False)
print('res --->',res)



