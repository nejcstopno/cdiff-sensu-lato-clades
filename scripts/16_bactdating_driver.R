
.libPaths(c("/home/nejc/cdiff_clades/Rlib", .libPaths()))
suppressMessages({library(BactDating); library(ape)})
args <- commandArgs(trailingOnly=TRUE)
TR <- args[1]; RATE <- as.numeric(args[2]); L <- 2540864
tag <- sprintf("%s_%s", TR, args[2])
tr <- read.tree(sprintf("dating/%s.nwk", TR))
n  <- length(tr$tip.label); mu <- RATE*L
set.seed(42)
res <- bactdate(tr, rep(2020, n), initMu=mu, updateMu=FALSE, updateAlpha=FALSE,
                updateSigma=FALSE, updateRoot=FALSE, model="strictgamma",
                nbIts=100000, thin=100, showProgress=FALSE)
dt <- res$tree; dep <- node.depth.edgelength(dt); dates <- dt$root.time + dep
meta <- read.csv("clade460.csv", stringsAsFactors=FALSE)
out <- data.frame()
for (cc in unique(meta$new_clade)) {
  mem <- meta$genome_id[meta$new_clade==cc]; mem <- mem[mem %in% dt$tip.label]
  nodeid <- if (length(mem)==1) which(dt$tip.label==mem) else getMRCA(dt, mem)
  par <- dt$edge[dt$edge[,2]==nodeid,1]
  ci  <- if (length(par)==1 && par<=nrow(res$CI)) res$CI[par,1:2] else c(NA,NA)
  out <- rbind(out, data.frame(tree=TR, rate=RATE, clade=cc, n=length(mem),
    stem_Mya=(2020-dates[par])/1e6, stem_lo_Mya=(2020-ci[2])/1e6, stem_hi_Mya=(2020-ci[1])/1e6,
    crown_Mya=(2020-dates[nodeid])/1e6))
}
rid <- n+1
out <- rbind(out, data.frame(tree=TR, rate=RATE, clade="ROOT_460", n=n,
  stem_Mya=NA, stem_lo_Mya=NA, stem_hi_Mya=NA, crown_Mya=(2020-dates[rid])/1e6))
write.csv(out, sprintf("dating/bd_%s.csv", tag), row.names=FALSE)
write.tree(dt, sprintf("dating/bd_%s.nwk", tag))
cat("DONE", tag, "root_Mya", (2020-dates[rid])/1e6, "\n")
