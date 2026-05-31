from collections import Counter

with open("words.txt", "r", encoding="utf-8") as f:
    words = [line.strip().lower() for line in f]

print("total:", len(words))
print("only:", len(set(words)))

counts = Counter(words)
duplicates = [w for w, c in counts.items() if c > 1]
print(len(duplicates))