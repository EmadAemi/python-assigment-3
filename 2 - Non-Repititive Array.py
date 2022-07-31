import random
a = []
n = int(input("N: "))
while len(a) < n:
    temp = random.randint(0,10*n)
    if temp not in a:
        a.append(temp)
print(a)