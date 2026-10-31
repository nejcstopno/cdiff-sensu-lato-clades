
import sys, os, csv, gzip
csv.field_size_limit(10**9)
pan=sys.argv[1]; out=sys.argv[2]; prokdirs=sys.argv[3:]
# 1) load prokka faa/ffn
faa={}; ffn={}
def rd(fp, d):
    name=None; buf=[]
    with open(fp) as fh:
        for line in fh:
            if line[0]=='>':
                if name: d[name]=''.join(buf)
                name=line[1:].split()[0]; buf=[]
            else: buf.append(line.strip())
    if name: d[name]=''.join(buf)
gids=[]
for pd_ in prokdirs:
    for gid in os.listdir(pd_):
        p=os.path.join(pd_,gid)
        if not os.path.isdir(p): continue
        f1=os.path.join(p,gid+'.faa'); f2=os.path.join(p,gid+'.ffn')
        if os.path.exists(f1) and os.path.exists(f2):
            rd(f1,faa); rd(f2,ffn); gids.append(gid)
gids=sorted(gids)
sys.stderr.write("genomes=%d proteins=%d cds=%d\n"%(len(gids),len(faa),len(ffn)))
# 2) presence/absence
fh=open(os.path.join(pan,'gene_presence_absence.csv'))
rdr=csv.reader(fh); hdr=next(rdr)
cols=hdr[3:]
idx={g:i for i,g in enumerate(cols)}
missing=[g for g in gids if g not in idx]
sys.stderr.write("genomes_not_in_panaroo=%r\n"%missing)
sel=[idx[g] for g in gids]
nfam=0; kept=[]; stats={'total':0,'core464':0,'single':0,'in_prokka':0}
for row in rdr:
    stats['total']+=1
    vals=[row[3+i] for i in sel]
    if any(v=='' for v in vals): continue
    stats['core464']+=1
    if any(';' in v for v in vals): continue
    stats['single']+=1
    if any(v not in faa or v not in ffn for v in vals): continue
    stats['in_prokka']+=1
    kept.append((row[0], vals))
sys.stderr.write("stats=%r\n"%stats)
os.makedirs(out, exist_ok=True)
with open(os.path.join(out,'family_stats.txt'),'w') as fo:
    for k,v in stats.items(): fo.write("%s\t%s\n"%(k,v))
with open(os.path.join(out,'genome_order.txt'),'w') as fo:
    fo.write("\n".join(gids)+"\n")
os.makedirs(os.path.join(out,'fam_aa'), exist_ok=True)
os.makedirs(os.path.join(out,'fam_nt'), exist_ok=True)
names=[]
for fam,vals in kept:
    safe=fam.replace('/','_').replace(' ','_')
    names.append(safe)
    with open(os.path.join(out,'fam_aa',safe+'.faa'),'w') as fo:
        for g,v in zip(gids,vals): fo.write(">%s\n%s\n"%(g,faa[v].rstrip('*')))
    with open(os.path.join(out,'fam_nt',safe+'.fna'),'w') as fo:
        for g,v in zip(gids,vals): fo.write(">%s\n%s\n"%(g,ffn[v]))
with open(os.path.join(out,'families.txt'),'w') as fo: fo.write("\n".join(names)+"\n")
print("families_written", len(names))
