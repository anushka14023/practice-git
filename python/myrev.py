n = 12345
r = 0
while(n > 0):
    ld = n % 10
    r = r * 10 + ld
    n= n // 10
print('The reverse number is =', r)
# WAP to Reverse a number using while loop in Python.