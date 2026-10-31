
from Bio import SeqIO
from Bio.Seq import Seq
import sys
inp, out = sys.argv[1], sys.argv[2]
n=0
with open(out,'w') as o:
    for r in SeqIO.parse(inp,'fasta'):
        s = r.seq[:len(r.seq)-(len(r.seq)%3)]
        p = str(s.translate(table=11, to_stop=False)).rstrip('*')
        if len(p) >= 30:
            o.write(f">{r.id}\n{p}\n"); n+=1
print("proteins written", n)
