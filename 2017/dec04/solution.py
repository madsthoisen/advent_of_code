with open("input") as f:
	phrases = [phrase.strip().split(" ") for phrase in f.readlines()]

# part I
print(sum(len(phrase) == len(set(phrase)) for phrase in phrases))

# part II
phrases_sorted = [[''.join(sorted(word)) for word in phrase] for phrase in phrases]
print(sum(len(phrase) == len(set(phrase)) for phrase in phrases_sorted))
