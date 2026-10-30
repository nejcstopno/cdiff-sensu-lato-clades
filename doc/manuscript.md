# Clostridioides difficile sensu lato: thirteen divergent clades with labile toxin loci and almost no conjugative transposons

**Draft manuscript, revision 5.** All frequency statistics are computed on **unique
strains** (431 in the working set; 29,455 across the collection), never on genome entries.
Comparative claims are restricted to the **eleven clades with at least six unique
strains**. Of 30,972 genomes passing quality control, two are non-*Clostridioides* and
excluded, leaving **30,970** throughout.

---

## Abstract

*Clostridioides difficile* is defined clinically by a pathogenicity locus (PaLoc) that
most of its genomic diversity does not carry, and by a set of divergent environmental
lineages whose ecology has been inferred entirely from where people have cultured them.
We assembled 30,970 quality-passed *Clostridioides* genomes — 29,455 unique strains — and
found that average nucleotide identity to the *C. difficile* 630 reference group is
discontinuous, with an empty band between 97% and 98%. Below that gap, 205 genome entries
(176 unique strains) resolve into thirteen divergent clades (DC1–DC13) at a 97% threshold
stable across 96.5–97.5%. Published archetype sequence types place DC1 = C-I, DC3 = C-II,
DC2 = C-III and DC7 = C-IIIb; nine clades have no published counterpart. Twelve map to a
single GTDB r226 genomospecies each and DC12 to none. All fourteen multi-genome clades
are strictly monophyletic on a 2,530-gene core phylogeny.

Against that strictly clade-structured core, toxin-locus content is not clade-structured.
No toxin gene reaches fixation in any divergent clade, and the canonical five-gene PaLoc
is confined to the sensu stricto clades. The informative contrast is not how many toxin
states a clade holds but how evenly it holds them: the sensu stricto group carries the
**most** states of any clade (seven) at the **lowest** evenness (0.379), 58.9% of its
strains sharing one architecture, whereas the divergent clades are genuinely even
mixtures (mean evenness 0.819 against a depth-matched null of 0.513, *p* < 10⁻⁴).
Phylogenetic discordance at the toxin loci is not demonstrable at this alignment depth:
an approximately unbiased test cannot reject the core topology for either *tcdA* or
*tcdB*.

The sharpest division between the two groups is in the mobilome, and it runs opposite to
the usual expectation. Divergent clades carry **more** prophage and **more** plasmids, but
near-complete Tn916-family conjugative transposons — the vehicle through which
antimicrobial resistance moves in this organism — are present in **123 of 236 sensu stricto
strains (52.1%) against 3 of 176 divergent strains (1.7%)** (odds ratio 62.8,
*p* = 8.8×10⁻³⁴), and absent from ten of the thirteen divergent clades. This is not a
by-product of the clinical collection's antibiotic exposure: restricted to host-derived
strains in both groups the contrast **strengthens** (54.5% against 1.5%, odds ratio 77.9,
*p* = 2.9×10⁻¹⁷), so the deficit tracks lineage and not habitat.

A second comparison constrains how the two groups differ in anaerobic oxidative-stress
chemistry without resolving its direction. The desulfoferrodoxin C-terminal domain PF06397
— the one marker whose reconstruction is stable under every coding threshold we tested — is
present in two of the four outgroup genomes, as is haem catalase, which is absent from all
255 sensu stricto strains. **The ancestral state cannot be resolved from these data**,
which is enough to retire the claim that these systems were acquired in the divergent
clades, but not enough to assert reduction in the clinical lineage. And the two available
lines of ecological evidence contradict each other.
The culture record places these clades overwhelmingly in the environment — 53.4% of
isolates with a recorded source across the nine comparable clades, against 2.9% for sensu
stricto — while recruitment of
clade representatives against 1,161,119 public metagenomes detects them in 49 gut runs and
in no soil, water or waste run. Neither observation settles their distribution, because
the two methods do not overlap in sensitivity: shotgun metagenomes at these depths reach a
floor near 0.013% relative abundance in soil and 0.041% in the shallower gut runs, roughly
two to three orders of magnitude above where a dormant spore population would sit, while
enrichment culture detects presence without quantifying it. We therefore make no claim about preferred habitat, and instead report the
discrepancy and supply the instrument that can resolve it: clade-specific primer sets for
eight of the thirteen clades, validated in silico against 460 genomes spanning all
fifteen.

---

## Introduction

*C. difficile* is the leading cause of antibiotic-associated diarrhoea, and its taxonomy
has been built around clinical isolates and the PaLoc. Cryptic clades C-I to C-III,
recovered mainly from soil and water, were argued to be genomically distinct enough to
constitute separate genomospecies; later surveys added C-IV and C-V together with a
binary-toxin locus on a plasmid, and a 2025 preprint added C-VI and C-VII and split
C-III. Whether these lineages are separate species or ancient within-species lineages
remains disputed between those groups.

Two framings of the PaLoc also coexist. The locus occupies a single conserved chromosomal
integration site and carries clade-specific variants, which suggests stability; yet it
varies in presence among close relatives and transfers experimentally, which suggests
mobility. Within sensu stricto this is reconciled by rare mobilisation at that one site,
and *tcdB* is known to have diversified by intragenic recombination while *tcdA* shows no
such signal. Whether the same holds across the deeper divergences separating the cryptic
clades has not been tested at scale.

A third problem has gone untested altogether. Every statement about cryptic-clade ecology
rests on isolation records from culture surveys, and those surveys were deliberately
environmental. No culture-independent estimate of where these organisms occur has been
published.

We address three questions. Where the species boundaries fall when the full genome set is
used rather than a reference panel. How toxin-locus content is distributed across the
resulting clades. And whether independent data support the environmental lifestyle that
the isolation records imply.

---

## Results

### A discontinuous species boundary, and fifteen clades

Average nucleotide identity of all 30,972 quality-passed genomes against the six-genome
630 reference group, taken as the maximum over the six, is bimodal with an **empty 97–98%
band**: 21,806 genomes at 99–100%, 6,183 at 98–99%, **zero** between 97% and 98%, 2,717 at
96–96.5%, and 205 divergent entries spread between 88.8% and 95.8%.

Taking the maximum is the choice that works hardest against this result. The best of six
references is at least as high as any single one, so it inflates every genome's identity,
pulls genomes *toward* sensu stricto, and tends to fill the gap rather than open it; the
mean, the median or any individual reference can only widen it.

