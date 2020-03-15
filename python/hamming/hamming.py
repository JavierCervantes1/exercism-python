def distance(strand_a, strand_b):
    da = len(strand_a)
    db = len(strand_b)
    
    if da == db:
        res = sum(strand_a != strand_b for strand_a, strand_b in zip(strand_a, strand_b))
    else:
        raise ValueError("Los tamaños no son igual")
        res = 0
    return res
