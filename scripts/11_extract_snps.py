
import numpy as np, sys
aln, out_fa, out_cnt = sys.argv[1], sys.argv[2], sys.argv[3]
names=[]; seqs=[]; cur=[]
with open(aln) as fh:
    for line in fh:
        if line.startswith('>'):
            if cur: seqs.append(''.join(cur)); cur=[]
            names.append(line[1:].strip())
        else: cur.append(line.strip())
if cur: seqs.append(''.join(cur))
L=len(seqs[0]); n=len(seqs)
print('taxa',n,'length',L, flush=True)
A=np.frombuffer(''.join(seqs).encode(), dtype=np.uint8).reshape(n,L)
del seqs
ACGT=np.array([65,67,71,84],dtype=np.uint8)
Au=np.where(np.isin(A,np.array([97,99,103,116],dtype=np.uint8)), A-32, A)
counts=np.zeros((4,L),dtype=np.int32)
for i,b in enumerate(ACGT): counts[i]=(Au==b).sum(axis=0)
nonzero=(counts>0).sum(axis=0)
var = nonzero>1
const = nonzero==1
const_counts=[int(counts[i][const & (counts[i]>0)].shape[0]) for i in range(4)]
print('variable sites', int(var.sum()), 'constant', int(const.sum()), flush=True)
S=Au[:,var]
with open(out_fa,'w') as o:
    for nm,row in zip(names,S):
        o.write('>'+nm+'\n'+row.tobytes().decode()+'\n')
open(out_cnt,'w').write(','.join(map(str,const_counts))+'\n')
print('constant site counts A,C,G,T:', const_counts)
