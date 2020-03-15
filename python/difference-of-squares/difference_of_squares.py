def square_of_sum(number):
    suma = number * ((number + 1)/2)
    res = suma * suma
    return res


def sum_of_squares(number):
    func = number * (number + 1) * (2 * number + 1)
    res = func / 6
    return res


def difference_of_squares(number):
    res = square_of_sum(number) - sum_of_squares(number)
    return res

        
