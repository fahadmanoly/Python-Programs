
import math
#functions
def fns(a,b):
    s=a+b
    return s

c=fns(30,40)
print(c)

#lambda function
fns = lambda a,b:a*b
print(fns(2,3))

 # list comprehesnison
lic = [2**i for i in range(1,6)]
newlic = [math.sqrt(n) for n in lic if n%2 ==0 ]
print(lic)
print(newlic)

# dictionary comphresnsion
newdic = {j:j*j for j in lic}
print(newdic)





