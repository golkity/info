a = int(input("Введите первое целое число (A): "))
b = int(input("Введите второе целое число (B): "))

for i in range(a, b + 1):
    print(f"{i}*{i}={i*i}")
