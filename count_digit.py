n = int(input("enter the number: "))

num = n
count = 0
while num > 0:
    num = num // 10
    count = count + 1
print(count)
