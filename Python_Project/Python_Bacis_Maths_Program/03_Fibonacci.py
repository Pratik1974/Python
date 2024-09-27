# Fibonacci Series in Python

n = int(input("Enter the number of terms: "))
first, second = 0, 1
print("Fibonacci Series:")

for i in range(n):
    print(first, end=" ")
    first, second = second, first + second
