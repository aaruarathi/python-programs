# def sum():
#     a=20
#     b=30
#     print(a+b)
# sum()
# def multiply():
#     a=20
#     b=30
#     print(a*b)
# multiply()

# def average():
#     m=30
#     n=100
#     o=2000
#     k=(m+n+o)/3
#     print(k)
# average() 

# def sum():
#     m=int(input("enter a number"))
#     sum=0
#     for i in range(1,m):
#         sum+=i
#     print(sum)
# sum()
        
# def factorial():
#     n=int(input("enter a number"))
#     fact=1
#     while(n>0):
#         fact=fact*n
#         n=n-1
#     print(fact)
# factorial()

# def year():
#     k=int(input("enter a year"))
#     if k%4==0:
#         print("leap year")
#     else:
#         print("not a leap year") 
# year()  

# def fibinocci(x):
#     j=0
#     k=1
#     print(j)
#     print(k)
#     for i in range(0,x+1):
#         l=j+k
#         j=k
#         k=l
#         print(l)
# fibinocci(6)

def number():
    a=3
    n=0
    if a>1:
        for i in range(1,a+1):
            if(a%i)==0:
                n=n+1
    if n==2: 
        print("prime number")
    else:
        print("number is not prime")

number()
        



    