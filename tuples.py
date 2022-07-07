#this code gives overview on tuples
'''tuples=['potato','tomato','brinjal']
print(tuples)'''

#access python
'''tuples=['potato','tomato','brinjal']
print(len(tuples))'''


#creation of tuple
'''y=('one',)
print(type(y))

y=['one',]
print(type(y))

y=('one')
print(type(y))'''

#update the tuples
'''y=('one','two','three')
z=list(y)
z[1]='four'
y=tuple(z)
print(y)'''


'''y=('one','two','three')
z=list(y)
z.append("four")
y=tuple(z)'''


'''y=('one','two','three')
z=('four',)
y+=z
print(y)'''

#remove of element is also share same process  on add

#deletion of tuple
'''y=('one','two','three')
del y
print(y)'''
#this shows error as such tuple is not exists

#unpack tuples
'''y=('one','two','three')
(red,green,blue)=y
print(red)
print(green)
print(blue)'''


'''y=('one','two','three','four','five')
(red,green,*blue)=y
print(red)
print(green)
print(blue)'''

#join tuples
'''a=('1','2','3')
b=('4','5','6')
c=a+b
print(c)'''

'''a=('1','2','3')
c=a*2
print(c)'''

a=('1','2','3')
c=a*2
print(c)
d=c.count('2')
print(d)
e=c.count('3')
print(e)


