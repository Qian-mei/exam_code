import sys
from collections import defaultdict
def find(p,q):
    if not f[p]:return False
    elif p == q:return True
    return find(f[p],q)

n = int(input())
f = {}
ins = defaultdict(list)
for _ in range(n):
    chi,sta,fat = input().split()
    if sta == 'subClassof': f[chi] = fat
    else: ins[fat].append(chi)
tar = input()
# 防止f[tar]没有父节点，并截断f[tar]
f[tar] = tar
res = []
for i in f:
    if find(i,tar):
        res += ins[i]
print('node: children--->father ',f)
print('instance: fruit--->apple ',ins)
print('res:-------------')
print(' '.join(sorted(res)))


