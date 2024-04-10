list_sec = []
for i in range(1, 1001):
    list_sec.append(i)

for a in list_sec[:1000//2]:
    for b in range(a, 1000-a):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print(a, b, c)
