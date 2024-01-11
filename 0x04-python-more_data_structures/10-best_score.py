#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return None
    max_score = max(a_dictionary.values())
    best = [key for key, value in a_dictionary.items() if value == max_score]
    return best[0] if best else None
