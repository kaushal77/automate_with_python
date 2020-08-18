def eggs(x):
    x = [z**2 for z in x]
    return x

val = [1,2,3]
s = eggs(val)
print(val,s)