The 96–97% block is not a continuum with sensu stricto. It is clade C5, the RT078/ST11
lineage: 2,760 of its 2,775 genomes carry a published clade-5 sequence type and 2,677 are
ST11/RT078. Two genomes widely used as *C. difficile* references, TW11 and 12038, are
99.92% identical to each other but only 96.15–96.39% to 630; including them in a reference
panel lifts 2,798 C5 genomes above a 98% cutoff and closes the gap artificially.

Below the gap, average-linkage clustering of the 205 divergent entries returns thirteen
clades, stable across thresholds 96.5–97.5% — a 1.0-point plateau — with the cutoff taken
at 97%. Two independent derivations agree: a complete all-versus-all on the 205, and 230
greedy representatives covering all 30,972 genomes return the identical partition. Four
of seventeen groups reported by a previous in-house analysis were artefacts.

**Concordance with published nomenclature.** Each published archetype sequence type falls
in exactly one of our clades: ST181 in DC1 (C-I), ST200 in DC3 (C-II), ST369 in DC2
(C-III), and ST919 — strain TUM20227, assigned C-IIIb in a recent reanalysis — in DC7.
DC2's median ANI of 89.27% to the 630 group independently matches the published C-III
range of 89.2–89.4%. The C-IIIa/C-IIIb assignment carries a further internal check, because
the preprint that erected it separated the two subclades at 95.2% ANI: if ST369 → DC2 and
ST919 → DC7 both hold, DC2 and DC7 must be approximately 95% identical to each other. Our
all-versus-all matrix gives a **median DC2 ↔ DC7 ANI of 96.10% (range 95.42–96.45%, 490
genome pairs)** — the two are each other's nearest neighbours among the divergent clades,
and the value sits just above the published C-IIIa/C-IIIb separation rather than near the
≈89% that would be expected if the C-IIIb assignment were misplaced. The mapping is
therefore consistent with our data, not merely imported from it. The remaining nine clades have no counterpart we could anchor,
because no archetype sequence type or accession has been designated for C-IV, C-V, C-VI
or C-VII; establishing those anchors is a prerequisite for any further reconciliation.
Twelve of thirteen clades correspond to exactly one GTDB r226 genomospecies and the
partition is finer than GTDB: *difficile_F* splits into four clades and sp020641055 into
two. **DC12 carries no GTDB species assignment.**

ANI alone cannot subdivide sensu stricto — the largest cluster still holds 27,989 genomes
at 98% linkage. PopPUNK resolves it into 255 strain clusters over 30,757 genomes, and
**none of the 70 clade-typed clusters spans more than one published clade**.

![Figure 1]({{artifact:9df841c6-8885-4646-b508-f6f85cb67c81}})

**Figure 1. The species boundary is discontinuous and resolves into thirteen divergent
clades.** ANI to the 630 reference group across all quality-passed genomes with the empty
97–98% band marked; clade C5 occupying the 96–97% block; and the threshold scan showing
the plateau over which the partition is invariant. *n* = 30,972 genomes for the ANI
distribution, 205 entries for the partition.

### Phylogeny, rooting and the limits of dating

A core-genome maximum-likelihood phylogeny (2,530 genes, 2.54 Mb, 460 taxa) recovers
**all fourteen multi-genome clades as strictly monophyletic with zero foreign tips and
SH-like support of 1.00 at every clade ancestor**. Four outgroups spanning three genera
(*Paraclostridium sordellii*, *Metaclostridioides mangenotii*, *P. bifermentans*,
*Terrisporobacter glycolicus*) give a monophyletic ingroup at 100% ultrafast bootstrap in
two independent marker sets, and place the root on a single branch separating 103 genomes
(DC2, DC4, DC5, DC7, DC8, DC9) from 357. The 357 resolve further into 291 (Cds_C1-C4,
Cds_C5, DC3, DC10, DC13) and 66 (DC1, DC6, DC11, DC12). All three blocks are
monophyletic and are referred to below.

We attempted to date the splits and **report no absolute ages**. The core alignment is
not substitution-saturated — the uncorrected-versus-corrected distance relationship is
near-linear (R² 0.986–0.999 over 399 pairs), the entropy saturation index is 0.026–0.078
against 1.0 for saturated data, and only 2.9% of sites carry three or more states. A
strict clock nonetheless does not hold: depth-based and height-based clock-free orderings
of the fifteen clades are unrelated (Spearman ρ = −0.356, *n* = 15, *p* = 0.19) where a
clock demands +1. And the choice among defensible branch-length estimators of one topology
spans ninefold, which with the sixfold published clock range gives roughly fiftyfold total
uncertainty. Within those limits our estimates are consistent with the literature and
published point estimates fall inside six of eight brackets tested.

Two methodological notes for the record. The published "95% credible intervals" are
arithmetically **rate brackets**: at all four published nodes the lower bound times
1.5×10⁻⁸ equals the upper bound times 2.5×10⁻⁹ to within 0.8%. And both clock rates
originate as a long-term **synonymous** clock, two orders of magnitude slower than the
short-term transmission clock of ~3.2×10⁻⁷ substitutions/site/year; we apply them only in
that sense and note that spore dormancy makes the clock non-linear over these depths.

![Figure 2]({{artifact:2c43a9e8-48d9-46cd-868e-a378dc84df81}})

**Figure 2. Outgroup-rooted phylogeny and the bounds on divergence dating.** Left: dated
phylogeny of the fifteen clades on a 1,455-gene codon-aware core, rooted with four
outgroups across three genera; node positions at the slow clock, bars reaching the fast
clock. Right: age brackets for the two datable nodes under four branch-length estimators
of the same topology, against the published values. *n* = 460 ingroup genomes plus 4
outgroups.

### Clade-specific gene content

The pangenome holds 16,101 gene families across the 460-genome working set (2,270 core,
322 soft core, 2,079 shell, 11,430 cloud). Because that set contains 29 redundant entries,
clade-specific calls were **re-derived on the 431 unique strains**; the pangenome itself
was not recomputed, since removing columns cannot create or merge families, but prevalence
within a clade can be inflated when the same strain is counted twice.

Specificity is presence in at least 90% of clade members and at most 5% outside, rarefied
to six strains with 50 resamples. **Every comparable divergent clade carries more
clade-specific families than sensu stricto** (13): DC10 94, DC1 91, DC5 63, DC2 59, C5 54,
DC7 49, DC6 39, DC4 36, DC8 26, DC3 22. DC5 falls from 96 families to 63 on deduplication
because three of its nine strains were each present twice; no other clade moves by more
than four. DC9, at five unique strains, falls below the comparability threshold.

