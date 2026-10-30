#!/bin/bash
#SBATCH -p mb-cpu
#SBATCH -c 32
# Tn916 / CTn homology search against all 460 proteomes.
# Queries: the 21 translations >=60 aa of Tn916 (GenBank U09422.1).
set -eo pipefail
source "$CONDA_PREFIX_ROOT/etc/profile.d/conda.sh"
conda activate AMOA-SEQ
W=cdiff_clades/tn916; mkdir -p "$W"; cd "$W"
if [ ! -s all460.faa ]; then
  for f in ../prokka460/*/*.faa; do
    g=$(basename "$(dirname "$f")")
    awk -v G="$g" '/^>/{sub(/^>/,">"G"|");print;next}{print}' "$f"
  done > all460.faa
fi
makeblastdb -in all460.faa -dbtype prot -out all460
blastp -query tn916_queries.faa -db all460 \
  -outfmt "6 qseqid sseqid pident length qlen slen evalue bitscore" \
  -evalue 1e-10 -max_target_seqs 100000 -num_threads 32 > tn916_hits.tsv
# Calling rule (fixed before inspection):
#   component present  : >=50% identity over >=70% of query length
#   tet(M) present     : >=90% identity over >=90% of query length
#   complete element   : integrase AND excisionase AND >=4 of 6 conjugation-module genes
