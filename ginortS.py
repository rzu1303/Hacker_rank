l = []
u = []
o = []
e = []

for i in input():
    if i.isdigit():
        if int(i) % 2 == 0:
            # e = i
            e.append(i)
        else:
            # o = i
            o.append(i)
    else:
        if  i.islower():
            # l = i 
            l.append(i)
            # l.sort()
        else:
            # u = i 
            u.append(i)

l.sort()
u.sort()
o.sort()
e.sort()
print("".join(l+u+o+e))

