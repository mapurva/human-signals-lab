def reverse_message(msg):
    return " ".join(msg.split()[::-1])

def symmetry_score(msg):
    reversed_msg = reverse_message(msg)
    
    original_words = msg.lower().split()
    reversed_words = reversed_msg.lower().split()
    
    matches = 0
    
    for w1, w2 in zip(original_words, reversed_words):
        if w1 == w2:
            matches += 1
    
    return matches / len(original_words)


msg = input("Enter message: ")

rev = reverse_message(msg)
score = symmetry_score(msg)

print(f"Original: {msg}")
print(f"Reversed: {rev}")
print(f"Symmetry Score: {score}")