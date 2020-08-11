def collatz(number):
    if number%2 == 0:
        x  = number // 2
        print(x)
        return x
    else:
        z = 3*number + 1
        print(z)
        return z
        

try:
    uservalue = int(input('enter value: '))
    foo = 0
    while(foo != 1):
        foo = collatz(uservalue)
        uservalue = foo
except ValueError:
    print('enter only integer')
        
