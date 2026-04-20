# Read messages
messages <- readLines("data/messages.txt")

# Emotional words
emotional_words <- c("miss", "love", "feel", "want", "need", "thinking")

# Function to compute score
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

# Compute scores
scores <- sapply(messages, closeness_score)
scores <- scores / max(scores)

# Print results
print(data.frame(messages, scores))

# Plot trend
plot(scores, type="o", main="Emotional Trend",
     xlab="Message Index", ylab="Score")