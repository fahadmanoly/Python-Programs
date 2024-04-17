data = [3,4.2,'fhad']
print(data)
print(data[1])
for i in range(len(data)):
    print(data[i])
for i in data:
    print('i is',i)

# methods in list
# append
data.append('manoly')
print(data)

# insert
data.insert(2,151)
print(data)

# remove
data.remove(4.2)
print(data)

#pop method - removing specified elemnt using index
data.pop(3)
print(data)

#delete method
data.append(12)
print(data)
del data[3]
print(data) 
del data

# clear method
data=[1,3,5,3,6,8,2,6,8,2,'fahad']
print(data)
data.clear()
print(data)

#reverse method
data=[1,2,3,4,5,6,7,8]
print(data)
data.reverse()
print(data)
print(id(data))
print(type(data))

#Dictionary
a={'a':10,'b':20,5:'faad','c':45,'d':23,'e':43}
print(a)
print(type(a))
print(a[5])

#methods in dictionary
print(len(a))
print(a)
a.popitem()
print(a)
a.pop('b')
print(a)
cop=a.copy()
print('copy is',cop)
del cop[5]
print('deleted',cop)
cop.clear()
print(cop)





