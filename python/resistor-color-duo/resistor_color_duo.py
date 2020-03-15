def value(colors):
    colores = ["black", "brown", "red", "orange", "yellow", 
            "green", "blue", "violet", "grey","white",]
    
    code = code1 = code2 = ''
    
    for col in colores:
        if colors[0] == col:
            code1 =  str(colores.index(col))
        if colors[1] == col:
            code2 =  str(colores.index(col))
        code = code1 + code2

    return int(code)