mas = []
k = int(input("Введите число элементов "))
for i in range(k):
    new_element = int(input())
    mas.append(new_element)
mas.append(0)
n = 0
for i in range(0, len(mas)):
    if (mas[i] > 0) and (mas[i + 1] < 0):
        n += 1
    if (mas[i] < 0) and (mas[i + 1] > 0):
        n += 1
    if mas[i] == 0:
        print(n)
        break
