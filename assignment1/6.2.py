def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


def sum_prime(n):
    total = 0
    for i in range(1, n + 1):
        if is_prime(i):
            total += i
    return total


n = int(input("Enter n: "))
print("Sum of prime numbers:", sum_prime(n))