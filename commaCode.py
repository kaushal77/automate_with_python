
def comma(arr):
    z = arr[:-1]
    foo = ", ".join(str(y) for y in z)
    strfoo = foo + ' and ' + str(arr[-1])
    return strfoo



spam = ['apples', 42 , 'tofu', 'cats']
x= comma(spam)
print(x)