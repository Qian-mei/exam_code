from collections import defaultdict
'''
n 为驿站总数，s最初起始出发点，m为单行道数，k为双向道数
u,v为两个驿站,w为u-->v的耗时
a为当前耗时为奇数时的附加耗时,b为偶当前耗时为数时的附加耗时
q为包裹数,tar为每个包裹的目的地
'''

def dijkstra(start,end):
    if start == end:return 0
    nextnode = {start:True}
# nextnode表示链路外更新的节点
    nextnode.update({i:False for i in road[start]}) 
# costtime 表示链路上的点到node的最短耗时
    costtime = {i:time[(start,i)] for i in road[start]}
    mintime,tempnode = float('inf'),start
    
#    test_count = 0    
    while True:
        # print(start,nextnode,costtime)
        for node in nextnode:
            if not nextnode[node] and costtime[node]:
                mintime = min(mintime,costtime[node])
                tempnode = node
        if tempnode == end:
            break
# 添加节点进链路
        nextnode[tempnode] = True
# 更新链路外原有节点的距离
        for node in nextnode:
            if not nextnode[node] and costtime[node] and time[(tempnode,node)]:
                costtime[node] = min(costtime[node],costtime[tempnode]+time[(tempnode,node)])
# 更新链路外新增节点
        costtime.update({i:costtime[tempnode]+time[(tempnode,i)] for i in road[tempnode] if i not in nextnode})
        nextnode.update({i:False for i in road[tempnode] if i not in nextnode})
        
#        test_count+=1
#        if test_count==5000:break
              
    return costtime[end]

# input
n,s,m,k = list(map(int,input().split()))
road = defaultdict(list)
time = defaultdict(int)
for i in range(m):
    u,v,w = list(map(int,input().split()))
    if v != u and v not in road[u]:
        road[u].append(v)
        time[(u,v)] = w
for i in range(k):
    u,v,w = list(map(int,input().split()))
    if v != u and v not in road[u]:
        road[u].append(v)
        time[(u,v)],time[(v,u)] = w,w
a,b,q = list(map(int,input().split()))
tar = list(map(int,input().split()))

# main()
restime = 0
start = s
dp = defaultdict(int)
for i in range(q):
    end = tar[i]
# 存储两个村庄之间的最短路径耗时
    if not dp[(start,end)]:
        dp[(start,end)] = dijkstra(start,end)
    restime += dp[(start,end)]
    restime += a if restime%2 else b
    start = end
print(restime)
    
'''
自测数据
input：
6 6 6 0

1 2 1

2 3 2

3 4 3

4 5 4

5 1 5

6 1 6

0 0 6

1 5 4 3 2 1

output: 66
'''
