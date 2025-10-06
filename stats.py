def word_count(text):
    return len(text.split())


def char_count(text):
    counts = {}
    for c in text.lower():
        if not counts.get(c):
            counts[c] = 0
        counts[c] += 1
    return counts