**These counts are permissive, and in one clade substantially so.** The ≤5%-outside rule is
evaluated across all 431 strains, so a family fixed in a large clade and also fixed in a
small one still passes: a family present in 100% of DC1 and 100% of DC11 (one strain) sits
at 0.2% outside and is counted as DC1-specific. Requiring *zero* carriers outside the
assigned clade reduces 1,110 families to **358 strictly exclusive ones**, and the loss is
very unevenly distributed (Table S30). DC10 (68% strictly exclusive), DC3 (75%), DC4 (65%)
and DC2 (63%) are little affected, whereas **DC1 retains only 26%**: for the median
DC1-assigned family there is another clade — most often its sister DC6 (38 families) or
DC11 (17) — in which the family is also at 100% prevalence. DC8 (14%) and DC13 (10%) are
affected similarly. The permissive counts therefore measure *lineage-block* rather than
strictly clade-private content, and the comparative ranking above should be read with the
strictly exclusive column alongside it. The conclusion that every comparable divergent clade
exceeds sensu stricto survives both definitions; the specific family counts do not transfer
between them. Primer design is unaffected, because it drew only on single-clade families
and every recommended pair derives from a strictly exclusive one.

Of 1,110 clade-specific families, Prokka named 205, KOfam assigned 206 KEGG orthologues,
Pfam-A matched 579, dbCAN 38 carbohydrate-active enzymes and MEROPS 32 peptidases; the
union is 595, leaving **515 families (47%) completely dark**. The only clade-exclusive
KEGG module is M00986, sulfur reduction, present in 49 of 50 DC1 genomes and 0 of 410
others; it rests on a single orthologue (K18367) and we make no phenotypic claim from it.

Two clades are informative opposites. **DC3 carries a genome-degradation signature** — the
highest insertion-sequence load of the eleven comparable clades (median 87.5 copies against
21.0 for sensu stricto) together with the slowest predicted growth (2.26 h). Its
compositional-anomaly load is unremarkable (median 39 candidates per strain against 43 for
sensu stricto), so the signature is mobile-element proliferation rather than aberrant
sequence composition. **DC10 is its mirror**: the fewest complete KEGG modules of any
comparable clade, yet the highest glycoside hydrolase content (55.2) and the most
clade-specific families (94).

![Figure 3]({{artifact:9be02b95-fd57-4b99-bb3f-e2acd256a55a}})

**Figure 3. Clade-specific gene content on unique strains.** Clade-specific families per
clade, rarefied to six strains with 50 resamples. Bars are the deduplicated (431-strain)
values; open circles the values before deduplication, showing that only DC5 changes
materially. Clades with fewer than six unique strains are excluded. Sensu stricto
reference 13 families.

### Toxin-locus content is evenly polymorphic in divergent clades and near-monomorphic in sensu stricto

We inventoried the large clostridial toxins and binary toxin at protein level across all
460 genomes by homology search rather than annotation name, with reference lengths and
contig-edge status recorded per homologue, then reduced to 431 unique strains.

**The canonical five-gene PaLoc (*tcdR*–*tcdB*–*tcdE*–*tcdA*–*tcdC*) is confined to the
sensu stricto clades** — present at full length in 77 strains and at any status in 148
Cds_C1-C4 strains, plus two Cds_C5 strains at partial status, and in **none of the 205
divergent entries** under either definition. **No toxin gene reaches fixation in any
divergent clade**; the highest prevalence observed is *cdtR* at 92% in DC6.

That within-clade variation is not new in kind. It is established for sensu stricto, six
independent non-toxigenic lineages have been described there, and non-canonical
arrangements have been reported across C-I to C-V. What has not been done is to quantify
it at matched sampling depth, and doing so inverts the expected contrast.

Counting states is the wrong instrument, because state richness is dominated by singletons
and a clade that is half non-toxigenic scores high for the wrong reason. **Evenness is the
appropriate measure, and on it the sensu stricto group is the outlier**: it holds the most
toxin-positive states of any clade in the study (seven) at the lowest evenness (0.379),
with 58.9% of its strains sharing a single architecture and the other six states rare
variants. All eight divergent clades with two or more toxin-positive states exceed it.
Subsampling the sensu stricto toxin-positive strains to each clade's depth (10,000 draws)
makes DC2 (*p* = 0.007), DC6 (*p* = 0.0067) and DC3 (*p* = 0.024) individually
significant, with DC8 marginal (*p* = 0.097) and the clades of five to six strains
underpowered. Across all eight, the observed mean evenness of 0.819 exceeds a
depth-matched null of 0.513 (95% range 0.309–0.695) in **0 of 10,000 draws**
(*p* < 10⁻⁴); Stouffer combination of the per-clade tests gives *p* = 3×10⁻⁵. Sensu
stricto is a near-monomorphic clade with a tail of rare variants; the divergent clades are
even mixtures.

**Per-clade *p*-values are reported uncorrected and inference rests on the aggregate test.**
Under Benjamini–Hochberg control across the family of eight per-clade comparisons, DC6 and
DC2 remain significant (*q* = 0.028 each) while DC3 becomes marginal (*q* = 0.063) and DC8
does not survive; the aggregate permutation test, which is a single test, is unaffected.

**The result also survives a stricter definition of a strain than our metadata key
provides.** Cross-checking deduplication against the all-versus-all matrix found 95
within-clade genome pairs at ≥99.99% ANI that the metadata key did not collapse — some are
plainly the same isolate reaching the archives by two routes (an EnteroBase assembly and
the underlying read accession), others are genuinely distinct isolates from one clonal
sampling series, and ANI alone cannot separate the two. Both, however, are
pseudo-replication for our purposes. Collapsing every divergent clade at 99.99% ANI reduces
176 metadata strains to **135 clusters**, hitting DC1 (45 → 30), DC3 (26 → 21), DC5 (9 → 4)
and DC9 (5 → 2) hardest. Re-running the whole analysis on those clusters — and leaving sensu
stricto uncollapsed, which makes the comparison conservative in the unfavourable direction —
gives an observed mean evenness of 0.796 against a depth-matched null of 0.662, exceeded in
26 of 10,000 draws (*p* = 0.0027). Per clade, DC6 strengthens (*p* = 0.005) and DC2 holds
(*p* = 0.028), while DC3 loses significance (*p* = 0.137) and DC5 and DC9 fall below the
minimum depth entirely. The headline result is robust to the strain definition; the DC3
component is not, and we do not rely on it.

