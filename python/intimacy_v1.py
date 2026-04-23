emotional_words = ["miss", "love", "feel", "want", "need", "thinking"]

def closeness_score(message):
    words = message.lower().split()
    score = 0
    
    for w in words:
        if w in emotional_words:
            score += 3
    
    score += len(words) * 0.5
    return score