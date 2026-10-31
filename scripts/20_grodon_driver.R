.libPaths(c("/home/nejc/cdiff_clades/Rlib", .libPaths()))
suppressMessages({library(gRodon); library(Biostrings)})
ids <- readLines("/home/nejc/cdiff_clades/ws460_ids.txt")
outf <- "/home/nejc/cdiff_clades/grodon_460.csv"
cat("genome_id,n_cds,nHE,CUBHE,ConsistencyHE,CPB,FilteredSequences,d_hours,LowerCI,UpperCI\n", file=outf)
for (g in ids) {
  f <- file.path("/home/nejc/cdiff_clades/prokka460", g, paste0(g, ".ffn"))
  if (!file.exists(f)) { cat("MISSING", g, "\n"); next }
  genes <- readDNAStringSet(f)
  he <- grepl("ribosomal protein", names(genes), ignore.case = TRUE)
  if (sum(he) < 10) { cat("FEWHE", g, sum(he), "\n"); next }
  out <- try(suppressWarnings(predictGrowth(genes, he, mode = "full")), silent = TRUE)
  if (inherits(out, "try-error")) { cat("FAIL", g, "\n"); next }
  cat(paste(c(g, length(genes), sum(he), out$CUBHE, out$ConsistencyHE, out$CPB,
              out$FilteredSequences, out$d, out$LowerCI, out$UpperCI), collapse=","), "\n",
      sep="", file=outf, append=TRUE)
}
cat("gRodon version:", as.character(packageVersion("gRodon")), "\n")
