def word_count(text):
    return len(text.split())


def char_count(text):
    counts = {}
    for c in text.lower():
        if not counts.get(c):
            counts[c] = 0
        counts[c] += 1
    return counts


def sort_dict_by_value(d: dict) -> list[dict]:
    def sort_on(item):
        return item["num"]

    items = []
    for key in d:
        items.append({"char": key, "num": d[key]})
    items.sort(key=sort_on, reverse=True)
    return items
