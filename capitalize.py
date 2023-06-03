def solve(s):
    for x in s[:].split():

        s = s.replace(x, x.capitalize())
    return s
name = input()
result = solve(name)
print(result)