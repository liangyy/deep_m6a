countFreq <- function(mydat.valid) {
  hit <- mydat.valid$peak.id
  valid.count <- data.frame(table(hit))
  valid.count <- valid.count %>% mutate(peak.id = hit) %>% select(Freq, peak.id)
  mydat.valid <- inner_join(mydat.valid, valid.count, by = 'peak.id')
  mydat.valid <- mydat.valid %>% mutate(log2.freq = floor(log2(Freq)))
  return(list(count = valid.count, df = mydat.valid))
}
stratifyMatch <- function(f, t, c, e) {
  apply(data.frame(f = f, t = t, c = c, e = e), 1, .stratifyMatch)
}
.stratifyMatch <- function(x) {
  f <- x[1]
  t <- x[2]
  c <- x[3]
  e <- x[4]
  if (c + f + t ==0) {
    return('ncRNA')
  } else if (f / e > 0.75 & t == 0) {
    return('fiveUTR')
  } else if (t / e > 0.75 & f == 0) {
    return('threeUTR')
  } else if (c / e > 0.75) {
    return('CDS')
  } else if (t * f * c != 0) {
    return('wholeTranscript')
  } else if (f * c != 0) {
    return('mixFiveCDS')
  } else if (t * c != 0) {
    return('mixThreeCDS')
  }
}
stratifyPeak <- function(x) {
  class(x) <- 'character'
  types <- unique(x)
  if (length(types) == 1) {
    return(types)
  } else {
    return('notSure')
  }
}