dec = int(input())

for i in range(1, int(number)+1):
    width = len(f"{number:b}")
    print(f"{i:{width}} {i:{width}o} {i:{width}X} {i:{width}b}")



