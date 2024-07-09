def printname():
    print("hello")
printname()
def sum():
    a=2
    b=4
    print(a+b)
sum()
def add(x,y):
    print(x+y)
add(1,5)
def subtract(*x):
    print(x[2]-x[1])
subtract(10,20,30,40,50)
def multiply(x,y,z):
    print(x*y*z)
multiply(x=3,y=6,z=1)
def sum(**x):
    print(x["i"]+x["j"])
sum(i=22,j=11,k=14,l=43)
def country(c="india"):
    print("iam from "+c)
country("usa")
country("canada")
country()
def name(x):
    for i in x:
        print(i)
y=["arathi","greeshma","aswathi","gokul"]
name(y)
def number(x):
    return 10+x
print(number(40))
def add():
    pass
y=lambda x:x+5
print(y(10))
z=lambda x,y:x+y
print(z(6,4))

