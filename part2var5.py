import numpy

i = (0.9, 8.4, 2)
y = 1.6 * (10 ** (-4))
x = -1
k = 6
for j in range(len(i)):
    c = i[j] / k - (numpy.sqrt(y) / 0.4)
    d = numpy.e ** (1 - c) + 4.9 * (x ** 2 + 1)
    print(d)

i = 0
while i <= 3:
    c = i / k - (numpy.sqrt(y) / 0.4)
    a = numpy.e ** (1 - c) + 4.9 * (x ** 2 + 1)
    i += 0.5
    print(a)

y = (1.3, 8, 0.2)  # -8 заменено на 8,тк нельзя корень извлечь
x = 1
for n in range(len(y)):
    while x <= 2:
        c = i / k - (numpy.sqrt(y[n]) / 0.4)
        b = numpy.e ** (1 - c) + 4.9 * (x ** 2 + 1)
        x += 0.1
        print(b)
