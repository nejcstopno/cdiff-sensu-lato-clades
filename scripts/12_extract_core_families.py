
import sys, os, csv
csv.field_size_limit(10**9)
pan=sys.argv[1]; out=sys.argv[2]; og_fp=sys.argv[3]; thresh=float(sys.argv[4]); prokdirs=sys.argv[5:]
faa={}; ffn={}
def rd(fp,d):
    name=None; buf=[]
    for line in open(fp):
        if line[0]=='>':
            if name: d[name]=''.join(buf)
            name=line[1:].split()[0]; buf=[]
        else: buf.append(line.strip())
    if name: d[name]=''.join(buf)
gids=[]
for pd_ in prokdirs:
    for gid in sorted(os.listdir(pd_)):
        p=os.path.join(pd_,gid)
        if not os.path.isdir(p): continue
        f1=os.path.join(p,gid+'.faa'); f2=os.path.join(p,gid+'.ffn')
        if os.path.exists(f1) and os.path.exists(f2):
            rd(f1,faa); rd(f2,ffn); gids.append(gid)
gids=sorted(gids)
og=[l.strip() for l in open(og_fp) if l.strip()]
ingroup=[g for g in gids if g not in og]
sys.stderr.write("genomes=%d ingroup=%d outgroup=%d\n"%(len(gids),len(ingroup),len(og)))
rdr=csv.reader(open(os.path.join(pan,'gene_presence_absence.csv'))); hdr=next(rdr)
idx={g:i for i,g in enumerate(hdr[3:])}
need=int(round(thresh*len(ingroup)))
stats={'total':0,'og_all_single':0,'ingroup_ok':0,'in_prokka':0}
kept=[]
for row in rdr:
    stats['total']+=1
    ogv=[row[3+idx[g]] for g in og]
    if any(v=='' or ';' in v for v in ogv): continue
    stats['og_all_single']+=1
    inv={g:row[3+idx[g]] for g in ingroup}
    present={g:v for g,v in inv.items() if v!='' and ';' not in v}
    if len(present)<need: continue
    stats['ingroup_ok']+=1
    allv=dict(zip(og,ogv)); allv.update(present)
    allv={g:v for g,v in allv.items() if v in faa and v in ffn}
    if any(v not in allv for v in og): continue
    if len(allv)-len(og) < need: continue
    stats['in_prokka']+=1
    kept.append((row[0],allv))
sys.stderr.write("stats=%r\n"%stats)
os.makedirs(out,exist_ok=True)
for sub in ('fam_aa','fam_nt'): os.makedirs(os.path.join(out,sub),exist_ok=True)
open(os.path.join(out,'genome_order.txt'),'w').write("\n".join(gids)+"\n")
with open(os.path.join(out,'family_stats.txt'),'w') as fo:
    for k,v in stats.items(): fo.write("%s\t%s\n"%(k,v))
names=[]
for fam,allv in kept:
    safe=fam.replace('/','_').replace(' ','_')
    names.append(safe)
    with open(os.path.join(out,'fam_aa',safe+'.faa'),'w') as fo:
        for g,v in allv.items(): fo.write(">%s\n%s\n"%(g,faa[v].rstrip('*')))
    with open(os.path.join(out,'fam_nt',safe+'.fna'),'w') as fo:
        for g,v in allv.items(): fo.write(">%s\n%s\n"%(g,ffn[v]))
open(os.path.join(out,'families.txt'),'w').write("\n".join(names)+"\n")
print("families_written",len(names))
