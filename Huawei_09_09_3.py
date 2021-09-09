from collections import defaultdict

'''
题目：计算某个模块target的运行耗时,它的耗时 = 本身的耗时 + max(所有一级前置模块的耗时),若改模块中含有环，返回-1
测试示例：
6
m5 # 结果为-1 // m3 #结果为40
m1 5
m2 10 m4
m3 10 m1 m2
m4 20
m5 30 m4 m6
m6 40 m5
'''
def dfs(model,path):
    if noncircle[model]: return True
    maxtime = 0
    existcircle = False
# path利用回溯法存储走过的路径，避免陷入环的死循环。
    path.append(model)
#    print('+path:',path)
    for mod in relationship[model]:
        if mod in path or not dfs(mod,path):
            existcircle = True
            break            
        else:
            maxtime = max(maxtime,time[mod])
    path.pop()
#    print('-path:',path)
    if existcircle:return False
# 更新该节点的耗时，同时记录节点的搜寻状态
    time[model] += maxtime
    noncircle[model] = True
    return True

if __name__ == "__main__":
# noncircle存储已经搜寻过的无环的节点，下一次调用该节点直接使用time{node:cost_time}
# relationship存储某节点的前置节点，若无，为空list
    noncircle = defaultdict(bool)
    relationship = defaultdict(list)
    time = {}
    n = int(input())
    target = input()
    for _ in range(n):
        value = input().split()
        relationship[value[0]] += value[2:]
        time[value[0]] = int(value[1])
        if not relationship[value[0]]:noncircle[value[0]] = True
    path = []
    print(time[target] if dfs(target,path) else -1)