def is_isogram(string):
    letters = set()
    string = string.lower()
    
    for character in string:
        if not character.isalpha():
            continue
        
        if character in letters:
            return False
        
        letters.add(character)
        
    return True
