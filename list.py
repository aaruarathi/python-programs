a=[1,2,3,4,5,6]
print(a)
print(type(a))
print(len(a))
b=list(("apple","orange","grapes","banana"))
print(b)
print(b[1])
print(b[-1])
print(b[1:3])
print(b[-3:-1])
print(b[1:])
print(b[:3])
print("apple"in(b))
print("lemon"in(b))
print("lemon "not in b)
print("apple"not in b)
b[1]="mango"
print(b)
b[-1]="orange"
print(b)
b.append("mango")
print(b)
b.insert(2,"watermelon")
print(b)
b.extend(a)
print(b)
b.remove("mango")
print(b)
b.pop(4)
print(b)
b.pop()
print(b)
del b[3]
print(b)
# b.clear()
# print(b)
# del b
# print(b)
for i in b:
    print(i)
c=list(("black","red","white","yellow","orange"))
print(c)
c.sort()
print(c)
c.sort(reverse=True)
print(c)
d=[4,9,1,5,10]
print(d)
d.sort()
print(d)
d.sort(reverse=True)
print(d)
e=d.copy()
print(e)
f=list(c)
print(f)
h=c+d
print(h)
for i in d:
    a.append(i)
print(a)
print(a.count(1))

