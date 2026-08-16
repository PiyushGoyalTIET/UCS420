#WAP to add all prime numbers from 1 to n
n = int(input("Enter a number: "))
sum = 0
is_prime = True
for i in range(2, n + 1):
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        sum += i
print("Sum of prime numbers from 1 to", n, "is:", sum)