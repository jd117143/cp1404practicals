"""
CP1404 - Practical 5
Program counts word occurrences in a string
Estimate: 30 minutes
Actual: 42 minutes
"""

word_to_count = {}
text = input("Enter text: ")
words = text.split()

for word in words:
    count = word_to_count.get(word, 0)
    word_to_count[word] = count + 1

max_length = max(len(word) for word in word_to_count.keys())
for word, count in sorted(word_to_count.items()):
    print(f"{word:{max_length}}: {count}")
