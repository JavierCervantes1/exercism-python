def find_anagrams(word, candidates):
    newcandidates = []
   
    for candidate in candidates:
        if len(candidate) == len(word) and candidate.lower() != word.lower():
            if sorted(candidate.lower()) == sorted(word.lower()):
                newcandidates.append(candidate)
            
    return newcandidates
    