Two polymorphisms are discrete enough to read as states rather than assembly noise.
**DC10 splits four-to-two into mutually exclusive configurations** — four strains carry
*tcdA* plus *tcdR* and no binary-toxin gene, two carry full-length *cdtB* with a partial
*cdtA* and no *tcd* gene at all — and no DC10 strain carries both. **DC3 holds a
*tcdA*–*tcdR* module in eight of 26 strains and a separate *cdtR*–*tcdR*–*tcdB*–*tcdE*
locus in seven**, so DC3 retains full-length *tcdB* at a median 92.4% identity to
reference TcdB, the highest of any divergent clade.

DC1 and DC6 carry a **fused binary-toxin and *tcd* locus**
(*cdtB*-*cdtA*-*cdtR*-*tcdR*-*tcdB*-*tcdE*) as one contiguous ~14 kb block with no
intervening coding sequence. **This claim rests on eight assemblies and we state the count
explicitly.** Three of 45 DC1 strains and seven of 12 DC6 strains carry all six genes at
all; among those, the six are contiguous on a single contig in **3 of 3 DC1 strains and 5 of
7 DC6 strains** (the two DC6 exceptions break at four genes, consistent with an assembly
gap rather than a different architecture). Seven of the eight contiguous instances are
internal to their contig with at least 1 kb of flanking sequence on both sides — the minimum
flank is 9.1 kb in DC1 and 710 bp in the single edge-proximal DC6 case — and the block
spans 13,988–13,993 bp in every instance. Collapsing near-identical genomes leaves two
independent DC1 and four independent DC6 observations. The architecture therefore
characterises a *minority* of DC1 (three strains) and about half of DC6, not the clades as
wholes. The closest published observation is a full CdtLoc immediately upstream of a
monotoxin PaLoc in a C-III sequence type, described as colocated and syntenic without
enumerating this six-gene contiguous order. **We flag this as the claim in this manuscript
most in need of long-read validation**, since a contig join is exactly the artefact a
short-read assembly would produce, and six of our eight instances come from two study
series rather than from independent isolates. DC2, DC4 and DC8 carry
a compact CDT-only locus of ~5.1–5.2 kb; DC7 and DC13 a pseudogenised *tcdA* — in DC13 at
100% nucleotide coverage and 84.3% amino-acid identity but with a longest open reading
frame of 191 residues; and **DC5 carries no toxin gene at all across its nine strains**
apart from a single full-length *tcdC* homologue at 86.6% identity in one.

Divergent TcdB homologues are 82–92% identical to reference TcdB over their whole length,
so gene-family fragmentation in the pangenome reflects genomic context rather than
sequence divergence. The most divergent single domain in the dataset is the DC7 TcdB
glucosyltransferase domain at 69.8% identity. That protein, from strain TUM20227, has been
described independently as a deeply divergent TcdB falling outside the established B1–B12
subtype framework; our contribution is to place it in a thirteen-clade context and to show
that its clade is itself toxin-polymorphic, not to report its divergence.

![Figure 4]({{artifact:a4235f20-1991-4bea-ad20-106e20145b4e}})

**Figure 4. Toxin-locus content is polymorphic within every clade.** (a) Prevalence of
each of the eight toxin genes per clade as a percentage of unique strains. (b) Composition
of each clade by toxin-gene state, grouped into seven interpretable classes; the number of
distinct raw states and the strain count are given at right. (c) Distinct toxin-locus
states per six strains, rarefied with 2,000 draws, bars giving the 2.5–97.5 percentile
range; the dashed line is the sensu stricto reference. All panels use the 431 unique
strains and the eleven clades with at least six strains. The fused
*cdtB*-*cdtA*-*cdtR*-*tcdR*-*tcdB*-*tcdE* block referred to in the text is carried on a
single contig by **8 assemblies — 3 of 45 DC1 strains and 5 of 12 DC6 strains** — of which 7
are internal to their contig with at least 1 kb of flanking sequence on both sides; the
block spans 13,988–13,993 bp in every instance and the architecture therefore describes a
minority of DC1 rather than the clade as a whole.

### Phylogenetic discordance is not demonstrable at this alignment depth

In a protein tree the toxin sequences appear to interleave across the clade boundary:
sensu stricto TcdB occupies three separate positions, Cds_C5 two, and DC6 two distinct
lineages. **This apparent discordance does not survive a formal test and we do not claim
it.** Testing each gene's own maximum-likelihood tree against that gene's alignment
constrained to the core-genome topology, an approximately unbiased test (10,000
resamplings) **cannot reject the core topology for either gene**: *tcdA* ΔlogL 4.99,
*p*-AU 0.379; *tcdB* ΔlogL 60.65, *p*-AU 0.157. Both constrained topologies fall inside
the 95% confidence set, and half the internal nodes of the *tcdB* gene tree are below 95%
ultrafast bootstrap, which is the likely explanation.

The direction is consistent across independent measures. *tcdB* departs from the core
topology about twice as far as *tcdA* (normalised Robinson–Foulds 0.300 against 0.185),
and within-subtree exclusivity fails for four of seven multi-strain groups for *tcdB*
against one of four for *tcdA*. This reproduces, at sensu lato scale and by a different
method, the established finding that *tcdB* diversified by extensive intragenic
recombination while *tcdA* carries no such signal. We report it as **independent
confirmation of greater *tcdB* lability**, not as a new result, and we do not infer
transfer from it.

We also record the scope of our horizontal-transfer screen, because it reads more broadly
than it is. That screen searched the **1,110 clade-specific gene families** against a
707-million-sequence protein database: only 19 have a foreign best hit, 735 a
*Clostridioides* best hit, 298 no non-*Clostridioides* homologue at all, and median
identity to the best foreign hit is 67.8%, indicating ancient divergence rather than
recent transfer. Toxin genes are by construction not clade-specific and were therefore
**never in the tested set**. The screen's negative does not cover them.

### The oxidative-stress system is reduced in the clinical lineage, not gained in the divergent clades

Of 41 detected sporulation, germination and stress domains, 23 are copy-number identical
across all 460 genomes, including Spo0A, SpoIIE, SpoIID, SpoIIIA, SpoVAD, dipicolinate
synthase and the small acid-soluble proteins. Persistence machinery is not elaborated in
the divergent clades. The one system that differs is oxidative-stress chemistry, and its
structure follows the tree.

