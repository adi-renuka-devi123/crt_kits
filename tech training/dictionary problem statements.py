# prg 3 word frequency analyzer-Resume Parser
text = input().lower().split()
freq = {}
for w in text: freq[w] = freq.get(w, 0) + 1
print(freq, "| Top 3:", sorted(freq.items(), key=lambda x: x[1], reverse=True)[:3])