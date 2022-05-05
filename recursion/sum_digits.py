def sum_of_digits(n):
    assert n >= 0 and int(n) == n, "The number has to be only positive integer"
    if n == 0:
        return 0
    else:
        return int(n%10) + sum_of_digits(int(n//10))

print(sum_of_digits(-2))