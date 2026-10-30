# Detailed methods

**Clostridioides difficile sensu lato: thirteen divergent clades with labile toxin loci
and a reduced oxidative-stress system**

This document gives the full method for every analysis in the project, in the order the
results are presented. It supersedes the earlier per-phase notes
(`cdiff_clade_redefinition_methods.md`, `methods_note_dating.md`,
`methods_note_rigorous_dating.md`, `cdiff_toxin_architecture_notes.md`,
`cdiff_hgt_methods.md`, `cdiff_lifestyle_growth_assessment.md`,
`cdiff_consolidated_methods_and_findings.md`), several of which carry values from before
the deduplication and rooting corrections. Where a stated number differs between this
document and those, **this document is authoritative**.

All computation ran on an HPC cluster (SLURM, 256-core / 1 TB partition) unless noted.

---

## 0. Conventions that apply throughout

**Denominators.** Of 32,957 assemblies collected, 30,972 pass quality control. Two of
those are non-*Clostridioides* and were excluded, leaving **30,970 genome entries**
corresponding to **29,455 unique strains**. The 460-genome working set reduces to **431
unique strains**. Every frequency statistic in the manuscript is computed on unique
strains, never on genome entries; where a figure shows entries this is stated in its
caption.

**Comparability rule.** Comparative claims between clades use only the **eleven clades
with at least six unique strains** — nine divergent (DC1–DC8, DC10) plus Cds_C1-C4 and
Cds_C5. DC9 (5 strains), DC11 (1), DC12 (2) and DC13 (1) are excluded from comparisons
and reported descriptively. Any statement in an earlier document of the form "N of 10
comparable divergent clades" predates deduplication and is wrong; the correct
denominator is nine.

**Rarefaction.** Where a per-clade count depends on sample size (clade-specific gene
families, CAZyme counts, toxin-state richness), values are rarefied to a common depth by
repeated subsampling without replacement, with the number of draws stated per analysis.

**Statistics.** Two-sided tests throughout. Spearman rank correlation for clade-level
associations, Fisher's exact test for 2x2 contingency, Mann-Whitney U for distribution
shifts, binomial tests against an empirical background for enrichment or depletion.
Every reported correlation states its *n* and the population it was computed over.

**Multiple testing.** Per-clade and per-marker *p*-values are reported **uncorrected**, and
inference rests on the aggregate test within each analysis rather than on any individual
clade. Three families of related tests arise, and Benjamini–Hochberg false-discovery control
within each family is reported alongside the raw values in
`cdiff_multiple_testing_policy.csv`:

1. **Toxin-state evenness, eight per-clade permutation tests.** DC6 and DC2 survive at *q* = 0.028, DC3 becomes marginal at *q* = 0.063, and DC8 (*q* = 0.19) does not survive. The aggregate permutation test on the mean across the eight clades is a single test and is unaffected. The manuscript's claim is the aggregate one; DC3 is explicitly not relied upon.
2. **Oxidative-stress correlations, three tests.** All three survive (*q* = 0.012, 0.038, 2.2×10⁻¹¹).
3. **Ecology correlations, two tests.** Both were already non-significant uncorrected (*p* = 0.35, 0.92) and remain so.

Correction is applied within a family, not across the document, because the families test
unrelated hypotheses; the family memberships above are declared rather than chosen after the
fact. No claim in the manuscript depends on a test that survives only without correction.

---

## 1. Genome collection and quality control

Assemblies were drawn from the in-house *Clostridioides* collection at the Agricultural
Institute of Slovenia together with public assemblies downloaded from EnteroBase and
NCBI, giving 32,957 FASTA files (directory `genomes_fixed`; the separate
`cdiff_genomes_enterobase` download folder holds 32,105 files and is not the analysis
set).

Quality was assessed with **CheckM2 1.0.2** using the default lineage-free model.
Genomes were retained at **completeness >= 95% and contamination <= 5%**, which passes
30,972 and fails 1,985. No N50 or contig-count filter was applied at this stage;
contig counts are carried through and reported per genome, because fragmentation matters
for the locus-architecture and plasmid analyses but not for ANI or gene content.

*Output:* `cdiff_genome_qc_32957.csv`.

## 2. Species screening

Two genomes passing QC are not *Clostridioides*: GCF_002865995.1 (*Paraclostridium
sordellii*) and strain AF351-6 (*Clostridium_J senegalense*). Both were identified by
ANI to type-strain references and removed, and both had previously been reported as
"divergent clades" by an earlier in-house analysis. Two further earlier clades were
artefacts: one was a zero-byte file and one comprised these same two genomes.

*Output:* `cdiff_species_screen_30975.csv`, `cdiff_curated_sensu_lato_30970.csv`.

## 3. Average nucleotide identity

ANI was computed with **skani 0.2.2** (`skani dist`, default `-m 1000` marker
compression) against a six-genome *C. difficile* 630 reference group: 630
(GCF_000009205.2), 630-delta-erm (GCF_002080065.1), DSM 1296T (GCF_001077535.1),
FDAARGOS_267 (GCF_002073735.2), CD161 (GCF_003095675.1) and CDT4 (GCF_003095695.1).
Each genome's ANI to the group is the maximum over the six.

**Taking the maximum is conservative with respect to the result we report, and deliberately
so.** The maximum over six references is necessarily at least as high as the value against
any single reference, so this choice inflates every genome's apparent identity to sensu
stricto. It therefore pulls genomes *toward* the reference group and works to **close** the
97–98% gap, not to open it. Finding the band empty despite the most gap-closing of the
available summary statistics is a stronger result than finding it empty against one
arbitrarily chosen reference, and the panel is not an arbitrary choice of convenience. Using
the mean or the median over the panel, or any single panel member, can only lower the
identities and widen the gap.

The reference panel matters. Two genomes widely used as *C. difficile* references,
**TW11 (GCF_009362915.1) and 12038 (GCF_003697225.1)**, are 99.92% identical to each
other but only 96.15-96.39% identical to 630; they are clade-5 anchors, not sensu
stricto references. Including them lifts 2,798 clade-C5 genomes above a 98% cutoff and
closes the species gap artificially. They were therefore excluded from the reference
group, and this is reported as a methodological caution rather than buried.

For the divergent genomes, a complete all-versus-all ANI matrix was computed
(`divergent_all_vs_all.tsv`). Sketches for all 30,976 genomes were retained to allow
re-screening without recomputation.

## 4. Clade delimitation

Clades below the species gap were delimited by **average-linkage hierarchical clustering
on the ANI distance matrix** of the 205 divergent entries, with the cut taken at
**97% identity**. The threshold was not chosen a priori: a scan from 88% to 99% in
0.1-point steps shows the thirteen-clade solution is invariant across **96.5-97.5%**, a
1.0-point plateau, and the cut was placed at its centre.

Two independent derivations agree:
1. complete all-versus-all clustering of the 205 divergent entries;
2. a greedy-representative pass over all 30,972 genomes (230 representatives at 97%
   identity), which returns the identical partition with identical membership counts.

*Outputs:* `cdiff_divergent_threshold_scan.csv`, `cdiff_divergent_clades_13.csv`,
`cdiff_divergent_genome_assignments_205.csv`, `cdiff_clade_assignments_all_genomes.csv`.

## 5. Strain deduplication

Genome entries were collapsed to strains using a **strain key** built from, in priority
order: BioSample accession, PubMLST isolate identifier, EnteroBase barcode, and
submitter strain name after normalisation (case, whitespace, punctuation and common
prefixes). Entries sharing a key are one strain; one representative per strain was
chosen by highest completeness, then fewest contigs.

This matters disproportionately for the divergent clades: all 29 redundant entries in
the 460-genome working set fall in them. DC9 drops from 7 entries to 5 strains and so
below the comparability threshold; DC11's two entries are a single strain; DC5 loses
three of twelve (HGP05, HGP07 and HGP47 each appeared twice, once as a deposited
assembly and once as a database barcode).

**ANI cross-check, and what it found.** The metadata hierarchy above cannot detect an
isolate deposited twice under different BioSamples by different groups, so it was
cross-checked against the divergent all-versus-all ANI matrix: every within-clade genome
pair at **≥99.99% ANI** was flagged and compared against the strain key. This was intended
as a positive control and did not return one. **120 within-clade pairs sit at ≥99.99% ANI,
and 95 of them were not collapsed by the strain key.** Two different situations are mixed
in that set and ANI alone cannot separate them:

- *Genuine re-deposition.* Several pairs match an EnteroBase assembly to the underlying public read accession — `CLO_AA7548AA_AS` / `ERR232399`, `CLO_CA5277AA_AS` / `ERR232398`, `CLO_CA3594AA_AS` / `SRR3629298` and others, all at 99.99–100% — i.e. one isolate reaching the archives by two routes under unrelated identifiers.
- *Clonal sampling series.* Others are distinct named isolates from one study whose genomes are near-identical: the HGP series from a single Western Australian survey (HGP05/HGP19/HGP43/HGP71/HGP78-2/HGP79 in DC5; HGP14/HGP30/HGP33/HGP78 in DC9), the Slovenian sediment isolates S1-S-1/S3-P-5/S16-S-2 in DC4, and the ZZV23 series in DC2.

For the statistics in this work both have the same consequence — they are
pseudo-replication, not independent observations — so a **conservative strain definition**
was derived by single-linkage clustering of each divergent clade at 99.99% ANI. This reduces
**176 metadata strains to 135 ANI clusters**, with DC1 falling 45 → 30, DC3 26 → 21,
DC5 9 → 4, DC9 5 → 2 and DC2 39 → 35.

