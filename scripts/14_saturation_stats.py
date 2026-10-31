
import sys, os, itertools, random
import numpy as np
aln_fp, panel_fp, dist_fp, dtype, out_prefix = sys.argv[1:6]
def read_fa(fp):
    d={}; name=None; buf=[]
    for line in open(fp):
        if line[0]=='>':
            if name: d[name]=''.join(buf)
            name=line[1:].split()[0]; buf=[]
        else: buf.append(line.strip())
    if name: d[name]=''.join(buf)
    return d
panel=[l.strip() for l in open(panel_fp) if l.strip()]
A=read_fa(aln_fp)
panel=[p for p in panel if p in A]
M=np.array([np.frombuffer(A[p].upper().encode(),dtype=np.uint8) for p in panel])
if dtype=='nt':
    valid=set(b'ACGT'); amb=b'-NRYKMSWBDHVX?'
else:
    valid=set(b'ACDEFGHIKLMNPQRSTVWY'); amb=b'-X?BZJU*'
vmask=np.isin(M, np.array(sorted(valid),dtype=np.uint8))
n=len(panel)
# ---- p-distances, pairwise complete deletion
rows=[]
for i,j in itertools.combinations(range(n),2):
    m=vmask[i]&vmask[j]
    ncomp=int(m.sum())
    diff=int((M[i][m]!=M[j][m]).sum())
    rows.append((panel[i],panel[j],ncomp,diff,diff/ncomp if ncomp else float('nan')))
# ---- ML distances from IQ-TREE .mldist
ml={}
L=open(dist_fp).read().split('\n')
nt_=int(L[0].split()[0]); names=[]
mat=[]
for line in L[1:1+nt_]:
    f=line.split(); names.append(f[0]); mat.append([float(x) for x in f[1:]])
mat=np.array(mat); idxn={x:k for k,x in enumerate(names)}
# ---- site statistics
nstates=np.zeros(M.shape[1],dtype=np.int16)
for b in sorted(valid):
    nstates += (((M==b)&vmask).any(axis=0)).astype(np.int16)
ncols=M.shape[1]
colvalid=vmask.all(axis=0)
var=(nstates>1)
with open(out_prefix+'_pairs.tsv','w') as fo:
    fo.write("taxon1\ttaxon2\tn_compared\tn_diff\tp_distance\tml_distance\thidden_frac\n")
    for t1,t2,nc,nd,p in rows:
        d=mat[idxn[t1],idxn[t2]] if t1 in idxn and t2 in idxn else float('nan')
        hf=(d-p)/d if d and d==d and d>0 else float('nan')
        fo.write("%s\t%s\t%d\t%d\t%.6f\t%.6f\t%.6f\n"%(t1,t2,nc,nd,p,d,hf))
# ---- entropy-based saturation index (Xia-style), computed on fully-determined columns
sub=M[:,colvalid]
H=[]
for k in range(sub.shape[1]):
    col=sub[:,k]
    _,cnt=np.unique(col,return_counts=True)
    pr=cnt/cnt.sum()
    H.append(-(pr*np.log(pr)).sum())
H=np.array(H)
Hobs=float(H.mean())
# saturated reference: iid draws from the empirical composition of the same columns
vals,cnts=np.unique(sub,return_counts=True)
freq=cnts/cnts.sum()
rng=np.random.default_rng(0)
Hsat=[]
for rep in range(20):
    S=rng.choice(vals,size=(sub.shape[0],min(50000,sub.shape[1])),p=freq)
    h=[]
    for k in range(S.shape[1]):
        _,cc=np.unique(S[:,k],return_counts=True); pp=cc/cc.sum(); h.append(-(pp*np.log(pp)).sum())
    Hsat.append(np.mean(h))
Hsat=np.array(Hsat)
with open(out_prefix+'_summary.tsv','w') as fo:
    def w(k,v): fo.write("%s\t%s\n"%(k,v))
    w('dataset', out_prefix); w('n_taxa', n); w('n_sites', ncols)
    w('n_sites_no_missing', int(colvalid.sum()))
    w('n_variable_sites_panel', int(var.sum()))
    w('frac_variable', float(var.sum())/ncols)
    w('n_sites_ge3_states', int((nstates>=3).sum()))
    w('frac_sites_ge3_states', float((nstates>=3).sum())/ncols)
    w('n_sites_4_states', int((nstates>=4).sum()))
    w('mean_entropy_Hobs', Hobs)
    w('mean_entropy_saturated_ref', float(Hsat.mean()))
    w('entropy_sd_saturated_ref', float(Hsat.std()))
    w('Iss_entropy_ratio', Hobs/float(Hsat.mean()))
    w('max_entropy_ln_nstates', float(np.log(len(valid))))
print('done', out_prefix)
