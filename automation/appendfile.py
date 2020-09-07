import os

baconfile = open('hello.txt','a')
baconfile.write('come lets go!!')
baconfile.close()

baconfile = open('hello.txt','r')
x = baconfile.read()
baconfile.close()
print(x)