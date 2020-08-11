catname = []
while True:
    print("enter name of cat " + str(len(catname)+1) + "(or enter nothing to stop)")
    name = input()
    if name =='':
        break
    catname = catname + [name]
print('names are:')
for i in catname:
    print(i)