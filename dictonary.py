x={"name":"arathi","age":20,"job":"student"}
print(x)
print(type(x))
print(len(x))
y=dict(colour="red",fruit="mango",vehicle="car")
print(y)
print(x["age"])
print(x.get("job"))
print(x.keys())
print(x.values())
print(x.items())
print("age"in x)
print("age"not in x)
print("place"in x)
print("place"not in x)
x["age"]=15
print(x)
x.update({"age":19})
print(x)
x["course"]="data analytics"
print(x)
x.update({"course":"data analytics"})
print(x)
x.pop("name")
print(x)
x.popitem()
print(x)
del x ["age"]
print(x)
# x.clear()
# print(x)
# del x 
# print(x)
for i in y:
    print(i)

for i in y:
    print(y[i])

for i in y.keys():
    print(i)
for i in y.values():
    print(i)
for i in y.items():
    print(i)
z=y.copy()
print(z)
x=dict(y)
print(x)
family={"child1":{"name":"greeshma","age":20},
        "child2":{"name":"gokul","age":24},
        "child3":{"name":"aswathi","age":23}}
print(family)
print(family["child2"])
print(family["child2"]["age"])
print(family["child3"]["name"])
        
 