#!/usr/bin/env python
# coding: utf-8

# In[1]:


number=[1,2,3,4]
value=iter(number)

    


# In[2]:


value


# In[3]:


val1=next(value)
val1


# In[4]:


val2=next(value)
val2


# In[10]:


value=lambda a,b,c:a+b+c
value(10,5,6)


    


# In[14]:


li=[1,3,4,5,5]


# In[17]:


for i in li:
    for j in l2:
        l2.append(i)
        print(j)


# In[ ]:


li


# In[16]:


len(li)


# In[25]:


class student:
    def teacher(self,a,b):
        return a+b

s1=student()
result=s1.teacher(33,33)
print(result)


# In[31]:


class emp:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
        
    def boss(self):
        print(self.name,self.mark)
        
    def market(self):
        val=self.name+self.mark
        print(val)
        
        
emp1=emp(33,22)
emp1.boss()
emp1.market()


# In[55]:


class A:
    def __init__(self):
        print("init A is here")
    
    def A1(self):
        print("A1 is here")
        
    def A2(self):
        print("A2 is here")
class B:
    def __init__(self):
        print("init B is here")
       
    
    def B1(self):
        print("B1 is here")
        
    def B2(self):
        print("b2 is here")
        

class C(A,B):
    def C1(self):
        print("C1 is here")
        
        
std1=C()
std1.B2()

        
        
    
    
        


# In[56]:


li=[1,2,3,4]


# In[57]:


li


# In[68]:


for i in li:
    if i==3:
        continue
    print(i)


# # DECORATOR

# In[2]:


def smart_divide(fun):
    def inner(a,b):
        if a<b:
            a,b=b,a
            return fun(a,b)
    return inner


@smart_divide
def div(a,b):
    print(a/b)

div(2,4)


# # while loop

# In[95]:


i=1

while i<=5:
    print("honey ",end="")
    j=1
    while j<=5:
        print("singh ",end="")
        j=j+1
    i=i+1
    print()


# # FOR LOOP

# In[1]:


x=['midhun',12,13,'king']
x


# In[2]:


for i in x:
    print(i)


# In[3]:


x1='midhun'
for i in x1:
    print(i)


# In[4]:


for j in range(0,10):
    print(j)


# In[13]:


for j in range(1,10,2):
    print(j)


# In[16]:


for j in range(20,0,-1):
    if j%5!=0:
        print(j)
    


# In[21]:


l='python'
print(l)


# In[22]:


for i in l:
    print(i)


# In[23]:


for i in range(len(l)):
    print(i)


# In[24]:


tup=(1,2,3,4,5,6)


# In[25]:


print(tup)


# In[26]:


for i in tup:
    print(i)


# In[27]:


for i in range(len(tup)):
    print(i)


# In[31]:


sett={1,2,3,4}
sett


# In[32]:


sett={1,"midhun","king",4,5}
sett


# In[33]:


for i in sett:
    print(i)


# In[36]:


for i in range(len(sett)):
    print(i)


# In[39]:


dicc={'name':"midhun",'age':10,'place':"allapy",'city':"pandalam"}
dicc


# In[40]:


dicc['name']


# In[44]:


dicc['city']="edappon"


# In[45]:


dicc['city']


# In[46]:


dicc


# In[47]:


a=dicc.get("name")


# In[48]:


a


# In[56]:


for x,y in dicc.items():
    print(x,y)


# In[57]:


dicc


# In[58]:


dicc.pop('age')


# In[59]:


dicc


# In[ ]:





# # dictionary methods

# In[63]:


dict={'name':"midhun",'queen':"honey","age":23}
dict


# In[64]:


len(dict) # check the length of the dictinary


# In[65]:


dict.popitem() #remove the last item


# In[66]:


dict


# In[68]:


dict.pop('name') # to remove specific element in a memory


# In[69]:


dict


# In[70]:


dict.clear() # to clear allelements in dictionary`


# In[71]:


dict


# In[72]:


dict={'name':"midhun",'queen':"honey","age":23}


# In[73]:


dict


# In[76]:


a=dict.copy() #to copy a dictionary


# In[77]:


a


# In[80]:


del dict['age']  #to delete specific elemnt in dictionary


# In[81]:


dict


# # LAMBDA FUNCTION

# In[82]:


def square(a):
    return a**2

square(5)


# In[84]:


func=lambda a:a**2
func(5)


# In[4]:


li=[1,2,3]
c=map(lambda a:a**2,li)
print(list(c))


# In[88]:


li=[2,3,45]
c=filter(lambda a:True if a%2==0 else False,li)
print(list(c))


# In[93]:


from random import shuffle


# In[92]:


def shuffle_list(mylist):
    shuffle(mylist)
    print(mylist)
    
    
    
a=[1,2,3,4]    
shuffle_list(a)    
    
    


# ###       args  AND kwags

# In[94]:


def student(a,b):
    add=a+b
    print(add)
    
