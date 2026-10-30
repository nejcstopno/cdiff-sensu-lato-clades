# *Clostridioides difficile* sensu lato — thirteen divergent clades

Analysis code, derived tables and figures for the manuscript
**"*Clostridioides difficile* sensu lato: thirteen divergent clades with labile toxin loci
and almost no conjugative transposons."**

## What this repository contains

| path | contents |
|---|---|
| `doc/manuscript.md` | manuscript source |
| `doc/detailed_methods.md` | per-analysis methodology, including pre-registered interpretation rules, negative controls and the limitations carried into the manuscript |
| `tables/` | 132 derived tables (CSV) |
| `figures/` | 31 figures (PNG + PDF) |
| `scripts/` | SLURM submission scripts for the cluster steps |
| `MANIFEST.csv` | every file with its size |

## Scope of the analysis

- **30,970** quality-passed *Clostridioides* genome entries = **29,455** unique strains.
- A **460-genome working set** (205 divergent + 255 one-per-PopPUNK-cluster comparators) reducing to **431 unique strains**.
- **Thirteen divergent clades** (DC1–DC13) below an empty 97–98% ANI band.

## Key result tables

| table | result |
|---|---|
| `cdiff_tn916_ctn_by_clade.csv` | complete Tn916/CTn elements in 52.1% of sensu stricto vs 1.7% of divergent strains |
| `cdiff_tn916_host_restricted_test.csv` | the same comparison restricted to host-derived strains: 54.5% vs 1.5%, odds ratio 77.9 |
| `cdiff_toxin_state_evenness.csv` | toxin-state evenness per clade with depth-matched permutation tests |
| `cdiff_clade_specificity_leak.csv` | second-highest clade prevalence for all 1,110 clade-specific families |
| `cdiff_clade_primers_recommended.csv` | 12 recommended clade-specific primer pairs (8 validated in silico) |
| `cdiff_clade_primers_all_255.csv` | all 255 candidate pairs |
| `cdiff_metagenome_detection_limits.csv` | per-biome shotgun detection floors |
| `cdiff_dedup_ani_pairs_99_99.csv` | within-clade pairs at ≥99.99% ANI not collapsed by the metadata strain key |

## Reproducibility status — read this before relying on the scripts

`scripts/` holds the submission scripts for the steps whose exact command lines are
recorded. **It is not yet a complete end-to-end pipeline.** The upstream steps —
CheckM2 quality control, skani ANI, PopPUNK, GTDB-Tk, Prokka, Panaroo, IQ-TREE, Gubbins,
geNomad, ISEScan, IntegronFinder, MOB-suite, dbCAN, gRodon and the sourmash/branchwater
recruitment — were run interactively on the cluster and their scripts must still be
collected from the job directories before this repository can be called complete.
Software versions are listed in `doc/detailed_methods.md` §33.

Two large intermediates are **not** deposited and must be regenerated: the Panaroo
`gene_data.csv` (2.3 GB) and the primer BLAST hit table (156 MB).

## Citation

A Zenodo DOI will be minted from a tagged release at manuscript submission and added here.

## Licence

Code: MIT. Derived data tables: CC BY 4.0.
