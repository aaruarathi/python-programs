m=["elephant","lion","cat","dog","tiger"]
print(m)
print(type(m))
print(len(m))
print(m[3])
print(m[-2])
print(m[2:4])
print(m[-3:-1])
print("cat"in m)
print("monkey"in m)
print("cat"not in m)
print("monkey"not in m)
m[3]="bear"
print(m)
m[-1]="panda"
print(m)
m.append("snake")
print(m)
m.insert(3,"zeebra")
print(m)
n=[11,22,33,44,55]
print(n)
m.extend(n)
print(m)
m.remove("lion")
print(m)
m.pop(2)
print(m)
m.pop()
print(m)
del n [2]
print(n)
for i in m:
    print(i)
n.sort()
print(n)
n.sort(reverse=True)
print(n)
o=[5,7,1]
print(o)
p=o.copy()
print(p)
x=list(m)
print(x)
q=n+o
print(q)
print(q.count(11))