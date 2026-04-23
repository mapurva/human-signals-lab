def preprocess(message):
    import string
    return message.translate(str.maketrans('', '', string.punctuation)).lower()

def closeness_score(message):
    processed = preprocess(message)
    words = processed.split()
    score = 0
    
    emotional_words = ["miss", "love", "feel", "want", "need", "thinking"]
    
    for w in words:
        if w in emotional_words:
            score += 3   # Dev B improvement
    
    score += len(words) * 0.5
    return score