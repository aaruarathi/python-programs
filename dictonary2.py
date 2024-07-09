x={"class":"6","subject":"maths","mark":"49"}
print(x)
print(type(x))
print(len(x))
y=dict(colour="black",fruit="apple",vehicle="bike")
print(y)
print(x["class"])
print(x.get("subject"))
print(x.keys())
print(x.values())
print(x.items())
print("class"in x)
print("class"not in x)
x["mark"]=30
print(x)
x.update({"mark":39})
print(x)
x["age"]="12"
print(x)
x.pop("subject")
print(x)
x.popitem()
print(x)
del x ["class"]
print(x)
for i in x:
    print(i)
for i in y:
    print(i)
for i in y.keys():
    print(i)
for i in y.values():
    print(i)
for i in y.items():
    print(i)
z=y.copy()
print(z)