**The metadata strain key remains the primary definition**, because collapsing genuinely
distinct clonal isolates discards real sampling and because 99.99% single-linkage will chain
across an outbreak series. The conservative definition is carried as a sensitivity analysis
wherever a headline statistic depends on per-clade strain counts (§18). Note that sensu
stricto was **not** ANI-collapsed — the all-versus-all matrix covers only the divergent
genomes — so every such sensitivity analysis compares collapsed divergent clades against an
uncollapsed reference, which biases against the result being tested.

*Outputs:* `cdiff_strain_keys_30970.csv`, `cdiff_strain_redundancy_by_clade.csv`,
`cdiff_working_set_460_dedup.csv`, `cdiff_dedup_ani_crosscheck_by_clade.csv`,
`cdiff_dedup_ani_pairs_99_99.csv`.

## 6. Population structure within sensu stricto

ANI cannot subdivide sensu stricto — the largest cluster still holds 27,989 genomes at
98% linkage. **PopPUNK 2.7.8** was therefore run on the full set (sketch, model fit and
assignment), resolving 30,757 genomes into **255 strain clusters**. As a consistency
check, none of the 70 clusters containing a genome with a published clade designation
spans more than one published clade.

*Output:* `cdiff_poppunk_clusters_by_clade.csv`.

## 7. Taxonomic placement and concordance with published nomenclature

**GTDB-Tk 2.4.1** (`classify_wf`) against **GTDB release r226** placed every divergent
genome. Twelve of thirteen clades correspond to exactly one GTDB genomospecies; the
partition is finer than GTDB, with *difficile_F* splitting into four clades and
sp020641055 into two. **DC12 receives no GTDB species assignment.**

Concordance with the published cryptic-clade nomenclature was established from
**archetype sequence types** rather than by eye. Published archetypes were located in
the MLST-typed table and their clade membership recorded; each falls in exactly one
clade:

| archetype ST | published clade | falls in |
|---|---|---|
| ST181 | C-I | DC1 |
| ST200 | C-II | DC3 |
| ST369 | C-III | DC2 |
| ST919 (strain TUM20227) | C-IIIb | DC7 |

DC2's median ANI of 89.27% to the 630 group independently matches the published C-III
range of 89.2-89.4%. **No archetype ST or accession has been designated for C-IV, C-V,
C-VI or C-VII**, so the remaining nine clades are reported as unresolved against that
nomenclature rather than inferred.

**Internal consistency check on the C-IIIa/C-IIIb mapping.** The last two rows of that table
are not independent: the preprint erecting C-IIIa and C-IIIb separated them at **95.2% ANI**,
so if ST369 → DC2 (C-IIIa) and ST919 → DC7 (C-IIIb) both hold, DC2 and DC7 must themselves
be roughly 95% identical. If instead they returned a value near the ≈89% typical of
unrelated divergent clade pairs, the C-IIIb assignment — and the abstract sentence resting
on it — would be wrong. The check was run against the existing all-versus-all matrix rather
than recomputed:

| pair | genome pairs | median ANI | range |
|---|---|---|---|
| DC2 ↔ DC7 | 490 | **96.10%** | 95.42–96.45% |

DC2 is DC7's second-closest divergent clade (after DC9 at 96.18%) and DC7 is DC2's closest,
and the value sits just above the published C-IIIa/C-IIIb separation rather than at the
inter-clade background. **The mapping is consistent with our own data.** For context, the
full between-clade matrix spans 94.77–96.18% among these clades, so 96.10% is at the high
end, as the mapping requires. Within-clade medians for comparison are 99.56% (DC2) and
99.32% (DC7).

**A second nomenclature, independently concordant.** The Rodríguez laboratory's working
clade numbering for Costa Rican and Slovenian isolates (prefix before the `/` in their
designations) maps **one-to-one** onto our partition across the strains we could match:

| their prefix | our clade |
|---|---|
| 10 | DC1 |
| 12 | DC3 |
| 4 | DC2 |
| 3 | DC4 |
| 6 | DC7 |
| 5 | DC8 |
| 8 | DC12 |

Seven prefixes, seven distinct clades, with no prefix splitting across our clades and no two
prefixes merging into one. This is a second nomenclature concordant with the partition and is
independent of the archetype-ST anchors above. Their accompanying *letter* labels agree less
well: 5/C-IIIb is our DC8 rather than DC7, and three isolates labelled C-I in a collaborator
spreadsheet (ZZV23-12520, ZZV23-12542, ZZV23-12543) are DC7 = C-IIIb, where the numeric
prefix 6 is correct and the letter label is not.

*Outputs:* `cdiff_clade_concordance.csv`, `cdiff_between_clade_ani.csv` (all 78 between-clade
and 12 within-clade median ANI values, derived from `divergent_all_vs_all.tsv`),
`cdiff_ONT_panel_clade_assignment.csv`.

## 8. Working set, annotation and pangenome

Comparative gene-content work used a **460-genome working set**: all 205 divergent
entries plus 255 sensu stricto comparators, one per PopPUNK strain cluster, so that the
reference group is a diversity sample rather than a redundant clinical collection.

All 460 were **uniformly re-annotated with Prokka 1.14.6** (`--kingdom Bacteria`),
discarding any submitter annotation, so that gene calls are comparable across genomes of
different provenance. The pangenome was built with **Panaroo 1.5.0** in
`--clean-mode moderate`. Moderate rather than strict was chosen deliberately: strict mode
removes genes supported by few genomes, which is precisely the signal a clade-specific
analysis needs, and at 88-96% ANI across the ingroup the stricter paralogue-splitting
heuristics discard real low-frequency families.

The pangenome holds 16,101 gene families (2,270 core, 322 soft core, 2,079 shell, 11,430
cloud).

**The pangenome was not recomputed after deduplication.** Removing genome columns from a
presence/absence matrix cannot create or merge gene families, so the family definitions
are unaffected; what deduplication changes is *prevalence within a clade*, and so only
the clade-specific calls were re-derived on the 431 strains.

## 9. Clade-specific gene families

A family is **clade-specific** when it is present in **>= 90% of the clade's members and
<= 5% of genomes outside it**. Because the 90% criterion is sensitive to clade size,
counts were **rarefied to six strains with 50 resamples**, and the rarefied mean is
reported.

Deduplication changes one clade materially: DC5 falls from 96 families to **63**, because
its three duplicated strains caused rarefied draws to resample the same strain and
inflate apparent within-clade prevalence. Every other clade moves by four families or
fewer.

The union of clade-specific families across all clades is **1,110** (an earlier figure of
1,093 that appears in several intermediate documents is wrong).

**The ≤5% rule permits sharing with small clades, and the resulting counts are inflated.**
The outside threshold is evaluated across all 431 strains, so a family fixed in a large
clade and *also fixed* in a small one still passes: a family present in 100% of DC1 and 100%
of DC11 (one strain) sits at 0.2% outside and is counted DC1-specific. The rule therefore
identifies families that are specific to a *lineage block* rather than strictly private to
one clade.

To quantify this, the **second-highest clade prevalence** was computed for every family and
is now reported as a column alongside the assigned clade
(`cdiff_clade_specificity_leak.csv`). Requiring **zero carriers outside the assigned clade**
reduces 1,110 families to **358 strictly exclusive**, and the loss is very unevenly spread:

| clade | families (≤5% rule) | strictly exclusive | % strict | median second-clade prevalence |
|---|---|---|---|---|
| DC10 | 93 | 63 | 67.7 | 0.0 |
| DC3 | 20 | 15 | 75.0 | 0.0 |
| DC4 | 34 | 22 | 64.7 | 0.0 |
| DC2 | 51 | 32 | 62.7 | 0.0 |
| DC5 | 54 | 31 | 57.4 | 0.0 |
| DC6 | 18 | 10 | 55.6 | 0.0 |
| Cds_C5 | 52 | 27 | 51.9 | 0.0 |
| DC12 | 35 | 17 | 48.6 | 8.3 |
| DC7 | 99 | 41 | 41.4 | 20.0 |
| Cds_C1-C4 | 10 | 3 | 30.0 | 20.7 |
| **DC1** | **97** | **25** | **25.8** | **100.0** |
| DC11 | 116 | 24 | 20.7 | 16.7 |
| DC9 | 32 | 6 | 18.8 | 43.7 |
| DC8 | 22 | 3 | 13.6 | 94.5 |
| DC13 | 377 | 39 | 10.3 | 20.0 |

**DC1 is the clade most affected.** For the median DC1-assigned family there exists another
clade in which that family is *also* at 100% prevalence — most often its sister DC6 (38
families) or DC11 (17). DC8's median second-clade prevalence of 94.5% has the same cause.
The systematic leaks follow sister relationships on the core tree (DC1–DC6–DC11, DC7–DC5,
DC5–DC9, DC10–DC13), which is what a lineage-block interpretation predicts.

**What this does and does not affect.** The qualitative conclusion that every comparable
divergent clade carries more clade-specific families than sensu stricto holds under both
definitions. The specific per-clade counts do not transfer between them and should be quoted
with the definition attached. **Primer design is unaffected**: it required single-clade
families and in-silico PCR validation independently, and all twelve recommended pairs —
including all eight validated ones — derive from strictly exclusive families with zero
outside carriers (verified in §32).

