for i in range(1, 11):
    print(i)

print("====================================")

i = 10

while i >= 1:
    print(i)
    i -= 1
print("====================================")

n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)
print("====================================")

n = int(input("Enter n: "))
sum = 0

for i in range(1, n + 1):
    sum += i

print("Sum =", sum)
print("====================================")

n = int(input("Enter a number: "))
fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial =", fact)
print("====================================")

for i in range(2, 101, 2):
    print(i)
print("====================================")
n = int(input("Enter a number: "))
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

print("Reverse =", reverse)
print("====================================")

n = int(input("Enter a number: "))
count = 0

while n > 0:
    n = n // 10
    count += 1

print("Number of digits =", count)
print("====================================")
n = int(input("Enter a number: "))
count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

if count == 2:
    print("Prime number")
else:
    print("Not a prime number")
print("====================================")

n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c
