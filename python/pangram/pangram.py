def is_pangram(sentence):
    letters = set()
    
    for character in sentence:
        if character.isalpha():
            letters.add(character.lower())
        
    return len(letters) == 26
