''''Lists'''
a = []
name = input("Enter 5 name")
a.append(name)
name = input()
a.append(name)
name = input()
a.append(name)
name = input()
a.append(name)
name = input()
a.append(name)

print(a)

a = ['z', 'b', 'c', 'd']
print(a)
print(a[0])
print(a[3])
print(a[-1])
print(len(a))
a.append('e')
print(a)
a[0] = 'x'
print(a)

print(['y']+a)

print(a[1:3])  #a[1:2] 1, 2-1 = 1