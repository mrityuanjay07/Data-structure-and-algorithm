n = int(input("enter the number:"))

num = n
factors = []
for i in range(1, num // 2):
    if num % i == 0:
        factors.append(i)
factors.append(num)
print(factors)
