#WAP to add all numbers divisible by 7 and 9 from 1 to n
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n + 1):
    if i % 7 == 0 and i % 9 == 0:
        sum += i

print("The sum of numbers divisible by 7 and 9 from 1 to", n, "is:", sum)