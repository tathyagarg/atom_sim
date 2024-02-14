import math


def decimal_to_int(val: float) -> int:
    """
    Converts the given value to an integer
    Eg:
        0.123 => 123
        0.28  => 28
    """
    while val - math.floor(val) != 0:
        val *= 10
    return int(val)  # Casting back to int is not required as val will always be a whole number


def fetch_int_length(number: int) -> int:
    """Returns the number of digits in the given number"""
    if number == 0: return 1  # Edge case

    length = 0
    while number != 0:  # Better than 'while number:' in terms of readability
        number //= 10   # Removes one of the digits
        length += 1
    return length


def fetch_float_length(number: float) -> int:
    """Returns the length of the given float, including the decimal point"""
    if number == 0: return 3  # Edge case

    whole, part = math.floor(number), number - math.floor(number)
    part = decimal_to_int(part)  # Converting to integer so the `fetch_int_length` function accepts it as a parameter
    return fetch_int_length(whole) + fetch_int_length(part) + 1  # Adding 1 to account for the decimal


def digit_sum(num: int) -> int:
    """Returns the sum of the digits"""
    total = 0
    while num != 0:
        total += num % 10
        num //= 10
    return total


def join_numbers(nums: tuple[int, ...]) -> int:
    """Joins the numbers into a single number"""
    total = 0
    for i, num in enumerate(nums):
        total += num * 10**i
    return total


def generate_checksum(*args):
    """Use the Luhn Checksum"""
    digits = [n * ((i % 2) + 1) for i, n in enumerate(args)]
    digit_sums = [digit_sum(n) for n in digits]
    check_digit = 10 - (sum(digit_sums) % 10)
    return join_numbers(args) * 10 + check_digit
