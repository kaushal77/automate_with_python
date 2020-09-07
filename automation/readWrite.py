import os

hellofile = open(str(os.path.abspath('.'))+'\\hello.txt')
textvalue = hellofile.readlines()
hellofile.close()
print(textvalue)
