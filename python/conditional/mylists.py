# if 'hungry':
#     print("1") 
# elif 'tired':
#     print("2")
    
l=[1,1,2,5,4,6]
print(l)
l.append(7)
l.sort()
l.insert(1,899)
print (l)
m=[21,22,23]
k=l+m
l.extend(m)#changes m
print(l)
print(k)

l.reverse()
print(l)
print(l.index(1))

m=l
m[0]=0
print(l)
m=l.copy()
m[5]=8
print(l)
print(m)
l=["l",["k"]]
print(l)