student(10,30)   #if we have multiple arguments we use *args 


# In[96]:


def student(*args):
    print(args)
    print(sum(args))

student(10,30,40,50)    


# In[97]:


#if you want to add multiple keyword

def emp(a):
    print(a)
    
    
emp("king")   if you have multiple keywords we use **kwags  
    


# In[106]:


def emp(**kwags):
    print('my name is {}'.format(kwags['name']))
    print(kwags)
    
    
    
emp(name="midhun",age=33)    


# # CLASS

# In[111]:


class student:
    a=10
    


obj=student()

print(obj.a)
obj.a=40
print(obj.a)


# # constructor

# In[114]:


class honey:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("my name is ",self.a)
        print("my real name is ",self.b)
        
    
    
honey1=honey(10,"midhun")


# # INSTANCE VARIABLE

# In[13]:


class king:
    def __init__(self):
        self.name='midhun'  #instance variable it is alaways inside the constructor
        
    def disp(self):
        print(self.name)
        
obj1=king()
obj2=king()
# print(obj1.name)
obj1.name='king'
# print(obj1.name)# they can modify it is because the instance variable is copiying to the 2 objects
#we created we need to check that we are calling the method with the 2 objects 

obj1.disp()
obj2.disp()
# yes they are copying the insatnace  variable


# # class variable or static variable

# In[16]:


class myclass:
    name='zneha'
    @classmethod  #class variable allel static varaible athe acces cheyan oru decorator venam
                     #decorator means oru functionte functionality modify cheyan aanu
    def disp(cls):
        print(cls.name)
        
obj1=myclass()
obj2=myclass()
# print(obj1.name)
obj1.name='mj'  # we can modify class variable outside the class
# print(obj1.name) 
obj1.disp()
obj2.disp()


# In[ ]:





# # class method

# In[22]:


class mystudent:
    @classmethod
    def disp(cls,a):
        cls.name=a
        print("hello i am class method")
        print(cls.name)
        
# mystudent.disp()   #one way to call the class method
obj1=mystudent()   # the other way
obj1.disp('midhun')

        
        


# # static method

# In[26]:


class myemp:
    @staticmethod
    def disp(a):  #  we dont want call the parameter in here
        print("hello i am static method")
        print(a)
        
# myemp.disp()  #one way to call static method
obj1=myemp() #other way is this
obj1.disp('mylove') #we can pass through like this


# # NESTED CLASS IN PYTHON

# In[34]:


class outer_class:
    def __init__(self):
        self.name='ali'
        print(self.name)
        self.obj2=self.inner_class() # this is how we just created inner class object
    #inner class    
    class inner_class:
        def __init__(self):
            self.age=39
            self.salary=2222
        def disp(self):
            print(self.age)
            print(self.salary)
            
            
obj1=outer_class() # in this way we can acess only outer class 
# if we want to acess the inner class only one way 
# we need to craete a object in outer class constructor


# obj2=inner_class() # this object will give error

# obj1.obj2.disp() # this is how we class inner class methods(function)

a=obj1.obj2 # onather way is that create a variable and put both obj in that variable
# then we can call the method like that varible (dot.) function name thats how we can acces  the methods 
a.disp()




            


# # single inheritance

# In[39]:


class student:
    salary=1000
    @classmethod
    def show(cls):
        print("i am astudent")
        
class teacher(student):
    age=10
    @classmethod
    def disp(cls):
        print("i am a teacher")
     
obj1=teacher()
obj1.disp()
obj1.show()
print(obj1.salary)


# # constructor overriding

# In[46]:


class emp:
    def __init__(self):
        print("i am an emp constuctor")
        
    @classmethod
    def disp(cls):
        print("i  am a dispp")
        
class worker(emp):
    def __init__(self,a):
        self.name=a
        print("i am a worker constructor")
        print(a)
    @classmethod
    def show(cls):
        print("i  am a show")
        
obj1=worker('midhun')   # it will call the constructor in emp class  because worker inherit emp class
obj1.disp()


# # MULTILEVEL INHERITANCE

# In[54]:


class father:
    def __init__(slef):
        print("father constructor")
    def fdisp(self):
        print("i am father")
        
class son(father):
    def __init__(self):
        super().__init__()
        print("son constructor")
    def sdisp(self):
        print("i am a son")
        
class grandson(son):
    def __init__(self):
        super().__init__()
        print("grandson constructor")
    def gdisp(self):
        print("i am a grandson")
        
obj1=grandson()    

        
        
        


# # MULTIPLE INHERITANCE

# In[64]:


class father:
    def __init__(self):
        print("father constructor")
    def fdisp(self):
        print("this is the father")
        
class mother:
    def __init__(self):
        print("mother constructor")
    def mdisp(self):
        print("this is the mother")
        
class son(father,mother):
    def __init__(self):
        super().__init__()
        print("son constructor")
    def sdisp(self):
        print("this is the son")
        
        
        
