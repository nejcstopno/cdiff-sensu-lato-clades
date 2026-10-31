
import sys
aln,ids,out=sys.argv[1:4]
keep=set(l.strip() for l in open(ids) if l.strip())
w=False; n=0
with open(out,'w') as fo:
    for line in open(aln):
        if line[0]=='>':
            w = line[1:].split()[0] in keep
            n += w
        if w: fo.write(line)
print(out, n)
