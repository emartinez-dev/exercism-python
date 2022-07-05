def find_anagrams(word, candidates):
    anagrams = []
    
    for candidate in candidates:
        if word.lower() == candidate.lower():
            pass
        elif sorted(list(word.lower())) == sorted(list(candidate.lower())):
            anagrams.append(candidate)
    
    return anagrams
