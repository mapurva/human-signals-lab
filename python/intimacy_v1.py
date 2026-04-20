def closeness_score(message):
    words = message.lower().split()
    score = 0
    
    emotional_words = ["miss", "love", "feel", "want", "need", "think"]
    
    for w in words:
        if w in emotional_words:
            score += 2
    
    score += len(words) * 0.5
    
    return score

msg = input("Enter message: ")
print("Closeness Score:", closeness_score(msg))