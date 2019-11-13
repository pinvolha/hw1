import random
n = int(input("Введите число элементов "))
A = []
for i in range(n):
    new_element = random.randint(0, 99)
    A.append(new_element)
print(A)
B = []
for i in range(0, len(A)):
    if (i % 2 == 0) and ((i + 1) < len(A)):
        b = A[i] + A[i + 1]
        B.append(b)
print(B)