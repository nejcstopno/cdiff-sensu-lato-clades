
import sys, os
out=sys.argv[1]
gids=[l.strip() for l in open(os.path.join(out,'genome_order.txt'))]
fams=[l.strip() for l in open(os.path.join(out,'families.txt'))]
def read_fa(fp):
    d={}; name=None; buf=[]
    for line in open(fp):
        if line[0]=='>':
            if name: d[name]=''.join(buf)
            name=line[1:].split()[0]; buf=[]
        else: buf.append(line.strip())
    if name: d[name]=''.join(buf)
    return d
aa={g:[] for g in gids}; nt={g:[] for g in gids}; p12={g:[] for g in gids}
parts=[]; used=0; skipped=0
for fam in fams:
    af=os.path.join(out,'aln_aa',fam+'.aln'); nf=os.path.join(out,'fam_nt',fam+'.fna')
    if not os.path.exists(af) or os.path.getsize(af)==0: skipped+=1; continue
    A=read_fa(af); N=read_fa(nf)
    L=len(next(iter(A.values())))
    if any(len(v)!=L for v in A.values()): skipped+=1; continue
    for g in gids:
        if g in A:
            s=A[g]; seq=N[g]; k=0; row=[]
            for ch in s:
                if ch=='-': row.append('---')
                else:
                    cod=seq[3*k:3*k+3]
                    if len(cod)<3: cod=cod+'N'*(3-len(cod))
                    row.append(cod); k+=1
            r=''.join(row); aa[g].append(s)
        else:
            r='-'*(3*L); aa[g].append('-'*L)
        nt[g].append(r)
        p12[g].append(''.join(r[i]+r[i+1] for i in range(0,len(r),3)))
    parts.append((fam,L)); used+=1
def w(d,fp):
    with open(fp,'w') as fo:
        for g in gids: fo.write(">%s\n%s\n"%(g,''.join(d[g])))
w(aa,os.path.join(out,'concat_aa.fasta')); w(nt,os.path.join(out,'concat_nt.fasta')); w(p12,os.path.join(out,'concat_p12.fasta'))
with open(os.path.join(out,'partitions.txt'),'w') as fo:
    for f,l in parts: fo.write("%s\t%d\n"%(f,l))
print("families_used",used,"skipped",skipped,"aa_cols",sum(l for _,l in parts),"nt_cols",3*sum(l for _,l in parts))
