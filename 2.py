a = int(input("Введите первое целое число: "))
b = int(input("Введите второе целое число: "))

result = 0
for _ in range(abs(b)):
    result += a

if b < 0:
    result = -result

print(result)
