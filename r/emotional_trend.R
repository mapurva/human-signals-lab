messages <- readLines("data/messages.txt")

emotional_words <- c("miss", "love", "feel", "want", "need", "thinking")

closeness_score <- function(msg) {
  words <- strsplit(tolower(msg), " ")[[1]]
  score <- 0
  
  for (w in words) {
    if (w %in% emotional_words) {
      score <- score + 2
    }
  }
  
  score <- score + length(words) * 0.5
  return(score)
}

scores <- sapply(messages, closeness_score)

print(data.frame(messages, scores))

plot(scores, type="o", main="Emotional Trend",
     xlab="Message Index", ylab="Score")

write.csv(data.frame(messages, scores), "results/trend_output.csv")