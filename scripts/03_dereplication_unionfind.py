
import sys, os
parent = {}
def find(x):
    r = x
    while parent[r] != r: r = parent[r]
    while parent[x] != r: parent[x], x = r, parent[x]
    return r
def union(a,b):
    ra, rb = find(a), find(b)
    if ra != rb: parent[rb] = ra
def add(x):
    if x not in parent: parent[x] = x
n=0
with open(sys.argv[1]) as f:
    header = f.readline()
    for line in f:
        p = line.split('\t', 2)
        a = os.path.basename(p[0]); b = os.path.basename(p[1])
        if a.endswith('.fa'): a = a[:-3]
        if b.endswith('.fa'): b = b[:-3]
        add(a); add(b); union(a,b)
        n += 1
        if n % 20000000 == 0: print(n, 'edges', flush=True)
print('total edges', n)
# include singletons from the full genome list
with open(sys.argv[2]) as f:
    for line in f:
        add(line.strip())
from collections import defaultdict
comp = defaultdict(list)
for g in parent: comp[find(g)].append(g)
print('components', len(comp))
with open(sys.argv[3],'w') as out:
    out.write('genome_id\tderep_cluster\tcluster_size\n')
    for i,(root, members) in enumerate(sorted(comp.items(), key=lambda kv:-len(kv[1])), start=1):
        for m in members: out.write(f'{m}\t{i}\t{len(members)}\n')
