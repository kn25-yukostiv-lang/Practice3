p = int(input("Введіть число p: "))

count = 0

for i in range(10, p + 1):
    s = str(i)
    if all('5' <= ch <= '9' for ch in s):
        count += 1

print("Кількість чисел:", count)