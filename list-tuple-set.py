l= []
n=int(input("enter limit:"))
print("enter the elements:")
for a in range(n):
     l.append(input(""))
print("list is:",l)
t=tuple(l)
print("tuple is:",t)
s=set(l)
print("set is:",s)