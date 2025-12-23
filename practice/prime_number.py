import math


def is_prime(num) -> bool:  # can define the return value type like this
    if num < 2:
        return False
    else:
        for temp in range(2, int(math.sqrt(num)) + 1):
            if num % temp == 0:
                return False
    return True


def next_prime(num):
    num0 = num
    while True:
        num += 1
        if is_prime(num):
            letter = f"{num0} is no prime.\nThe next prime number is {num}."
            return letter


def main_prime_check():
    num = int(input("Enter a number :"))
    if is_prime(num):
        return True
    else:
        return next_prime(num)


main_prime_check()