Haem catalase is absent from every one of the 255 sensu stricto strains and present in
DC9 (100%), DC11 (100%), DC5 (88.9%), DC7 (55.6%), DC8 (42.9%), DC6 (25.0%) and DC1
(2.2%). The desulfoferrodoxin C-terminal domain PF06397 is **strictly bimodal across all
fifteen clades** — its prevalence takes only the values 0, 94.7, 98.7 or 100%, with
nothing in between — while the N-terminal domain PF01880 remains at exactly one copy in
every strain in the study, so the difference is domain truncation rather than gene loss.
Mn-catalase copy number falls from 3.99–4.17 in Cds_C1-C4, Cds_C5, DC3, DC10 and DC13 to
1.00–3.33 in the remaining clades, and rubrerythrin rises in the same clades that lose it
(DC2 and DC5 at 5.00 copies against 3.88 for sensu stricto).

**The direction of change is the opposite of what the ingroup alone suggests.** We
annotated the four rooting outgroups for the same domains. Haem catalase is present in two of the four outgroup **genomes**
(*P. bifermentans*, *T. glycolicus*) and PF06397 in two (*M. mangenotii*, *T. glycolicus*).
The four genomes span **three genera**, because *Paraclostridium* contributes two of them,
so these are two-of-four genomes and not two-of-four genera. Haem catalase is therefore **not a novel acquisition
of the divergent clades**; loss in the lineage leading to sensu stricto is at least as
parsimonious an explanation. Fitch parsimony on the fifteen clades plus four outgroups
requires four state changes for PF06397 and six for haem catalase, and leaves the
ancestral state of both ambiguous — the outgroups are split two-to-two on each. We do not
reconstruct Mn-catalase copy number, because the outgroup counts come from a different
annotation pipeline and copy numbers are not comparable across pipelines.

**The two characters are not equally robust to how clades are coded, and we report the
difference rather than the more convenient of the two.** Coding a clade as present by
majority rule puts DC7 (55.6%) on one side of the 50% line and DC8 (42.9%) on the other, a
13-point difference deciding a character state. Re-running the reconstruction at 30%, 50%
and 70% thresholds and with polymorphic clades coded as ambiguous (Table S31) leaves
**PF06397 completely unaffected** — four changes and an ambiguous ancestral state under
every coding, which follows from its strict bimodality. Haem catalase is not so stable:
it requires five to six changes across codings, and while the ancestral state is ambiguous
at the 30% and 50% thresholds, it resolves to **absent at the 70% threshold and under
polymorphic coding**, under which presence in DC5, DC9 and DC11 reads as gain rather than
ancestral retention. The polarity of the haem-catalase character is therefore
threshold-dependent and we do not rest the reframing on it. What survives every coding is
the weaker but sufficient statement: the ancestral state cannot be resolved from these
data, so presence in the divergent clades cannot be called an acquisition — which is all
that is needed to retire the acquisition framing. PF06397, the character that is stable,
carries the reconstruction.

Nor do the three markers partition the clades cleanly. DC9 carries PF06397 at 100%
alongside haem catalase at 100% and a single Mn-catalase copy, and sits sister to DC8
inside the early-diverging group — a combination belonging to neither of the two regimes
the other clades suggest. The defensible description is a reduced and partially
substituted oxidative-stress apparatus in the lineage leading to clinical *C. difficile*,
with at least one further rearrangement inside the early-diverging clades, rather than a
clean two-state character.

### Conjugative transposons are near-absent from the divergent clades, and that tracks lineage rather than habitat

Tn916-family conjugative transposons (CTns) are the principal accessory-gene vehicle in
*C. difficile* and the compartment through which antimicrobial-resistance determinants move
in this species. They are detected by none of the four general mobilome tools we ran, so we
searched the 24 Tn916 coding sequences (GenBank U09422.1) against all 460 proteomes with
`blastp` and scored an element as **complete** where a genome carries a Tn916-family
integrase, the excisionase, and at least four of the six conjugation-module genes.

**Complete elements are present in 123 of 236 sensu stricto strains (52.1%) against 3 of 176
divergent strains (1.7%)** — Fisher odds ratio 62.8, *p* = 8.8×10⁻³⁴ — and are entirely
absent from ten of the thirteen divergent clades, the exceptions being single strains in
DC1, DC2 and DC7.

**This is not a detection-sensitivity artefact.** Tn916-family integrase hits match at the
same identity in both groups — median 62.5% in divergent clades against 64.3% in sensu
stricto — and 47 of 205 divergent genomes carry at least one conjugation-module gene. What
the divergent genomes lack is the co-occurring complete module, not detectable homology. Had
the threshold been excluding diverged copies, divergent-clade identities would sit
systematically lower; they do not.

**Nor is it a by-product of the clinical collection's antibiotic exposure, which is the
obvious confound.** The sensu stricto comparators are one genome per PopPUNK cluster from a
collection that is 97% host-associated and largely hospital-derived, while the divergent
clades are more than half environmental — and CTn carriage is exactly what decades of
antibiotic selection in a hospital would produce. We therefore repeated the comparison using
only host-derived strains in both groups. The contrast does not weaken; it **strengthens**,
to **109 of 200 host-derived sensu stricto strains (54.5%) against 1 of 66 host-derived
divergent strains (1.5%)** — odds ratio 77.9, *p* = 2.9×10⁻¹⁷. DC1, which is 87%
host-associated and the largest divergent clade, contributes 34 host-derived strains and one
complete element. **The deficit tracks lineage, not habitat.**

**One qualification, because the resistance implication does not follow automatically.**
*tet*(M), the resistance determinant Tn916 classically carries, is rare in both groups: 7 of
236 sensu stricto strains (3.0%) against 1 of 176 divergent strains (0.6%), which is the same
direction but **not significant** (odds ratio 5.35, *p* = 0.15), and the single divergent
carrier is in DC7. Cds_C5 carries 2 of 19 (10.5%). So the divergent clades lack the
*vehicle*, not demonstrably the *cargo*; what our data support is a deficit in conjugative
machinery, with the resistance consequence a prediction that cohort-scale resistance
genotyping would have to test.

Mobile-element content otherwise runs the other way: prophage occupies a median 6.4% of
divergent genomes against 3.7% of sensu stricto (*p* = 1.1×10⁻²⁹), all nine comparable
divergent clades exceed the Cds_C1-C4 median of 3.67%, and plasmid-bearing strains are more
frequent (56.3% against 39.6%). **The mobilome difference is therefore compartment-specific
rather than a uniform excess**, and the compartment the divergent clades lack is the
conjugative one.

### Culture and metagenome evidence disagree, and neither settles the question

