def count_words(text):
    return len(text.split())


def count_characters(text):
    counts = {}
    characters = list(text)

    for char in characters:
        char = char.lower()
        if char in counts and char is not None:
            counts[char] += 1
            continue
        counts[char] = 1

    return counts


def sort_dictionaries(dict):
    list_dict = sorted([{x:y} for x,y in dict.items()], key=lambda x : list(x.values()), reverse=True)
    return list_dict







