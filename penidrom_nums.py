# n = int(input("enter the number: "))

# num = n
# result = 0

# while num > 0:
#     ld = num % 10
#     result = result * 10 + ld
#     num = num // 10
# if result == n:
#      print(f"{n} is a penidrom number")
# else:
#     print(f"{n} is not a penidrom number")

n = int(input("enter the number:"))

num = n
result = 0
while num > 0:
    ld = num % 10
    result = result * 10 + ld
    num = num // 10
if result == n:
    print(f"{n} id penidrom")
else:
    print(f"{n} is not penidrom")