On unique strains with a recorded source niche, **53.4% of isolates from the nine
comparable divergent clades are environmental (79 of 148) against 2.9% of sensu stricto
(683 of 23,309)** — Fisher odds ratio 37.9, *p* = 1.0×10⁻⁷⁷.
**That fraction is robust to the conservative strain definition.** Re-running it on the 135
ANI clusters (§Methods), which collapse DC1 from 45 strains to 30 and DC3 from 26 to 21 —
the two least environmental divergent clades — moves the figure slightly **up**, to
**54.1% (66 of 122)**, odds ratio 39.0, *p* = 5.8×10⁻⁶⁶, with per-clade values tracking the
metadata-strain ones closely (DC2 84.4% against 84.8%, DC1 10.0% against 12.8%). The same
strain definition that costs the DC3 toxin-evenness component leaves the ecological
contrast intact. Including the four clades
below the six-strain threshold changes nothing material (84 of 158, 53.2%, odds ratio 37.6,
*p* = 3.2×10⁻⁸²), because three of those four clades contribute a single strain each; we
quote the restricted figure throughout for consistency with every other comparative
statement. Six of the nine comparable divergent clades are at least 50% environmental, and
three (DC4, DC5, DC10) are exclusively so. This is the entire
evidential basis for the cryptic clades being described as environmental organisms.

We tested it against culture-independent data and obtained the opposite answer. One
best-quality representative per clade (all ≥99.9% complete) was sketched and queried
against an index of 1,161,119 public SRA metagenomes; 306,095 runs returned non-zero
containment. Of 5,088 runs in which some clade genome is at least 30% contained, sensu
stricto dominates 4,960 and **divergent clades only 52**. Retrieving ENA metadata for
those 52 plus 299 sensu stricto-dominant and 300 background runs, **49 of the 52 divergent
hits are gut or faecal, three are unclassified, and none is soil, sediment, water or
waste**, against 13.3% such biomes in the background (binomial *p* = 5.9×10⁻⁴). Sensu
stricto behaves identically among the runs sampled (1 of 299 environmental, expected 39.9)
and the gut fraction does not differ between the two groups (Fisher *p* = 0.47). **That
background is itself biased in the conservative direction.** The 300 background runs were
drawn from runs returning containment between 0.02 and 0.05 in the same search — that is,
runs already carrying low-level *Clostridioides*-like *k*-mers, which plausibly skews the
background toward gut relative to the SRA as a whole. If so, 13.3% *understates* the
environmental fraction of the underlying archive, the expected environmental count is too
low, and the binomial *p*-value is an upper bound on the true one. Clades
that are 100% environmental by culture — DC4, DC5 and DC10 — contribute three gut runs and
no environmental run between them.

**The disagreement is a property of the methods, not of the organisms, and we resolve it
no further than that.** The two approaches do not overlap in sensitivity. A *k*-mer of
length 21 is recovered only where 21 consecutive bases are covered, so for 150 bp reads the
effective recovery factor is (L − k + 1)/L = 0.867; reaching the 0.30 containment threshold
for a 4.3 Mb genome therefore requires approximately 0.41-fold coverage, about 1.8 Mbp of
target reads. At the median depth of the background runs this is a floor of **0.013%
relative abundance in soil and sediment**, 0.017% in water and waste, and **0.041% in the
gut runs**, which are shallower (median 4.3 Gbp against 13.7 Gbp for soil). The clades were
detected in guts at an implied median abundance of 0.094% (interquartile range
0.049–0.149%) — **2.3-fold above the gut floor that applies to those runs**, a narrow
margin, and one we state against the correct biome rather than against the deeper soil
floor. A dormant spore population in soil would plausibly sit two to three orders of
magnitude *below* the soil floor. Enrichment culture, conversely,
recovers an organism from a gram of soil without saying what fraction of the community it
represented. Shotgun metagenomics at these depths measures abundance and is blind to
presence; selective culture detects presence and says nothing about abundance.

We therefore make **no claim about the preferred habitat of these clades**. What the
combined evidence does bear on is environmental *growth* rather than presence: an organism
replicating in soil should at some point constitute a measurable fraction of some soil
community, and across 300 background runs none of these clades does. That is consistent
with the flat predicted growth rates, the absence of plant-polysaccharide machinery and the
narrower carbon breadth reported above, and with persistence as spores rather than
vegetative growth — but it is an argument about population dynamics, not about
distribution.

Resolving distribution needs an assay matched to the expected density. We therefore
designed clade-specific primer sets from the clade-specific gene families, restricted to
single-copy, non-mobile families with no non-*Clostridioides* homologue in a
707-million-sequence protein database. Of 255 candidate pairs tested by in-silico PCR
against all 460 working-set genomes, **eight clades have a pair amplifying every strain of
the target clade and no genome of any other clade** (DC1 50/50, DC2 49/49, DC3 29/29, DC5
12/12, DC8 8/8, DC9 7/7, DC10 6/6, DC13 1/1). **Five divergent clades have no validated
pair, for two distinct reasons** (Table S32). For DC6, DC7 and DC12 the failure is a
recall–specificity trade-off rather than an absence of candidates: pairs reaching 100%
target recall exist in each, but amplify 2, 111 and 44 off-target genomes respectively,
while the best pair with zero off-target amplification reaches only 58%, 60% and 50%
recall. DC4's single pure target yields no pair that is both complete and specific — the
best reaches 88% recall and amplifies six DC9 genomes. DC11 is a different failure: thirteen
of its families reached nucleotide extraction, but none produced an alignment and primer3
candidate passing the purity and amplicon criteria, so no candidate pair was designed at
all. The same applies to both sensu stricto groups, which are not targets here. These assays
operate orders of magnitude below the shotgun floor and are the appropriate instrument for
testing whether the divergent clades are genuinely resident in soil at spore-level density. Specificity has not
yet been tested against non-*Clostridioides* environmental background, and no wet-lab
validation has been performed; both are prerequisites to field use.

Candidate explanations for an environmental lifestyle fail independently of this.
**Plant association is refuted**: of 47 diagnostic plant-cell-wall enzyme families, 36
score exactly zero in all 460 genomes under both a strict two-tool consensus and a
permissive HMM-only caller — every cellulase, xylanase, pectinase and pectate lyase, and
all ten plant-glycan carbohydrate-binding modules. Polysaccharide lyases total one protein
in one genome and no cellulosome is present. Glycoside hydrolase content is in fact *lower*
in seven of the nine comparable divergent clades (the exceptions are DC3 at 44.4 and DC10
at 55.2, against 41.1 for sensu stricto), and the deficit lies in intracellular
sugar-phosphate families rather than extracellular ones. **Growth rate is flat**:
codon-usage prediction gives clade means from 1.64 h (DC6) to 2.26 h (DC3) against 1.85 h
for sensu stricto.

