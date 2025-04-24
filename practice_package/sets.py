def find_common_elements(set1, set2):
    return {item for item in set1 if item in set2}

def is_superset(set_a, set_b):
    return all(item in set_a for item in set_b)

def remove_duplicates(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def count_unique_words(text):
    words = text.lower().split()
    return len(set(words))

def find_shared_items(*sets):
    if not sets:
        return set()
    shared = sets[0].copy()
    for s in sets[1:]:
        shared.intersection_update(s)
    return shared