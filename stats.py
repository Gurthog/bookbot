def word_count(text):
    return len(text.split())


def char_count(text):
    counts = {}
    for c in text.lower():
        if c not in counts:
            counts[c] = 0
        counts[c] += 1
    return counts