Mobile-element content differs across every comparable divergent clade, in both directions;
it is treated in its own section above.

**No measured variable correlates with environmental fraction.** Across the nine comparable
divergent clades, doubling time gives ρ = +0.36 (*p* = 0.35), genome size ρ = −0.37,
glycoside hydrolases ρ = −0.17, haem catalase ρ = −0.13, plasmid content ρ = −0.20,
prophage ρ = −0.17 and insertion sequences ρ = −0.15, all *p* ≥ 0.33. Computed across all
eleven comparable clades the doubling-time association is ρ = −0.04 (*p* = 0.92); we report
both because the choice of population changes the sign without changing the conclusion.

![Figure 5]({{artifact:7c9310cb-a805-4041-8d4d-ff1fb20b53e1}})

**Figure 5. Culture and metagenome evidence disagree, and the methods do not overlap in
sensitivity.** (a) Percentage of isolates from environmental sources per clade, on unique
strains with a recorded source, with the numerator and denominator printed beside each bar;
the dashed line is the sensu stricto value of 2.9% (683 of 23,309).
(b) Number of metagenome runs in which each clade is the dominant match at ≥0.30
containment; a dot at zero marks a clade with no run. All 52 divergent hits are gut,
faecal or unclassified and none is soil, water or waste. Sensu stricto dominated 4,960
runs, of which 299 were sampled for metadata. (c) Sensitivity of the two approaches on a
common abundance axis: implied relative abundance in the 49 gut runs where a divergent
clade was detected (points, median bar), the detection floor of those same gut runs
(0.041%, solid line) and of the deeper soil and sediment runs (0.013%, dotted line), and
the shaded range below the soil floor in which a dormant spore population would fall.
**The gut detections clear the floor of their own biome by only 2.3-fold.** Floors and
implied abundances are both computed from C = 1 − exp(−x·(L−k+1)/L) at k = 21 and L = 150,
so the k-mer recovery correction of 0.867 is included in both; the 0.30 call threshold
corresponds to 0.41-fold coverage of a 4.3 Mb genome, about 1.8 Mbp of target reads. Because
the correction multiplies floors and abundances by the same factor, it shifts both by 15%
and cancels in their ratio: the margin is 2.30-fold uncorrected and 2.29-fold corrected.
Comparing the gut abundance against the soil floor instead would give 7.3-fold and would be a
cross-biome comparison. Panels (a)
and (b) use unique strains and the nine comparable divergent clades.


---

## Discussion

The species boundary of *C. difficile* is genuinely discontinuous and the discontinuity is
reproducible, but it is easy to conceal with a poorly chosen reference panel — a caution
applying to any ANI-based species assignment in this genus. The divergent clades are real,
monophyletic and finer-grained than current nomenclature; four correspond to named cryptic
clades and nine have no published counterpart.

Whether they are separate species we do not resolve, and we do not think an ANI gap alone
can resolve it. The disagreement in the literature — novel independent genomospecies
against ancient within-species lineages — is a disagreement about gene flow, and the
appropriate test is whether recombination is interrupted at these boundaries, not whether
identity falls below a threshold. Reported interruption of gene flow in bacteria occurs
anywhere between roughly 90% and 98% identity depending on lineage, which spans our entire
divergent range. We therefore report the boundary as discontinuous, provide the
concordance needed to place these clades against the literature, and leave the rank open
pending an explicit introgression test.

The toxin result is confirmatory in kind and novel in quantification. Within-clade PaLoc
presence/absence variation and *tcdB*-specific lability are both established. What the
thirteen-clade framework adds is that the sensu stricto group — which supplies the
reference architecture for the entire diagnostic literature — is the **least** variable
clade in the genus once sampling depth is matched, while every divergent clade is an even
mixture of states. The practical consequence is concrete: a *cdtB*-only DC10 strain and a
*tcdA*-only DC9 strain both exist in this dataset and would both be missed by a two-target
assay built on the sensu stricto architecture.

The ecological question we cannot answer is worth stating plainly, because the literature
has answered it on one line of evidence. Every description of the cryptic clades as
environmental organisms rests on isolation records from surveys that deliberately sampled
soil and water. Culture-independent data give the opposite picture, and the two cannot be
reconciled by argument because they measure different things at non-overlapping
sensitivities: enrichment culture establishes presence without quantifying it, shotgun
metagenomics at these depths quantifies abundance and is blind below roughly 0.013% in soil. We
report the discrepancy rather than adjudicate it, and note that the direction of the
culture bias is known — these clades were found by looking in the environment — while the
direction of any metagenomic bias is simply a floor.

What the combined evidence does bear on is growth rather than presence. An organism
replicating in soil should at some point be a measurable fraction of some soil community,
and none of these clades is, in 300 background runs. With flat predicted growth rates, no
plant-polysaccharide machinery, narrower carbon breadth, and an oxidative-stress
reconstruction that makes the clinical lineage the derived and reduced one rather than the
divergent clades the adapted ones, the parsimonious reading is persistence as spores rather
than environmental growth. Whether those spores are abundant enough in soil to matter
ecologically is an empirical question, and the clade-specific assays reported here are
designed to answer it.

Four limitations bound this. Neither line of ecological evidence is unbiased: the culture
record over-represents the environment by construction, and the metagenome screen is
abundance-limited, with a floor near 0.013% in soil and 0.041% in the shallower gut runs,
far above where a spore population would sit. We therefore treat the habitat question as open rather than
resolved in either direction. Clade sizes remain
small — nine divergent clades are comparable, four are not, and DC11 and DC13 rest on one
strain each, so for those the clade and the strain are the same observation. Clade
attribution in the metagenome screen rests on relative k-mer containment, which is weak
for the small-margin hits. And our recombination assessment ran Gubbins on a concatenated
core-gene alignment, which violates that method's assumption of spatially contiguous
sequence; we therefore neither interpret its branch lengths as substitution counts nor use
them for dating.

---

## Methods summary

Full methods, every threshold and all caveats are in the consolidated methods record. In
brief: quality control with CheckM2 (completeness ≥95%, contamination ≤5%); ANI with skani
against a six-genome 630 reference group; average-linkage clustering at 97% with a
96.5–97.5% stability scan; PopPUNK for strain-level structure within sensu stricto;
uniform re-annotation of the 460-genome working set with Prokka 1.14.6 and pangenome
construction with Panaroo in moderate clean mode; core-genome phylogenies with FastTree and
IQ-TREE; outgroup rooting with four genomes across three genera; recombination assessment
with Gubbins; divergence estimation with BactDating and TreeTime under fixed published
clock rates; functional annotation with KOfam, Pfam-A, dbCAN and MEROPS; mobilome with
geNomad, ISEScan, IntegronFinder and alignment-based plasmid detection; growth-rate
prediction with gRodon; horizontal transfer by DIAMOND against NCBI nr with a
ribosomal-protein negative control.

