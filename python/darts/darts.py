def score(x, y):
    dart_location = (x ** 2 + y ** 2) ** (1 / 2)
    if dart_location <= 1:
        return 10
    elif dart_location <= 5:
        return 5
    elif dart_location <= 10:
        return 1

    return 0
