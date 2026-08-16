import random

# Replace with your own roll number
random.seed(1024170406)

#Generate 100 random numbers between 100 and 900 (inclusive)
numbers = [random.randint(100, 900) for _ in range(100)]

print("Random numbers:", numbers)

#Count and print all odd numbers
odd_numbers = [num for num in numbers if num % 2 != 0]
print("Odd numbers:", odd_numbers)
print("Count of odd numbers:", len(odd_numbers))

#Count and print all even numbers
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers:", even_numbers)
print("Count of even numbers:", len(even_numbers))

#Count and print all prime numbers
def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


prime_numbers = [num for num in numbers if is_prime(num)]

print("Prime numbers:", prime_numbers)
print("Count of prime numbers:", len(prime_numbers))

#Number occurring most frequently and its frequency
most_frequent = max(set(numbers), key=numbers.count)
frequency = numbers.count(most_frequent)

print("Most frequent number:", most_frequent)
print("Number of occurrences:", frequency)