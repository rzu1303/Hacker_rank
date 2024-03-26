l = []
u = []
o = []
e = []

for i in input():
    if i.isdigit():
        if int(i) % 2 == 0:
            e.append(i)
        else:
            o.append(i)
    else:
        if  i.islower():
            l.append(i)
        else:
            u.append(i)

l.sort()
u.sort()
o.sort()
e.sort()
print("".join(l+u+o+e))