obj1=son()  


# # Hierarchical INHERITANCE

# In[67]:


class father:
    def fdisp(self):
        print("this is father")
        
class daughter(father):
    def ddisp(self):
        print("this is daughter")
        
class son(father):
    def sdisp(self):
        print("THIS IS SON")
        
obj1=son() 
obj2=daughter()
obj2.fdisp()

        
        


# # ABSTRACT METHOD AND ABSTRACT CLASS

# In[73]:


from abc import ABC,abstractmethod
class student(ABC):
    def __init__(self):
        self.name='ali'
        print("this is constructor")
    @abstractmethod
    def show(self):
        pass
    def teacher(self):
        print("i am here ")
        
# obj1=student()  #abstract class can't access through object... in abstract class we can only initailize its we can't define 
# obj1.teacher()             # only way is to inherit the abstract class 

class teacher(student):
    def show(self):
        print("this is the way")
        print(self.name)
        
obj1=teacher()
obj1.show()

        
        


# # interface in python

# In[11]:


from abc import ABC,abstractmethod
class queen(ABC):
    @abstractmethod
    def qdisp(self):
        pass
    @abstractmethod
    def qshow(self):
        pass
    
# obj1=student()
# obj1.disp()

class king(queen):
    def qdisp(self):
        print("this is interface")
    def qshow(self):
        print("this is other interface")
        
obj1=king()
obj1.qdisp()
obj1.qshow()


# # POLYMORPHISM

# In[13]:


class father:
    def gender(self):
        print("i am male")
      
class mother:
    def gender(self):
        print("i am a female")
        
obj1=father()
obj1.gender()
obj1=mother()
obj1.gender()


# # DUCK TYPING

# In[16]:


class joker:
    def jok(self):
        print("i am a joker")
    def main(self):
        print("i am a duck")
        
class person:
    def jok(self):
        print("i am a joker")
    def main(self):  
        print("i am a duck")
 
def call(objc):
    objc.jok()
    objc.main()

obj1=joker() 
obj2=person()
call(obj1)
print("i ama that person")
call(obj2)


# # OPERATOR OVERLOADING

# In[19]:


class student:
    def __init__(self,a):
        self.a=a
        print(self.a)
        
    def __add__(self,other):
        return self.a+other.a
        
        
class text:
    def __init__(self,a):
        self.a=a
        print(self.a)
        
obj1=student(10)
obj2=text(100)
print(obj1+obj2)  #this is how we add 2 objects #same method name but the arguments are different


# # METHOD OVERLOADING

# In[30]:


class vaishnav:
    def __init__(self,a):
        self.name=a
        print(self.name)
        
    def honey(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a
        
        
        return s
        
        
obj1=vaishnav(10)
print(obj1.honey(20,20,23))


# # METHOD OVERRIDING

# In[37]:


class north:
    def show(self):
        print("this is north")
     
class south(north):
    def show(self):
        super().show() # to call the parent clsss
        print("this is south")
    
        
        
obj1=south() #both class have same method name but south inherit north in that time it override the north only show the south method
obj1.show()
        


# # DECORATOR

# In[21]:


def outer_func(temp_func):  #new_func stored in tem_func
    def inner_func():
        print("this is inner")
        print(temp_func())        
        print("the is outer")
    return inner_func()
    
@outer_func
def new_func():
    print("hello this is new function")





# def new_func():
#     print("hello this is new function")

# def outer_func(temp_func):  #new_func stored in tem_func
#     def inner_func():
#         print("this is inner")
#         print(temp_func())        
#         print("the is outer")
#     return inner_func()
    
# temp=outer_func(new_func)
# print(temp)
    
    



# In[ ]:


def hello(func):
    def inner():
        print("this is inner")
        print(func)
        
    return inner()

hello(10)


# In[48]:


def outer_func(temp_func):
    def inner_func():
        print("this is inner")
        print(temp_func())
        print("this is outer ")
    return inner_func()
    
    
@outer_func
def hello():
    print("this is hello")


# # Generator

# In[55]:


def show():
    a=10
    b=12
    yield a
    yield b
    
c=show()   
print(next(c))
print(next(c))


# In[62]:


def table():
    n=2
    i=1
    while i<=10:
        mul=i*n
        yield mul
        i=i+1
        
c=table()
for i in c:
    print(i)


# # Turnery operator

# In[3]:


score=1
if score>10:
    print("passs") 
else:
    print("fail")


# In[6]:


score=11
a="pass" if score>10 else "fail"
print(a)


# In[ ]:


def hello(func):
    def inner():
        print("this is inner")
        print(func)
        
    return inner()

a=hello(new)


def new():
    print("this is new function")


# In[3]:


def hello(func):
   def inner():
       print("this is inner")
       print("king")
       print(func())
       
   return inner()

# a=hello(new)
# print(a)

@hello
def new():
   return("this is new")


# In[ ]:




