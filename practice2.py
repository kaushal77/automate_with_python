#line-continuation character
# print("hello " + \
#     "boy")

# #sort() method for lists
# a = ["a","ddff","ASSWWE","iri4ji"]
# a.sort()
# print("after sorting : ",a)
# a.sort(key = str.lower)
# print(a)

# #tupple

# tup = ('cat','bat','rat')
# print(tup[0])

#reference

a = ['cat','bat','rat']
b = ['a','b','c']
a = b
print(a,b)
a[0] = 'horse'
print(a,b)