#!/bin/bash
#SBATCH -p mb-cpu
#SBATCH -c 4
# Within- and between-clade median ANI from the divergent all-versus-all skani matrix.
# Also flags within-clade pairs at >=99.99% ANI that the metadata strain key did not collapse.
set -eo pipefail
cd cdiff_clades
python - <<'PY' > dc_pairwise_ani.tsv
import csv, statistics, collections, os
cl = {r["genome_id"]: r["new_clade"] for r in csv.DictReader(open("clades205.csv"))}
pairs, within = collections.defaultdict(list), collections.defaultdict(list)
with open("divergent_all_vs_all.tsv") as fh:
    rd = csv.reader(fh, delimiter="\t"); hdr = next(rd)
    qi, ri, ai = hdr.index("Ref_file"), hdr.index("Query_file"), hdr.index("ANI")
    for row in rd:
        a = os.path.basename(row[qi]).rsplit('.', 1)[0]
        b = os.path.basename(row[ri]).rsplit('.', 1)[0]
        ca, cb = cl.get(a), cl.get(b)
        if not ca or not cb: continue
        (within[ca] if ca == cb else pairs[tuple(sorted((ca, cb)))]).append(float(row[ai]))
print("type\tclade_a\tclade_b\tn_pairs\tmedian_ANI\tmin_ANI\tmax_ANI")
for k, v in sorted(within.items()):
    print(f"within\t{k}\t{k}\t{len(v)}\t{statistics.median(v):.2f}\t{min(v):.2f}\t{max(v):.2f}")
for (x, y), v in sorted(pairs.items()):
    print(f"between\t{x}\t{y}\t{len(v)}\t{statistics.median(v):.2f}\t{min(v):.2f}\t{max(v):.2f}")
PY
