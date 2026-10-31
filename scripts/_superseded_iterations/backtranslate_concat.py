
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
aa_cat={g:[] for g in gids}; nt_cat={g:[] for g in gids}; p12_cat={g:[] for g in gids}
parts=[]; used=0; skipped=0
for fam in fams:
    af=os.path.join(out,'aln_aa',fam+'.aln')
    nf=os.path.join(out,'fam_nt',fam+'.fna')
    if not os.path.exists(af) or os.path.getsize(af)==0: skipped+=1; continue
    A=read_fa(af); N=read_fa(nf)
    if set(A)!=set(gids): skipped+=1; continue
    L=len(next(iter(A.values())))
    if any(len(v)!=L for v in A.values()): skipped+=1; continue
    ok=True; nt_rows={}
    for g in gids:
        s=A[g]; nt=N[g]; k=0; row=[]
        for ch in s:
            if ch=='-': row.append('---')
            else:
                cod=nt[3*k:3*k+3]
                if len(cod)<3: cod=cod+'N'*(3-len(cod))
                row.append(cod); k+=1
        nt_rows[g]=''.join(row)
    for g in gids:
        aa_cat[g].append(A[g]); nt_cat[g].append(nt_rows[g])
        r=nt_rows[g]; p12_cat[g].append(''.join(r[i]+r[i+1] for i in range(0,len(r),3)))
    parts.append((fam,L)); used+=1
def write(d,fp):
    with open(fp,'w') as fo:
        for g in gids: fo.write(">%s\n%s\n"%(g,''.join(d[g])))
write(aa_cat, os.path.join(out,'concat_aa.fasta'))
write(nt_cat, os.path.join(out,'concat_nt.fasta'))
write(p12_cat, os.path.join(out,'concat_p12.fasta'))
with open(os.path.join(out,'partitions.txt'),'w') as fo:
    for f,l in parts: fo.write("%s\t%d\n"%(f,l))
print("families_used",used,"skipped",skipped,"aa_cols",sum(l for _,l in parts),"nt_cols",3*sum(l for _,l in parts))
