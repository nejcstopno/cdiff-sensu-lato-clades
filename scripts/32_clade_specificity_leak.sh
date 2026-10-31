#!/bin/bash
#SBATCH -p mb-cpu
#SBATCH -c 8
# Second-highest clade prevalence for every clade-specific family.
# Quantifies how far the <=5%-outside rule admits families shared with small clades.
set -eo pipefail
cd cdiff_clades
python - <<'PY' > specificity_leak.csv
import csv
csv.field_size_limit(10**9)
fam   = {r["gene"]: r["clade"] for r in csv.DictReader(open("cs_families.csv"))}
clade = {r["genome_id"]: r["new_clade"] for r in csv.DictReader(open("strain431.csv"))}
sizes = {}
for g, c in clade.items(): sizes[c] = sizes.get(c, 0) + 1
print("gene,assigned_clade,assigned_prev_pct,second_clade,second_prev_pct,"
      "second_clade_n,n_other_clades_with_carrier,n_outside_strains,pct_outside")
with open("panaroo460/gene_presence_absence.csv") as fh:
    rd = csv.reader(fh); hdr = next(rd); cols = hdr[3:]
    idx = [i for i, c in enumerate(cols) if c in clade]
    cl  = [clade[cols[i]] for i in idx]
    for row in rd:
        gene = row[0]
        if gene not in fam: continue
        vals = row[3:]; cnt = {}
        for k, i in enumerate(idx):
            if i < len(vals) and vals[i].strip(): cnt[cl[k]] = cnt.get(cl[k], 0) + 1
        if not cnt: continue
        tgt  = fam[gene]
        prev = {c: 100.0 * n / sizes[c] for c, n in cnt.items()}
        others = sorted([(c, p) for c, p in prev.items() if c != tgt], key=lambda kv: -kv[1])
        sec, sp = others[0] if others else ("-", 0.0)
        nout = sum(n for c, n in cnt.items() if c != tgt)
        print(f"{gene},{tgt},{prev.get(tgt,0):.1f},{sec},{sp:.1f},{sizes.get(sec,0)},"
              f"{len(others)},{nout},{100.0*nout/len(clade):.2f}")
PY