*Outputs:* `cdiff_clade_specific_genes_dedup.csv`, `cdiff_clade_specific_genes.csv`
(pre-deduplication, retained for comparison), `cdiff_clade_specificity_leak.csv`,
`cdiff_clade_specificity_by_clade.csv`.

## 10. Functional annotation and annotation depth

Clade-specific families were annotated with four independent systems so that annotation
depth could be *measured* rather than assumed:

- **KOfam** HMMs against the DRAM KEGG profile set, using the per-family gathering
  thresholds in `kofam_ko_list.tsv`;
- **Pfam-A** (HMMER 3.4 `hmmsearch --cut_ga`);
- **dbCAN 5.2.9** (`run_dbcan`, HMM + DIAMOND consensus) for carbohydrate-active enzymes;
- **MEROPS** by DIAMOND against `pepunit.dmnd` for peptidases.

Of the 1,110 families, Prokka named 205, KOfam assigned 206 orthologues, Pfam-A matched
579, dbCAN 38 and MEROPS 32. The union is 595, leaving **515 families (47%) with no
functional annotation from any source**. Pfam alone rescued 289 families that had
neither a gene name nor a KEGG orthologue, which is why it is reported separately rather
than folded into a single annotation rate.

Bakta and DRAM re-annotation were considered and rejected: neither would change the gene
*calls* (Prokka's ORF prediction is not the limiting step) and both would have broken
comparability with the pangenome already built on Prokka output.

*Outputs:* `cdiff_clade_specific_gene_annotation.csv`, `cdiff_clade_specific_KO.csv`.

## 11. KEGG module completeness

Module completeness was computed per genome from KOfam assignments using the KEGG module
definitions retrieved from the KEGG REST API (`/list/module`, `/link/module/ko`),
evaluating each module's block logic rather than counting KOs. A module is called
complete at **completeness >= 0.8**.

Pathway-level *enrichment* testing on the clade-specific families was considered and
rejected: with 47% of those families unannotated, an enrichment test is a test of
annotation bias, not of biology. Module completeness over the whole proteome avoids
that, at the cost of being less specific.

One module is clade-exclusive: **M00986 (sulfur reduction)** in 49 of 50 DC1 genomes and
0 of 410 others. It rests on a single orthologue (K18367, sulfhydrogenase), and no
phenotypic claim is made from it.

*Outputs:* `cdiff_module_completeness_by_clade.csv`, `cdiff_module_completeness_by_genome.csv`,
`cdiff_clade_specific_KEGG_pathways.csv`.

## 12. Core-genome phylogeny

**Why three different core-gene sets appear in this document.** Three are used — a 2,530-gene Panaroo core, a 1,455-gene codon core and bac120 — and the set changes with the question, not with the result. All three were fixed before the analyses using them were run, and no question was answered by choosing among sets after seeing their answers.

| Set | Size | Used for | Why this set |
|---|---|---|---|
| Panaroo core genes | 2,530 genes, 2.54 Mb | Primary phylogeny, clade monophyly, toxin-congruence constraint tree | Maximum phylogenetic signal available within the 460-genome working set, and defined by the same pangenome as every gene-content analysis, so tree and gene content stay internally consistent |
| Codon-aware core | 1,455 genes | Molecular dating | A codon-partitioned strict clock requires in-frame alignments; the 1,455 are the subset of the 2,530 passing in-frame codon alignment without internal stop codons. The reduction is a mechanical consequence of the clock model, not a selection |
| bac120 | 120 markers | Outgroup rooting | The outgroups are other genera, and a Panaroo core computed on 460 *Clostridioides* genomes does not extend to them. bac120 is defined across bacteria and is the only one of the three that can place the root |

Where two sets could answer the same question they were both run and both reported: rooting was performed on bac120 *and* on the Panaroo core restricted to genes shared with the outgroups, and the two give the same root at 100% ultrafast bootstrap.

The Panaroo core-gene alignment (2,530 genes, 2.54 Mb) was used for the primary
phylogeny. Trees were inferred with **IQ-TREE 2.3.0** under ModelFinder
(`-m MFP`) with 1,000 ultrafast bootstrap replicates, and with FastTree for a rapid
cross-check of topology. All fourteen multi-genome clades are recovered **monophyletic
with zero foreign tips and SH-like support of 1.00 at every clade ancestor**.

*Outputs:* `cdiff_core_genome_fasttree.nwk`, `cdiff_clade_monophyly_coregenome.csv`.

## 13. Outgroup rooting

Midpoint rooting was used in an earlier phase and gave a different and, as it turned out,
misleading root. The tree was re-rooted with **four outgroup genomes spanning three
genera**: *Paraclostridium sordellii* (GCF_002865995.1), *Metaclostridioides mangenotii*
(GCF_017873185.1), *Paraclostridium bifermentans* (GCF_019916025.1) and
*Terrisporobacter glycolicus* (GCF_036812735.1).

Two independent marker sets were used so the rooting does not depend on one gene
selection: the **bac120** marker set and the Panaroo **core-gene** set. Both give a
monophyletic ingroup at **100% ultrafast bootstrap** and place the root on a single
branch separating **103 genomes (DC2, DC4, DC5, DC7, DC8, DC9) from 357**. The 357
resolve further into 291 (Cds_C1-C4, Cds_C5, DC3, DC10, DC13) and 66 (DC1, DC6, DC11,
DC12); all three blocks are monophyletic and are used in the ancestral-state analysis.

*Outputs:* `ml464_bac120_outgroup_rooted.treefile`, `ml464_coregenes_outgroup_rooted.treefile`.

## 14. Recombination assessment, and its limitation

Recombination was assessed with **Gubbins 3.3.1** on the core-gene alignment.

**This is a known methodological compromise and is stated as such.** Gubbins detects
recombination as spatially clustered SNP density along a contiguous genome alignment;
running it on a concatenated core-gene alignment, with intergenic regions and gene order
removed, violates that spatial assumption. Breakpoints spanning gene boundaries are
mis-located and branch lengths are compressed — in this dataset by about 3.7-fold
relative to the unfiltered alignment. Two of the comparator studies in this field made
the same choice, so the compromise is not unusual, but it has two consequences we
enforce: **Gubbins branch lengths are not interpreted as substitution counts, and are
not used for dating.**

*Outputs:* `gubbins_recombination_summary.csv`, `clade_stem_recombination.csv`,
`gubbins_per_branch_statistics.tsv`.

## 15. Substitution saturation

Before any dating, saturation was tested three ways on the core alignment:

1. **Uncorrected versus model-corrected pairwise distances** over 399 clade pairs. A
   saturated alignment plateaus; this one is near-linear, R^2 = 0.986-0.999.
2. **Entropy-based saturation index**, which is 0.026-0.078 against 1.0 for fully
   saturated data.
3. **Site pattern counts** — only 2.9% of sites carry three or more states.

All three agree that the alignment is **not** saturated. An earlier phase concluded the
opposite and attributed branch-length compression to saturation; that compression is
caused by the Gubbins-on-concatenate issue in section 14, not by saturation.

*Outputs:* `saturation_regression_summary.csv`, `saturation_site_diagnostics.csv`,
`saturation_pairwise_distances.csv`.

## 16. Molecular clock and divergence dating

**Clock-signal test first.** Before fitting any clock we tested whether one is
supported. Two clock-free orderings of the fifteen clades — by root-to-tip *depth* and by
node *height* — should agree perfectly (Spearman rho = +1) if a strict clock holds. They
are unrelated: **rho = -0.356, n = 15, p = 0.19**. A strict clock therefore does not hold
on this tree.

**Rate provenance.** The two rates used in the literature for this organism,
**2.5x10^-9 and 1.5x10^-8 substitutions/site/year**, both originate from a single study
as a **long-term synonymous** clock derived from dS in non-recombining core CDS. That is
two orders of magnitude slower than the short-term transmission clock (~3.2x10^-7) used
for outbreak work. We apply them only in the long-term sense, and note that spore
dormancy makes the clock non-linear over these depths.

**Estimation.** Node ages were estimated with **BactDating 1.1.4** and **TreeTime
0.12.1** on the codon-aware 1,455-gene core tree under each rate as a fixed strict clock,
and separately under four defensible branch-length estimators of the same topology
(2.54 Mb core with GTR+F+I+R and with GTR+CAT, 1,455-gene codon core, Gubbins clonal
frame).

**What is reported.** No absolute ages are claimed. The spread across branch-length
estimators is ninefold, which combined with the sixfold published rate range gives
roughly **fiftyfold total uncertainty**; reporting a point estimate would be
indefensible. Within those bounds, published point estimates fall inside **six of eight**
brackets tested.

**Two arithmetic observations recorded for the literature.** First, the published "95%
credible intervals" are arithmetically **rate brackets**: at all four published nodes,
the lower bound multiplied by 1.5x10^-8 equals the upper bound multiplied by 2.5x10^-9 to
within 0.8%. Second, an earlier claim from this project that published dates were
"16.5-99x too old" was **wrong**, caused by comparing the wrong nodes: under correct
outgroup rooting, DC2 is not sister to all other sensu lato but sits inside the
103-genome clade, so the event dated in the literature as "C-III emerged" is the root of
our ingroup, not DC2's stem. The corrected comparison is ingroup root 8.15-48.88 Mya
against a published 47.61 (13.58-81.73), and C1-C5 MRCA 0.997-5.98 against 3.89
(1.11-6.71).

**Sampling-density control.** Because the node-depth ratio used in the comparison is
sensitive to how densely each clade is sampled, it was recomputed over subsamples: a
published-like ratio arises in 62.0% of draws at n = 6 per clade, 41.7% at n = 12, and
0% at n >= 160. The discrepancy is therefore a sampling-density effect, not a
contradiction.

*Outputs:* `clade_ages_outgroup_rooted.csv`, `clade_ages_per_rate.csv`,
`bactdating_rooted_clade_ages.csv`, `noclock_depth_vs_height_rooted.csv`,
`knight2021_interval_ratios.csv`, `cdiff_c15_subsampling_ratio_test.csv`,
`cdiff_c15_node_definition_comparison.csv`.

## 17. Toxin inventory

Toxin genes were inventoried **at protein level by homology search, not by annotation
name**, because Prokka names toxin homologues inconsistently across divergent genomes.
For each of eight targets (*tcdR*, *tcdB*, *tcdE*, *tcdA*, *tcdC*, *cdtA*, *cdtB*,
*cdtR*) the reference protein from *C. difficile* 630 was searched against all 460
Prokka proteomes, and for each hit the following were recorded: number of proteins,
longest protein length, completeness against the reference, percent identity,
**whether the protein sits at a contig edge**, nucleotide reference coverage, and maximum
nucleotide identity.

Each gene in each genome was then called **full_length**, **partial_internal** (truncated
but not at a contig boundary, so a genuine truncation rather than an assembly artefact)
or **absent**. The contig-edge flag is what separates a real pseudogene from a broken
assembly and is carried through every downstream count.

Locus architecture was reconstructed from contig coordinates and gene order, and span in
base pairs recorded per clade.

**The DC1/DC6 fused block: the supporting count, stated explicitly.** The claim that DC1 and
DC6 carry *cdtB*-*cdtA*-*cdtR*-*tcdR*-*tcdB*-*tcdE* as one contiguous block rests on a
single number — how many genomes carry all six genes internal to one contig with flanking
sequence on both sides — and that number is given here and in the Figure 4 legend rather
than left implicit.

| | DC1 | DC6 |
|---|---|---|
| strains in clade | 45 | 12 |
| strains with ≥1 toxin gene | 19 | 12 |
| strains carrying all six genes | 3 | 7 |
| …with all six on **one contig** | **3 of 3** | **5 of 7** |
| …internal, ≥1 kb flanking both sides | 3 | 4 |
| …independent at 99.99% ANI (§5) | 2 | 4 |
| block span | 13,988–13,989 bp | 13,993 bp |
| minimum flanking distance | 9,143 bp | 710 bp |

Eight assemblies in total carry the full block on one contig. Seven are internal with ≥1 kb
of flanking sequence on both sides; the eighth (DC6, `CLO_AA9754AA_AS`) sits 710 bp from a
contig end and is flagged edge-proximal. The two DC6 strains that carry all six genes but
not on one contig break at four genes, which is consistent with an assembly gap rather than
a different architecture. **Collapsing near-identical genomes leaves two independent DC1 and
four independent DC6 observations**, and six of the eight come from two study series.

The honest reading is that the fused architecture characterises a **minority of DC1 (3 of 45
strains)** and about half of DC6, not either clade as a whole, and that the span is strikingly
invariant (13,988–13,993 bp) wherever it occurs. This remains the claim in the manuscript
most in need of long-read validation.

*Outputs:* `cdiff_toxin_inventory_by_genome.csv`, `cdiff_toxin_architecture_by_clade.csv`,
`cdiff_toxin_domain_identity.csv`, `cdiff_toxin_loci_context.csv`,
`cdiff_fused_block_contig_evidence.csv`, `cdiff_fused_block_assembly_status.csv`.

## 18. Toxin-state diversity

A **toxin state** is the set of toxin genes present at any status in a strain — so
`tcdR+tcdA` and `tcdR+tcdB+tcdE+cdtR` are different states, and a strain with no toxin
gene is the state `none`. States were computed on the 431 unique strains.

For presentation, raw states were grouped into seven interpretable classes: no toxin
genes; PaLoc fragment only; CdtLoc only; *tcdA*+*tcdR* only; partial PaLoc + CdtLoc;
monotoxin PaLoc (*tcdR*-*tcdB*-*tcdE*); canonical PaLoc (five genes).

**Richness** was rarefied to six and twelve strains with 2,000 draws, reporting the mean
and the 2.5-97.5 percentile range.

**Evenness is the primary measure, and richness is secondary.** Richness is dominated by
singletons and counts `none` as a state, so a clade that is half non-toxigenic scores
high for the wrong reason. Evenness was therefore computed as **normalised Shannon
equitability over toxin-positive states only**, excluding non-toxigenic strains so they
cannot contribute. Simpson's D is reported alongside.

**Significance** was assessed by a depth-matched permutation test: for each clade, the
sensu stricto toxin-positive strains were subsampled to that clade's number of
toxin-positive strains **10,000 times**, and the observed evenness compared to the
resulting null. Results were aggregated across clades two ways — the same procedure
applied to the mean evenness of the eight testable clades, and Stouffer combination of
the per-clade p-values.

**Sensitivity to the strain definition.** Because the ANI cross-check in §5 found 95
uncollapsed within-clade pairs at ≥99.99% ANI, the entire analysis was repeated on the
conservative ANI-cluster strain definition (176 → 135 divergent strains). Sensu stricto was
**not** collapsed, since the all-versus-all matrix does not cover it, so the comparison runs
against an uncollapsed reference and is biased against the result being tested. Both runs
use one implementation, so the two columns are directly comparable to each other.

| | metadata strain (primary) | ANI cluster ≥99.99% (conservative) |
|---|---|---|
| sensu stricto evenness | 0.3787 over 7 states | 0.3787 over 7 states |
| observed mean, 8 clades | **0.8185** | **0.7957** |
| depth-matched null mean | 0.6253 | 0.6618 |
| null 95% range | 0.520–0.719 | 0.547–0.762 |
| draws ≥ observed / 10,000 | **0** | **26** |
| aggregate *p* | **< 10⁻⁴** | **0.0027** |

Per clade, DC6 strengthens (*p* = 0.0065 → 0.0051) and DC2 holds (0.0068 → 0.0277), while
**DC3 loses significance (0.0183 → 0.1372)** and DC5 and DC9 fall below the minimum depth
entirely. The aggregate conclusion is robust to the strain definition; the DC3 component is
not, and combined with its marginal *q* = 0.063 under false-discovery control (§0) the
manuscript does not rely on it.

The per-clade permutation implementation reproduces the primary analysis closely (DC2
0.0068 vs 0.0070, DC6 0.0065 vs 0.0067, DC1 0.1425 vs 0.1430, DC4 1.000 vs 1.000). The
aggregate null mean differs between implementations (0.625 here against 0.513 originally)
because of how the per-clade draw depths are pooled; both give *p* < 10⁻⁴ on the primary
definition, and the sensitivity comparison above is internally consistent because both of
its columns come from the same implementation.

*Outputs:* `cdiff_toxin_signatures_by_clade.csv`, `cdiff_toxin_state_evenness.csv`,
`cdiff_toxin_state_richness_rarefied.csv`, `cdiff_toxin_gene_prevalence_by_clade.csv`,
`cdiff_toxin_evenness_dedup_sensitivity.csv`,
`cdiff_toxin_evenness_aggregate_sensitivity.csv`, `cdiff_multiple_testing_toxin.csv`.

## 19. Toxin gene-tree versus core-tree congruence

Protein sequences for each toxin gene were extracted from the combined toxin alignment,
degapped, and **realigned per gene with MAFFT v7.526** (`--auto`). For each gene:

1. an unconstrained ML tree was inferred (**IQ-TREE 2.3.0**, `-m MFP`, 1,000 ultrafast
   bootstraps);
2. the outgroup-rooted core-genome tree was **pruned to that gene's strain set** and
   supplied as a **topology-only constraint** (`-g`, branch lengths and support stripped)
   for a second inference on the same alignment;
3. the two topologies were compared on that alignment with the **approximately unbiased
   test** (`-z trees -n 0 -zb 10000 -au`), which also reports KH, SH, RELL bootstrap and
   expected likelihood weights.

Normalised Robinson-Foulds distance between the free and constrained topologies was
computed as symmetric split difference divided by the total number of splits.
Within-subtree exclusivity was tested separately by pruning each gene's tree to that gene
and asking, per clade, whether the clade's MRCA contains any foreign tip.

**Interpretation rule set in advance:** a gene tree that does not reject the core
topology is reported as *not demonstrating discordance*, never as demonstrating
congruence, and no transfer is inferred from a non-significant test.

*Outputs:* `cdiff_toxin_core_congruence_AUtest.csv`, `cdiff_toxin_monophyly_tests.csv`,
`cdiff_toxin_ML_tree.nwk`, `cdiff_toxin_alignment.faa`.

## 20. Oxidative-stress system and ancestral state

Five Pfam domains were scored across the working set: **PF00199** (haem catalase),
**PF05067** (Mn catalase), **PF06397** (desulfoferrodoxin C-terminal), **PF01880**
(desulfoferrodoxin N-terminal) and **PF02915** (rubrerythrin), using HMMER 3.4
`hmmsearch --cut_ga`.

To polarise the characters, the **four outgroup genomes were annotated de novo** with
Prokka 1.14.6 and searched with the same five HMMs under the same gathering thresholds.
The HMMs were extracted from Pfam-A by accession because the local Pfam file is not
indexed for `hmmfetch`.

Ancestral states were reconstructed by **Fitch parsimony** on the clade-level
outgroup-rooted topology, each clade coded by majority presence (threshold 50% for
prevalence characters). Reconstruction was run both with and without the outgroups, and
both counts are reported, because the ingroup-only count is what an analysis without
outgroups would produce and it gives a different answer.

**Copy number was deliberately not reconstructed.** The outgroup counts come from a
different annotation pipeline than the ingroup table, and copy numbers are not comparable
across pipelines; only presence/absence is.

**Threshold sensitivity, because a 13-point difference decides a character state.** Majority
coding at 50% puts DC7 (55.6% haem-catalase prevalence) on the present side and DC8 (42.9%)
on the absent side. Since the reframing of the oxidative-stress result rests on these
reconstructions, the analysis was repeated at **30%, 50% and 70% thresholds and with
polymorphic clades (10–90%) coded as ambiguous**. The clade-level topology was rebuilt with
a **bifurcating** root for this test; re-rooting with `root_with_outgroup` produces a
trifurcating root that inflates the change count by one per character, and the bifurcating
tree reproduces the originally reported counts (4 and 6 at the 50% threshold).

| domain | coding | changes | ancestral state | clades present |
|---|---|---|---|---|
| PF06397 | 30% | 4 | ambiguous | 6 |
| PF06397 | 50% | 4 | ambiguous | 6 |
| PF06397 | 70% | 4 | ambiguous | 6 |
| PF06397 | polymorphic | 4 | ambiguous | 6 |
| haem catalase | 30% | 5 | ambiguous | 5 |
| haem catalase | 50% | 6 | ambiguous | 4 |
| haem catalase | 70% | 5 | **absent** | 3 |
| haem catalase | polymorphic | 4 | **absent** | 2 |

**PF06397 is completely insensitive to the coding threshold** — identical under all four
codings, which follows mechanically from its strict bimodality (prevalence takes only the
values 0, 94.7, 98.7 and 100%). It is therefore the character that carries the
reconstruction.

**Haem catalase is not stable, and its polarity flips.** The ancestral state is ambiguous at
the inclusive thresholds but resolves to **absent** at 70% and under polymorphic coding,
under which presence in DC5, DC9 and DC11 reads as *gain* rather than ancestral retention —
the opposite of the direction the ingroup-plus-outgroup reconstruction at 50% suggests. This
is reported rather than suppressed, and the manuscript does not rest the reframing on haem
catalase. What survives every coding is the weaker statement that suffices: **the ancestral
state cannot be resolved from these data**, so presence in the divergent clades cannot be
called an acquisition.

*Outputs:* `cdiff_oxidative_stress_all15_clades.csv`,
`cdiff_oxidative_stress_ancestral_state.csv`, `cdiff_outgroup_oxidative_domains.csv`,
`cdiff_ancestral_state_threshold_sensitivity.csv`.

## 21. Carbohydrate-active enzymes and the plant-association test

CAZymes were called with **dbCAN 5.2.9** (`run_dbcan`) on all 460 Prokka proteomes, under
two callers: a **strict** two-tool consensus (HMM and DIAMOND must agree) and a
**permissive** HMM-only caller. Both are reported, because a negative result under a
permissive caller is much stronger than one under a strict caller.

**The plant-association hypothesis was tested on a diagnostic family panel, not on
substrate aggregates.** dbCAN's high-level family-to-substrate mapping is promiscuous —
GH1 alone is tagged with xylan, arabinan, beta-mannan and nine other substrates — so
summing it manufactures a plant-degradation signal out of polyspecific families. Instead,
a panel of **47 diagnostic plant-cell-wall families** was specified in advance: cellulases
(GH5, GH8, GH9, GH12, GH44, GH45, GH48, GH74), xylanases (GH10, GH11, GH30), pectinases
and pectate lyases (GH28, PL1, PL2, PL3, PL9, PL10, PL11, CE8, CE12), mannanases (GH26),
galactanases (GH53), and ten plant-glycan carbohydrate-binding modules.

Positive and negative controls were built into the panel: *Bacillus*-type germinant
receptors (GerA) should be **absent** from *C. difficile* and are; CspBAC and SleB/SleC
should be **present** in every genome and are. Cellulosome components (dockerin, cohesin)
were scored separately.

Per-clade CAZyme counts were rarefied to six genomes with 50 resamples.

*Outputs:* `cdiff_plant_cellwall_panel_by_clade.csv`,
`cdiff_cazyme_class_by_clade_rarefied.csv`, `cdiff_cazyme_families_by_genome.csv`.

## 22. Persistence machinery

A panel of **65 Pfam domains** covering sporulation, germination, spore-coat assembly and
stress response was scored with HMMER 3.4 `--cut_ga`; 41 were detected. Copy number per
genome was compared across clades, and domains that are copy-number identical in all 460
genomes were counted explicitly, because the relevant question is whether the apparatus is
*elaborated* in divergent clades rather than whether it is present.

*Outputs:* `cdiff_persistence_domains_by_clade.csv`,
`cdiff_persistence_domains_by_genome.csv`, `cdiff_persistence_domains_rarefied.csv`.

## 23. Catabolic breadth

Complete KEGG modules, transporter KOs and PTS-system KOs were counted per genome from the
KOfam assignments and rarefied to six genomes with 50 resamples, to test whether divergent
clades have broader or narrower carbon utilisation than sensu stricto.

*Output:* `cdiff_catabolic_breadth_by_clade.csv`.

## 24. Growth-rate prediction

Maximal growth rate was predicted with **gRodon 1.0.0** in `mode = "full"`, using
ribosomal proteins as the highly-expressed gene set, run on Prokka CDS nucleotide
sequences. Minimal doubling time and its confidence interval were recorded per genome.

**Stated limitation:** gRodon infers growth potential from codon-usage bias, which records
selection history rather than current conditions, and its calibration set is culturable
mesophiles. Absolute doubling times from it are not meaningful for an obligate anaerobe
sampled from soil; only relative ranks across clades are interpreted, and the manuscript
avoids calling any clade "fast-growing" or "copiotrophic" on this basis.

*Outputs:* `cdiff_growth_rate_by_clade.csv`, `cdiff_growth_rate_by_genome.csv`.

## 25. Genome size

Assembly length was compared between divergent and sensu stricto strains by Mann-Whitney
U on unique strains, and per clade by median. Because assembly length is sensitive to
fragmentation, the comparison was repeated restricted to genomes below the median contig
count, and the difference holds.

*Output:* `cdiff_genome_size_by_clade.csv`.

## 26. Mobilome

Four orthogonal tools were run on all 460 genomes:

- **geNomad 1.13.0** (`end-to-end`) for prophage and plasmid contig prediction;
- **ISEScan 1.7.3** for insertion sequences;
- **IntegronFinder 2.0.6** for complete integrons, CALIN elements and In0;
- **MOB-suite 3.1.9** (`mob_recon`) for plasmid replicon and relaxase typing and MPF
  classification.

Prophage burden is reported as the fraction of assembly length on prophage-predicted
contigs, not as a contig count, so that it is comparable across assemblies of different
fragmentation.

**Tool coverage gap, and the dedicated search that closes it.** ICEs and conjugative
transposons of the Tn916/CTn family are not detected by any of the four tools above — MOB-suite
MPF typing found a single conjugative element across the whole set, which is implausible and
reflects tool coverage rather than biology. Because Tn916-family CTns are the principal
accessory-gene vehicle in this organism, and because a surviving quantitative claim is that
mobile-element content differs across every divergent clade, a dedicated homology search was
run rather than left as a footnote.

**Method.** All 24 coding sequences of **Tn916 (GenBank U09422.1)** were retrieved from NCBI
and the 21 translations ≥60 aa used as queries: the integrase (Int-Tn, 405 aa and its 361 aa
and 324 aa variants), the excisionase (Xis-Tn, 67 aa), *tet*(M) (639 aa), and the
conjugation-module proteins (815 aa FtsK/SpoIIIE-like coupling protein, 754 aa, 461, 333, 329
and 310 aa). These were searched with `blastp` (BLAST+ 2.16.0, `-evalue 1e-10`) against a
concatenation of all 460 Prokka proteomes (1,754,993 proteins) with genome-tagged headers.

**Calling rule, fixed before inspection.** A component counts as present at **≥50% identity
over ≥70% of the query length**; *tet*(M) at ≥90% identity over ≥90% length. A genome carries
a **complete element** where it has a Tn916-family integrase *and* the excisionase *and* at
least **four of the six** conjugation-module genes; **partial** where it has an integrase and
at least one module gene but not the complete set. Calls were then collapsed to unique strains.

| clade | strains | complete CTn | % | *tet*(M) | median module genes |
|---|---|---|---|---|---|
| **Cds_C1-C4** | 236 | **123** | **52.1** | 7 | 6.0 |
| Cds_C5 | 19 | 2 | 10.5 | 2 | 0.0 |
| DC7 | 9 | 1 | 11.1 | 1 | 0.0 |
| DC2 | 39 | 1 | 2.6 | 0 | 0.0 |
| DC1 | 45 | 1 | 2.2 | 0 | 0.0 |
| DC3, DC4, DC5, DC6, DC8, DC9, DC10, DC11, DC12, DC13 | — | **0** | **0.0** | 0 | 0.0 |

**Complete elements are present in 123 of 236 sensu stricto strains (52.1%) against 3 of 176
divergent strains (1.7%)** — Fisher odds ratio 62.8, *p* = 8.8×10⁻³⁴ — and are absent from ten
of the thirteen divergent clades.

**This is not a detection-sensitivity artefact**, and the control is the integrase identity
itself: Tn916-family integrase hits match at median **62.5% identity in divergent clades
against 64.3% in sensu stricto**, i.e. no more diverged in the group where the element is
rare, and 47 of 205 divergent genomes carry at least one conjugation-module gene. What the
divergent genomes lack is the *co-occurring complete module*, not detectable homology. Had the
50% threshold been excluding diverged copies, divergent-clade identities would sit
systematically lower; they do not.

**Interpretation limit.** Component identities to Tn916 itself in the complete-element
carriers are median 52–79% (maxima at 100%), so most calls are **CTn-family relatives** of the
kind catalogued in strain 630 (CTn1, CTn2, CTn4, CTn5, CTn7) rather than Tn916 proper. The
search establishes family membership and element completeness, not element identity, and no
claim is made about which specific CTn is present in any genome.

The result qualifies the mobilome conclusion rather than extending it: divergent clades carry
**more** prophage and **more** plasmids but **almost no conjugative transposons**. The
mobilome difference is compartment-specific, and the compartment the divergent clades lack is
the one through which antimicrobial-resistance determinants move in this species.

**Habitat confound, and the test that removes it.** The sensu stricto comparators are one
genome per PopPUNK cluster drawn from a collection that is 97% host-associated and largely
hospital-derived, while the divergent clades are more than half environmental. CTn carriage
is precisely what prolonged antibiotic selection in a hospital setting would produce, so the
unrestricted comparison cannot by itself distinguish lineage from habitat. The comparison was
therefore repeated using only **host-derived strains in both groups**, with host defined as
`Source Niche` in {Human, Livestock, Poultry, Companion Animal, Aquatic Animal, Wild Animal,
Animal}.

| comparison | sensu stricto | divergent | odds ratio | *p* |
|---|---|---|---|---|
| all strains | 123/236 (52.1%) | 3/176 (1.7%) | 62.8 | 8.8×10⁻³⁴ |
| **host-derived only** | **109/200 (54.5%)** | **1/66 (1.5%)** | **77.9** | **2.9×10⁻¹⁷** |

The contrast strengthens rather than weakens, so the deficit is lineage-intrinsic. DC1 alone
contributes 34 host-derived strains and one complete element.

**tet(M), quantified.** An earlier version of this document asserted that *tet*(M) "follows
the same distribution" without numbers. It does so in direction only: **7 of 236 sensu
stricto strains (3.0%) against 1 of 176 divergent strains (0.6%), odds ratio 5.35,
*p* = 0.15 — not significant**, with Cds_C5 at 2 of 19 (10.5%) and the single divergent
carrier in DC7. *tet*(M) is rare in both groups, so the CTn deficit is a deficit in the
*vehicle* and not, on this evidence, in the *cargo*. The resistance implication is a
prediction for cohort-scale resistance genotyping, not a finding here.

**Note on the source field.** Isolation-source classification throughout this work uses the
curated `Source Niche` column, not `Source_lv1`. The two disagree: `Source_lv1` buckets nine
DC2 strains as "other" that `Source Niche` classes as Environment, which would change DC2's
environmental fraction from 84.8% to 56.2%. `Source Niche` is the field the canonical
isolation-source table was built from and is authoritative here.

*Outputs:* `cdiff_mobilome_by_clade.csv`, `cdiff_mobilome_by_genome.csv`,
`cdiff_tn916_ctn_by_clade.csv`, `cdiff_tn916_ctn_by_genome.csv`,
`cdiff_tn916_host_restricted_test.csv`, `cdiff_tetM_by_clade.csv`.

## 27. Plasmid detection, and its circularity

Plasmid carriage was scored **two independent ways**, and both are reported because they
differ roughly tenfold:

1. **Marker-based** — MOB-suite replicon and relaxase detection (~6.5% carriage).
2. **Alignment breadth** — `blastn` of each assembly against a panel of closed
   cryptic-clade plasmids (`-evalue 1e-10 -perc_identity 80 -max_target_seqs 5000`),
   merging HSP intervals **on the subject (plasmid) coordinates** and scoring carriage at
   >= 50% of the plasmid length covered. Merging on subject rather than query coordinates
   is what makes this work on fragmented drafts.

**The circularity is explicit and material.** The reference panel consists of plasmids
closed from cryptic-clade isolates of clades C-III and C-IV — the same lineages as DC2 and
DC4. An alignment-breadth criterion applied to draft assemblies of those clades therefore
cannot distinguish a resident plasmid from a chromosomally integrated homologous region,
and breadth-based carriage for DC2 and DC4 is an upper bound. Alignment identities of
85-95% indicate plasmid *families* rather than shared plasmids; only one DC4 assembly
carries a near-identical match.

*Outputs:* `cdiff_plasmid_breadth_by_clade.csv`, `cdiff_plasmid_breadth_by_genome.csv`,
`cdiff_plasmid_carriage_by_genome.csv`, `cdiff_cryptic_plasmid_reference_panel.csv`.

## 28. Horizontal transfer screen

All **1,110 clade-specific families** were searched with **DIAMOND 2.1.9**
(`blastp --sensitive`) against **NCBI nr** (707,028,945 sequences). For each family the
best hit inside and outside *Clostridioides* was recorded, together with taxonomic
lineage, percent identity, query and subject coverage, bitscore, and an alienness index
(bitscore ratio of best foreign to best *Clostridioides* hit).

Families were classed as `foreign_best` (a foreign hit beats every *Clostridioides* hit),
`foreign_only`, `Clostridioides_best`, `Clostridioides_only` (no non-*Clostridioides*
homologue at all) or `no_nr_hit`.

**Two scope statements.** First, nr contains thousands of *C. difficile* genomes, so
"best hit is *Clostridioides*" partly reflects database composition; this is why the
median identity to the best *foreign* hit (67.8%) is reported as the primary evidence of
ancient divergence rather than the hit-class proportions. Second, and more importantly,
**toxin genes are by construction not clade-specific and were never in the tested set**,
so this screen's negative result does not cover them. The manuscript states this
explicitly rather than letting the negative be read broadly.

*Outputs:* `cdiff_hgt_family_table.csv`, `cdiff_hgt_clade_summary.csv`.

## 29. Compositional anomaly detection

Tetranucleotide composition and codon usage were computed per CDS and compared to the
genome mean, as an orthogonal signal of recent acquisition.

**The naive version of this analysis is badly confounded in this genus and was corrected.**
A first pass flagged **26.5% of ribosomal proteins** against 2.1% of all genes — ribosomal
proteins are the textbook negative control for horizontal transfer, so a method that flags
a quarter of them is measuring expression-related codon bias, not acquisition. Two
corrections were required and together are sufficient:

1. **Length-decile ranks** — tetranucleotide distance to the genome mean is strongly
   length-dependent, so percentile ranks were computed *within* gene-length deciles rather
   than globally.
2. **A Karlin-style control** — a gene is a candidate only if its codon usage is no closer
   to the genome's ribosomal-protein usage than to the genome mean, which removes
   highly-expressed genes from the candidate set by construction.

After both, **0 of 16,563 ribosomal protein copies are flagged** and 18,855 of 1,568,840
eligible CDS (1.20%) are candidates. Only the corrected figures are reported.

*Outputs:* `cdiff_compositional_genome_summary.csv`.

## 30. Isolation source curation and provenance

Isolation metadata were assembled from the submitted collection spreadsheet, EnteroBase
fields, NCBI BioSample attributes, PubMLST isolate records and, where those failed, the
describing publication. Sources were normalised to `host`, `environment`, `food`, `other`
and `no record`; the manuscript's "environmental" category additionally counts
`other/engineered` sources (wastewater treatment, compost, biosolids), which is why the
environmental percentage computed directly from the coarse `Source_lv1` field is lower
than the canonical value.

Several provenance traps were encountered and are recorded because they generalise:

- `NNNN_` filename prefixes are **PubMLST isolate identifiers**, not arbitrary serials;
  resolving them recovered provenance for 77 genomes.
- EnteroBase's "Country" field can hold the **sequencing centre's** country rather than
  the isolate's.
- NCBI strips BioProject submitter contacts, and a BioProject-first literature search can
  miss the describing paper entirely when publication precedes data release; searching on
  BioProject *title* text in PubMed works where the accession does not.
- Depositor attribution must be **per strain, not per clade**.

Of 22 initially untraceable genomes, 19 were resolved; `MS1`, `MC1-MC4` and `MS3` have no
recoverable origin in the public record.

*Outputs:* `cdiff_all_genomes_with_metadata.csv`, `cdiff_pubmlst_provenance_77.csv`,
`cdiff_untraceable_resolution.csv`, `cdiff_remaining_unknown_source_16.csv`.

## 31. Metagenome recruitment

**Representatives.** One representative per clade (15 total) was chosen by highest
completeness, then fewest contigs; all are >= 99.86% complete with <= 2.61%
contamination, and the Cds_C1-C4 representative is a closed single-contig genome.

**Screen.** Each representative was sketched with **sourmash 4.9.2**
(`sketch dna -p k=21,scaled=1000`) and queried against the **branchwater** index of
**1,161,119 public SRA metagenomes**. Signatures must be POSTed as a raw JSON body with
`Content-Type: application/json`; multipart form upload is rejected. The API returns
matches down to a containment floor near 0.011, far below the web interface's 0.10
default — 96.8% of returned rows fall below 0.10, which is why a threshold had to be
applied downstream rather than relied upon.

**Clade attribution.** All fifteen representatives were queried, and a run was assigned to
the clade with **maximum containment** only where that maximum reached **0.30**. Because
the clades share a core genome, 110,628 runs return a hit for all fifteen queries;
attribution therefore rests on *relative* containment and the margin to the second-best
clade is reported per run. Small-margin hits are flagged as not credible on this evidence
alone.

**Biome assignment.** ENA run metadata were retrieved via the Portal API for the 52
divergent-dominant runs, 299 sensu stricto-dominant runs and 300 background runs sampled
from containment 0.02-0.05 in the same result set. Biome was assigned by keyword over
scientific name, isolation source, host, host body site, environmental material/feature/
biome, study title, sample title and description, into gut/faecal, soil/sediment, water,
waste/manure, food, other host site, or unclassified. The background was drawn from the
same returned set as the hits, so the comparison is internally consistent regardless of
any index-level filtering.

**Detection limit.** This is the part that bounds the conclusion, and the model carries a
read-length correction that an earlier version of this document omitted. Treating *k*-mer
containment *C* as Poisson recovery at base-level coverage *x* gives `C = 1 - exp(-x)` and a
threshold coverage of 0.357×. But a *k*-mer is recovered only where **k consecutive bases**
are covered, not one, so for reads of length *L* the effective per-read recovery is reduced
by **(L − k + 1)/L = 130/150 = 0.867** at *k* = 21 and *L* = 150. The corrected model is

```
C = 1 - exp(-x · (L - k + 1) / L)
```

and the 0.30 call threshold therefore requires **0.412-fold coverage** of a 4.3 Mb genome,
about **1.77 Mbp** of target reads rather than 1.53 Mbp. Converting to the relative abundance
needed at each biome's median run depth:

| biome | median depth (Gbp) | detection floor | previous (uncorrected) |
|---|---|---|---|
| soil/sediment | 13.70 | **0.0129%** | 0.011% |
| water | 10.45 | **0.0169%** | 0.015% |
| waste/manure | 10.52 | **0.0168%** | 0.015% |
| **gut (runs yielding hits)** | 4.33 | **0.0409%** | 0.035% |

Implied abundances for detected runs were obtained by inverting the same corrected relation,
capped at containment 0.98 where it saturates; gut detections sit at an implied median
**0.094%** (IQR 0.049–0.149%). The correction moves every number by about 15% and changes no
conclusion.

**Why the read-length correction changes the floors but not the margin.** This is worth
spelling out, because it is easy — and the methods review did — to expect the margin to
tighten. Inverting the corrected model gives `x = -ln(1 - C) / f` with `f = (L-k+1)/L`, so the
factor `1/f = 1.154` multiplies **both** the threshold coverage that sets the floor **and**
every implied abundance obtained by inverting the same relation. Floors and observed
abundances therefore scale identically and the correction **cancels in their ratio**:

| | uncorrected | corrected | ratio |
|---|---|---|---|
| gut floor | 0.0354% | 0.0409% | ×1.154 |
| gut median abundance | 0.0813% | 0.0938% | ×1.154 |
| **margin** | **2.30** | **2.29** | **×1.00** |

Applying the correction to the floor while leaving the observed abundance at its uncorrected
value would give 0.081/0.0409 = 1.98 and would mix two models — an uncorrected numerator
against a corrected denominator. The margin is a property of the containment values and the
relative depths, not of *k* or *L*, and it is correction-invariant by construction. What the
correction does change is the absolute floor, which is what bounds the soil conclusion.

**The margin must be quoted against the floor of the biome the detections are in.** The gut
detections sit at a median 0.094% in runs whose own floor is 0.0409%, a margin of
**2.3-fold**. An earlier version of the manuscript described this as "sevenfold above that
floor", which divided the gut abundance by the *soil* floor (0.094/0.0129 = 7.3) and so
compared across biomes. Since the detections are in gut runs, the gut floor applies, and the
true margin is narrow: these detections sit just over a factor of two above the level at
which they would have been invisible. The corrected figure is used in the manuscript and in
Figure 5c.

**The background sampling is biased in the conservative direction, and this is worth stating
rather than calling the comparison merely "internally consistent".** The 300 background runs
were drawn from runs returning containment 0.02–0.05 in the same search — that is, runs that
already carry low-level *Clostridioides*-like *k*-mers. Since *Clostridioides* is itself a
gut-associated genus, that selection plausibly skews the background toward gut relative to
the SRA as a whole. If it does, the observed 13.3% environmental fraction **understates** the
environmental fraction of the underlying archive, the expected environmental count among the
52 divergent hits is too low, and the binomial *p* = 5.9×10⁻⁴ is an **upper bound** on the
true value. The direction of this bias therefore works against the null, not for it.

**Environmental fraction under the conservative strain definition.** The per-clade
environmental fraction was also recomputed on the 135 ANI clusters of §5, assigning a cluster
to Environment where at least half its members carry that niche. The aggregate for the nine
comparable divergent clades moves from 53.4% (79 of 148 metadata strains) to **54.1% (66 of
122 clusters)**, odds ratio 39.0 against uncollapsed sensu stricto, *p* = 5.8×10⁻⁶⁶. Per-clade
values track closely (DC2 84.4% vs 84.8%, DC1 10.0% vs 12.8%, DC3 33.3% vs 26.9%). The
collapse falls hardest on DC1 and DC3, the two least environmental divergent clades, so it
moves the aggregate slightly upward. *Output:*
`cdiff_environmental_fraction_ani_clusters.csv`.

**Interpretation rule.** The screen bounds *abundance*, not *occurrence*. A dormant spore
population in soil would plausibly sit two to three orders of magnitude below the 0.0129%
soil floor, so the absence of environmental hits cannot exclude environmental presence, and
the manuscript does not claim it does. Sequencing depth was checked and is not the limiting
factor — background soil runs are deeper (median 13.7 Gbp) than the gut runs that yielded
hits (4.3 Gbp) — but depth sets the floor and does not make a rare organism common.

*Outputs:* `cdiff_metagenome_divergent_hits.csv`, `cdiff_metagenome_biome_composition.csv`,
`cdiff_metagenome_biome_tests.csv`, `cdiff_metagenome_detection_limits.csv`,
`clade_representatives.csv`.

## 32. Clade-specific primer design

**Target selection.** Candidates were drawn from the clade-specific families and filtered
to those that are specific to a **single** clade, **single copy** per genome, **not on a
mobile element**, carried by **>= 85-90%** of clade members, and classed
`Clostridioides_only` or `no_nr_hit` in the horizontal-transfer screen — that last
criterion, no non-*Clostridioides* homologue among 707 million proteins, is what makes a
target plausible for an environmental assay.

**Sequence recovery.** Panaroo writes alignments only for core genes, so accessory
families had to be recovered from `gene_data.csv` joined to `gene_presence_absence.csv`
on `annotation_id`. Sequences were realigned per family with **MAFFT v7.526** (`--auto`).

**Nucleotide-level purity re-check.** A family passing the 90%-in / 5%-out
clade-specificity rule is **not** necessarily exclusive at nucleotide level: of 142
first-round candidates, only 51 had every recovered sequence from the target clade.
Alignments were therefore retained only where **every sequence came from the target clade**
with **mean column identity >= 0.95** and consensus length >= 300 bp.

**Design.** Primers were designed on the per-family consensus with **primer3-py 2.4.0**:
Tm 58-62 C (optimum 60), length 18-24 nt (optimum 20), GC 40-60%, max poly-X 4, no
ambiguous bases, hairpin Tm <= 24 C, self- and pair-complementarity thresholds 45/35 C,
and product size 90-200 bp for qPCR/ddPCR. Up to five pairs per target were returned.

**In-silico PCR validation.** All oligos were searched with `blastn -task blastn-short`
(BLAST+ 2.16.0, `-perc_identity 85 -evalue 1000`) against a BLAST database of **all 460
working-set genomes**, with every contig tagged by its genome. An amplicon was called
where both primers of a pair hit the **same contig**, at **>= 90% identity over
near-full-length** (alignment length >= primer length - 2), on **opposite strands**, and
**50-500 bp apart**. Per pair, target recall (fraction of target-clade genomes amplified)
and off-target count (any genome of any other clade amplified) were recorded.

**Outcome per clade, including the five clades with no validated pair.** Of 255 candidate
pairs, eight clades yielded a pair at 100% target recall with zero off-target amplification
across all 460 genomes. The five divergent clades that did not are listed here with the stage
at which each failed, since "validated pairs for eight clades" otherwise leaves the gap
unexplained.

| clade | specific families | strictly exclusive | reached nt extraction | candidate pairs | validated | outcome |
|---|---|---|---|---|---|---|
| DC1 | 97 | 25 | 19 | 30 | 4 | validated |
| DC2 | 51 | 32 | 40 | 40 | 26 | validated |
| DC3 | 20 | 15 | 4 | 5 | 3 | validated |
| DC5 | 54 | 31 | 43 | 100 | 15 | validated |
| DC8 | 22 | 3 | 6 | 5 | 5 | validated |
| DC9 | 32 | 6 | 26 | 20 | 20 | validated |
| DC10 | 93 | 63 | 24 | 10 | 5 | validated |
| DC13 | 377 | 39 | 52 | 15 | 15 | validated |
| **DC4** | 34 | 22 | 8 | 5 | **0** | no pair both complete and specific: best reaches 88% recall and amplifies 6 DC9 genomes |
| **DC6** | 18 | 10 | 6 | 10 | **0** | recall–specificity trade-off: 100%-recall pair amplifies 2 off-target genomes; best zero-off-target pair reaches 58% recall |
| **DC7** | 99 | 41 | 14 | 10 | **0** | recall–specificity trade-off: 100%-recall pair amplifies 111 off-target genomes; best zero-off-target pair reaches 60% recall |
| **DC12** | 35 | 17 | 6 | 5 | **0** | recall–specificity trade-off: 100%-recall pair amplifies 44 off-target genomes; best zero-off-target pair reaches 50% recall |
| **DC11** | 116 | 24 | 13 | **0** | **0** | 13 families reached nucleotide extraction but none produced an alignment and primer3 candidate passing the purity and amplicon criteria — no candidate pair was designed |
| Cds_C1-C4 | 10 | 3 | 7 | 0 | 0 | same failure mode as DC11; not a target of this assay |
| Cds_C5 | 52 | 27 | 15 | 0 | 0 | same failure mode as DC11; not a target of this assay |

So the five divergent clades without a validated pair fail for **two distinct reasons**: DC4,
DC6, DC7 and DC12 have candidates but no pair that is simultaneously complete and specific,
while DC11 produced no candidate at all. For DC6, DC7 and DC12 a usable assay may still be
reachable by accepting partial recall or by designing on a second target; for DC11, with one
strain and no surviving pure alignment, more genomes are the prerequisite.

**Specificity leak check (cross-reference to §9).** Because the ≤5% clade-specificity rule
permits sharing with small clades, every recommended primer target was checked against the
second-highest-clade prevalence table. **All twelve recommended targets — including all eight
validated ones — derive from strictly exclusive families with zero carriers outside the
assigned clade.** The inflation documented in §9 therefore does not reach the primer sets.

**What is not tested.** Specificity was assessed only *within Clostridioides*. There is no
check against non-*Clostridioides* soil or gut background, and no wet-lab validation —
gradient PCR, a specificity panel against related clostridia, and a limit-of-detection
curve on spiked matrix are all prerequisites to field use.

*Outputs:* `cdiff_clade_primers_recommended.csv`, `cdiff_clade_primers_all_255.csv`,
`cdiff_primer_coverage_by_clade.csv`.

---

## 33. Software and databases

| Tool | Version | Use |
|---|---|---|
| CheckM2 | 1.0.2 | assembly quality control |
| skani | 0.2.2 | average nucleotide identity |
| PopPUNK | 2.7.8 | strain-level population structure |
| GTDB-Tk | 2.4.1 (GTDB r226) | taxonomic placement |
| Prokka | 1.14.6 | uniform genome annotation |
| Panaroo | 1.5.0 | pangenome (`--clean-mode moderate`) |
| IQ-TREE | 2.3.0 | ML phylogeny, ModelFinder, UFBoot, AU test |
| Gubbins | 3.3.1 | recombination (see limitation, section 14) |
| BactDating | 1.1.4 | divergence dating |
| TreeTime | 0.12.1 | divergence dating cross-check |
| ape / phangorn | 5.8-1 / 2.12.1 | tree handling in R |
| MAFFT | v7.526 | per-gene realignment |
| HMMER | 3.4 | Pfam, KOfam, persistence and oxidative-stress panels |
| DIAMOND | 2.1.9 | nr search, MEROPS, dbCAN consensus |
| BLAST+ | 2.16.0 | plasmid breadth, in-silico PCR |
| dbCAN | 5.2.9 | carbohydrate-active enzymes |
| geNomad | 1.13.0 | prophage and plasmid prediction |
| ISEScan | 1.7.3 | insertion sequences |
| IntegronFinder | 2.0.6 | integrons |
| MOB-suite | 3.1.9 | plasmid replicon/relaxase typing |
| gRodon | 1.0.0 | growth-rate prediction |
| sourmash | 4.9.2 | metagenome sketching |
| primer3-py | 2.4.0 | primer design |

Databases: NCBI nr (707,028,945 sequences), GTDB r226, Pfam-A, KOfam (DRAM distribution),
dbCAN, MEROPS `pepunit`, branchwater SRA index (1,161,119 metagenomes).

## 34. Limitations carried into the manuscript

1. **Gubbins on a core-gene concatenate** violates its spatial-clustering assumption;
   its branch lengths are not used as substitution counts or for dating (section 14).
2. **No strict clock holds** on this tree, and total dating uncertainty is roughly
   fiftyfold; no absolute ages are reported (section 16).
3. **The horizontal-transfer screen excludes toxin genes** by construction (section 28).
4. **The plasmid reference panel comes from the clades being tested**, so breadth-based
   carriage for DC2 and DC4 is an upper bound (section 27).
5. **The metagenome screen bounds abundance, not occurrence**, with a read-length-corrected
   floor of 0.0129% in soil and 0.0409% in the gut runs; the gut detections sit only
   **2.3-fold** above their own floor (section 31).
6. **Isolation-source ascertainment cannot be corrected** from these data; the culture
   record over-represents the environment by construction.
7. **Clade sizes remain small** — nine divergent clades are comparable, four are not, and
   DC11 and DC13 rest on one strain each.
8. **Conjugative transposons are covered only by a dedicated homology search**, which
   establishes Tn916/CTn family membership and element completeness but not the identity of
   the specific element in any genome; the four general mobilome tools do not detect them at
   all (section 26).
9. **Primer specificity is untested outside *Clostridioides*** and unvalidated in vitro, and
   five of thirteen divergent clades have no validated pair (section 32).
10. **A structural-modelling phase was halted** before completion; its outputs were never
    validated and are excluded from the supplementary set.
11. **Clade-specific family counts are permissive.** The ≤5%-outside rule admits families
    shared with small clades; only 358 of 1,110 are strictly exclusive, and DC1 retains just
    26% (section 9). Per-clade counts must be quoted with the definition attached.
12. **Deduplication by metadata leaves residual pseudo-replication.** 95 within-clade pairs
    at ≥99.99% ANI were not collapsed; the conservative ANI-cluster definition reduces 176
    divergent strains to 135, and the DC3 toxin-evenness component does not survive it
    (sections 5, 18).
13. **The polarity of the haem-catalase character is threshold-dependent** — ambiguous at
    30–50% coding, absent at 70% and under polymorphic coding — so the oxidative-stress
    reframing rests on PF06397 and on the unresolvability of the ancestral state, not on a
    directional claim about haem catalase (section 20).

---

## 35. Reproducibility and data deposit

This document names roughly sixty derived output tables, which is not by itself a
reproducible record. The following are to be deposited at submission; items not yet complete
are marked.

**Code.** All analysis scripts, including the SLURM submission scripts used on the compute
cluster, in a public repository. The repository must capture the per-step job scripts and not
only the downstream analysis notebooks, because most steps here are cluster jobs with
non-trivial resource and environment specifications (conda prefixes differ between
`miniconda3/envs` and the mamba prefix `~/.local/share/mamba/envs`, and several tools are
invoked by absolute path for that reason). *Status: not yet created.*

**Archived snapshot.** A Zenodo deposit of that repository at the submission commit, with the
DOI cited in the Data Availability statement. *Status: not yet created.*

**Accession lists.**
- The 460-genome working set with accession, clade assignment, strain key and QC metrics (`cdiff_working_set_460_dedup.csv`, `cdiff_genome_qc_32957.csv`).
- The 15 clade representatives with accessions and assembly statistics (`clade_representatives.csv`).
- The four rooting outgroups (GCF_002865995.1, GCF_017873185.1, GCF_019916025.1, GCF_036812735.1).

**Clade assignments and deduplication key.**
- Clade assignment for all 30,970 *Clostridioides* genome entries (`cdiff_clade_assignments_all_genomes.csv`).
- The per-strain deduplication key with its provenance field (`cdiff_strain_keys_30970.csv`) and the ANI cross-check that bounds its completeness (`cdiff_dedup_ani_pairs_99_99.csv`).

**Primer tables.** Both the full candidate set (`cdiff_clade_primers_all_255.csv`, 255 pairs)
and the recommended set (`cdiff_clade_primers_recommended.csv`, 12 pairs), plus the per-clade
outcome table recording why five clades have no validated pair
(`cdiff_primer_coverage_by_clade.csv`).

**Alignments and trees.** The core-gene alignment, the outgroup-rooted tree
(`ml464_bac120_outgroup_rooted.treefile`), the toxin alignment and gene trees
(`cdiff_toxin_alignment.faa`, `cdiff_toxin_ML_tree.nwk`), and the AU-test output
(`cdiff_toxin_core_congruence_AUtest.csv`).

**Not deposited.** The 2.3 GB Panaroo `gene_data.csv` and the 156 MB primer BLAST hit table
exceed practical deposit size and remain on the compute cluster; the scripts that regenerate
them from the deposited assemblies are in the repository. The five tables from the halted
structural-modelling phase are excluded deliberately, as they were never validated.
