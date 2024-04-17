lst=[1,2,3,1]
lst2=lst.copy()
lst3=lst
print(id(lst),lst)
print(id(lst2),lst2)
print(id(lst3),lst3)

lst.remove(1)
print(lst)
print(lst2)
print(lst3)