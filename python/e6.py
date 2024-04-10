def frst(x,y):
    list = []
    for i in range(x,y):
        tavan = i**2
        list.append(tavan)
    return sum(list)


def scnd(x,y):
    list = []
    for i in range(x,y):
        list.append(i)
    x = sum(list)
    return x**2

print(scnd(1,101)-frst(1,101))