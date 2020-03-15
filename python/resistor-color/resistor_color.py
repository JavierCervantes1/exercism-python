def color_code(color):
    
    for col in colors():
        if color == col:
            return colors().index(col)


def colors():
    return ["black", "brown", "red", "orange", "yellow", 
            "green", "blue", "violet", "grey","white",]
