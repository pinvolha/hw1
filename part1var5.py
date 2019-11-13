a = int(input("Ввведите число a= "))     #задача 5
b = int(input("Ввведите число b= "))
c = int(input("Ввведите число c= "))
d = int(input("Ввведите число d= "))
mas = [a, b, c, d]
res = 0
for i in range(3):
    if mas[i] % 2 != 0:
        res = res+1
if res > 0:
    print("Нечетное есть")
else:
    print("Нечетного нет")