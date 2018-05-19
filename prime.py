def prime(number):
    if number <= 0:
        return "error not allowed"

    results = []
    for i in range(2, number + 1):
        if is_prime(i):
            results.append(i)

    return results


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True



#New prime
def prime_tdd(number):
    """
    input:
        number(int) -> this is a positive

    outputs:
        results(list) -> list of numbers
    """
    if number < 0:
        return "error"

    results = []
    for i in range(2, number + 1):
        if is_prime(i):
            results.append(i)

    return results