**Clade concordance.** Published archetype sequence types were located in the QC-passed
sequence-type table and their clade membership recorded. Each archetype falls in exactly
one clade. No archetype has been designated for C-IV, C-V, C-VI or C-VII, so those clades
are reported as unresolved rather than inferred.

**Toxin-state diversity.** A state is the set of toxin genes present at any status in a
strain. Richness was rarefied to common depth with 2,000 draws; evenness is normalised
Shannon equitability computed over toxin-positive states only, so that non-toxigenic
strains do not contribute a state. Significance was assessed by subsampling the sensu
stricto toxin-positive strains to each clade's number of toxin-positive strains 10,000
times, and aggregated across clades both by the same procedure applied to the mean and by
Stouffer combination of per-clade p-values.

**Toxin-locus congruence.** Protein sequences for each toxin gene were extracted from the
combined toxin alignment, degapped, realigned with MAFFT, and used to infer a
gene-specific maximum-likelihood tree (IQ-TREE 2.3.0, ModelFinder, 1,000 ultrafast
bootstraps). The outgroup-rooted core-genome tree was pruned to that gene's strain set and
supplied as a topology-only constraint for a second inference. The two topologies were
compared on the same alignment with the approximately unbiased test (10,000 RELL
resamplings).

**Oxidative-stress reconstruction.** The four rooting outgroups were annotated with Prokka
and searched with hmmsearch under Pfam gathering thresholds for PF00199, PF05067, PF06397,
PF01880 and PF02915. Ancestral states were reconstructed by Fitch parsimony on the
clade-level outgroup-rooted topology, coding each clade by majority presence. Copy numbers
were not compared between the ingroup and outgroup pipelines.

**Clade-specific primer design.** Candidate targets were the clade-specific families
restricted to a single clade, single copy, not on a mobile element, carried by at least 85%
of clade members, and with no non-*Clostridioides* homologue in NCBI nr. Nucleotide
sequences were recovered from the Panaroo gene table, aligned with MAFFT, and retained only
where every sequence came from the target clade with mean column identity at least 0.95.
Primers were designed with primer3 (Tm 58–62 °C, GC 40–60%, amplicon 90–200 bp) and tested
by in-silico PCR: blastn-short of every oligo against all 460 working-set genomes, calling
an amplicon where both primers matched the same contig at ≥90% identity over near-full
length, on opposite strands, 50–500 bp apart. Specificity was assessed only within
*Clostridioides*; no environmental background or wet-lab validation was performed.

**Metagenome recruitment and its detection limit.** One representative per clade was
sketched with sourmash (k = 21, scaled = 1000) and queried against the branchwater index
of 1,161,119 SRA metagenomes. Detection limits were derived by treating k-mer containment
*C* as Poisson recovery at coverage *x*, *C* = 1 − e^(−x), so the 0.30 call threshold
requires 0.36-fold coverage of a 4.3 Mb genome, and converting that to the relative
abundance needed at each biome's median run depth. Implied abundances for detected runs
were obtained by inverting the same relation, capped at containment 0.98 where the
relation saturates. Clade attribution used relative containment across all fifteen
representatives simultaneously; a run was called for the clade with maximum containment
when that maximum reached 0.30. Biome was assigned from ENA run metadata by keyword over
scientific name, isolation source, host, environmental fields and study title. The
background comparison was a random sample of runs returned with containment between 0.02
and 0.05, drawn from the same result set as the hits.

**Plasmid detection and its circularity.** Plasmid carriage was scored two ways: by
MOB-suite replicon and relaxase markers, and by nucleotide alignment breadth against a
panel of closed plasmids. **That reference panel consists of plasmids closed from
cryptic-clade isolates of clades C-III and C-IV — the same lineages as DC2 and DC4** — so
an alignment-breadth criterion applied to draft assemblies of those clades cannot
distinguish a resident plasmid from a chromosomally integrated homologous region, and
breadth-based carriage rates for DC2 and DC4 in particular should be read as an upper
bound. Alignment identities of 85–95% indicate plasmid *families* rather than shared
plasmids; only one DC4 assembly carries a near-identical match. Marker-based and
breadth-based estimates differ roughly tenfold and both are reported.

**Deduplication and denominators.** All frequency statistics are computed on unique
strains. Of 32,957 assemblies, 30,972 pass quality control; two of those are
non-*Clostridioides* and excluded, leaving 30,970 genome entries corresponding to 29,455
unique strains. The 460-genome working set reduces to 431 strains, all 29 redundant
entries falling in divergent clades. Comparative claims use the **eleven clades with at
least six unique strains**; DC9, DC11, DC12 and DC13 are excluded from them. Where a
figure reports genome entries rather than strains this is stated in its caption.

---

## Data availability

**Genomes.** All 32,957 assemblies analysed are public; accessions for the 460-genome
working set, with clade assignment, strain key and quality metrics, and for the fifteen
clade representatives and four rooting outgroups, are supplied as supplementary tables.
Clade assignments for all 30,970 quality-passed *Clostridioides* genome entries and the
per-strain deduplication key, together with the ANI cross-check bounding that key's
completeness, are supplied in full.

**Code.** All analysis scripts, including the SLURM submission scripts for every cluster
step, are deposited in a public repository, archived at the submission commit under a Zenodo
DOI cited here. *(Repository and DOI to be inserted at submission; see detailed methods §35
for the deposit checklist.)*

**Derived data.** All derived tables and figures are listed in the supplementary index,
including the clade concordance table, the per-clade toxin-state and evenness tables with
permutation results and the deduplication sensitivity analysis, the topology-test output,
the oxidative-stress marker and ancestral-state tables with outgroup annotations and the
coding-threshold sensitivity, the clade-specificity leak table giving the second-highest
clade prevalence for every family, the Tn916/CTn element calls, the metagenome recruitment
hits with containment values and biome assignments, the per-biome detection-limit table, and
**both** the full 255-pair primer candidate set and the twelve recommended pairs with their
in-silico validation results and per-clade outcomes.

**Not deposited.** The 2.3 GB Panaroo gene table and the 156 MB primer alignment table
exceed practical deposit size and remain on the compute cluster; the scripts regenerating
them from the deposited assemblies are in the repository.
