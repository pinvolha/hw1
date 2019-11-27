import os
f1 = open(r"D:\test.txt", "r")
f2 = open(r"D:\test2.txt", "w+")
i = 1
while True:
    line = f1.readline()
    if i >= 4:
        f2.write(line)
    i += 1
    if len(line) == 0:
        break

f1.close()
f2.close()

f2 = open(r"D:\test2.txt", "r+")
lines = f2.readlines()
last_line = str(lines[-1])
print(last_line)
words = last_line.split()
last_word = len(words[-1])
print(last_word)
f2.close()
