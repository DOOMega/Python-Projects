
def factoriel(number):
    if not number >= 0:
        raise ValueError('must be zero or positive')
    
    def inner_factoriel(number):
        if number <= 1:
            return 1

        return number * inner_factoriel(number - 1)
    return inner_factoriel(number)

print(factoriel(5))