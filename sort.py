import random
import datetime
import prettytable
import matplotlib.pyplot as plt

def selsort(A):
    for i in range(len(A) - 1):
        m = i
        for j in range(i + 1, len(A)):
            if A[j] < A[m]:
                m = j
        A[i], A[m] = A[m], A[i]

def inssort(A):
    for i in range(1, len(A)):
        t = A[i]
        j = i - 1
        while j >= 0 and A[j] > t:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = t

table = prettytable.PrettyTable(["Размер списка", "Время Select", "Время Insert"])
x=[]
y1=[]
y2=[]

for N in range(1000,5001,1000):
    x.append(N)
    min = 1
    max = N
    A=[]
    for i in range(N):
        A.append(int(round(random.random()*(max-min)+min)))

print(A)
B = A.copy()

print("---")
selsort(A)
print(A)

print("******")

print(B)
print("---")
inssort(B)
print(B)


t1 = datetime.datetime.now()
selsort(A)
t2 = datetime.datetime.now()
y1.append((t2-t1).total_seconds())
print("Select сортировка   " +str(N)+"   заняла   "+str((t2-t1).total_seconds()) + "c")

t3 = datetime.datetime.now()
inssort(B)
t4 = datetime.datetime.now()
y2.append((t4 - t3).total_seconds())
print("Insert сортировка   " +str(N)+"   заняла   "+str((t4-t3).total_seconds()) + "c")
table.add_row([str(N), str((t2-t1).total_seconds()), str((t4-t3).total_seconds())])
print(table)

plt.plot(x, y1, "C0")
plt.plot(x, y2, "C1")
plt.show()