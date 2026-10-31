
import sys, numpy as np, os
edge_file, qc_file, qual_file, out_file = sys.argv[1:5]
ids = [l.strip() for l in open(qc_file) if l.strip()]
id2i = {g:i for i,g in enumerate(ids)}
n = len(ids)
print('genomes', n, flush=True)
A=[];B=[]
with open(edge_file) as f:
    f.readline()
    for line in f:
        p = line.split('\t',2)
        a = os.path.basename(p[0]); b = os.path.basename(p[1])
        if a.endswith('.fa'): a=a[:-3]
        if b.endswith('.fa'): b=b[:-3]
        ia=id2i.get(a); ib=id2i.get(b)
        if ia is not None and ib is not None:
            A.append(ia); B.append(ib)
A=np.array(A,dtype=np.int32); B=np.array(B,dtype=np.int32)
print('edges', len(A), flush=True)
from scipy.sparse import coo_matrix
G = coo_matrix((np.ones(len(A)*2,dtype=np.int8), (np.concatenate([A,B]), np.concatenate([B,A]))), shape=(n,n)).tocsr()
print('adjacency built', G.nnz, flush=True)
# order genomes by assembly quality (descending) from qual_file: genome_id<TAB>score
score = {}
for l in open(qual_file):
    g,s = l.rstrip('\n').split('\t'); score[g]=float(s)
order = sorted(range(n), key=lambda i: -score.get(ids[i], -1e9))
covered = np.zeros(n, dtype=bool)
rep_of = np.full(n, -1, dtype=np.int32)
reps=[]
for i in order:
    if covered[i]: continue
    reps.append(i); covered[i]=True; rep_of[i]=i
    nb = G.indices[G.indptr[i]:G.indptr[i+1]]
    new = nb[~covered[nb]]
    covered[new]=True; rep_of[new]=i
print('representatives', len(reps), flush=True)
with open(out_file,'w') as o:
    o.write('genome_id\trepresentative\tis_representative\n')
    for i in range(n):
        r = rep_of[i]
        o.write(f'{ids[i]}\t{ids[r] if r>=0 else ids[i]}\t{int(r==i or r<0)}\n')
