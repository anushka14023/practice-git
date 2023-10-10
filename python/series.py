# WAP to print the following output:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
for i in range(1,5):
    for j in range(0,i):
        print(i,end=" ")
    print("")
# 1
# 12
# 123
# 1234
# 12345
row=5
for i in range (1,row+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("")
# A
# AB
# ABC
# ABCD
# ABCDE

rows=70
for i in range(65,rows):
    for j in range(65,i+1):
        print(chr(j),end=" ")
    print("")
# ABCDE
# ABCD
# ABC
# AB
# A
rows=70
for i in range(64,rows):
    for j in range(rows-1,i,-1):
        print(chr(j),end=" ")
    print("")
