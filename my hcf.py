x = int(input('Enter First Number: '))
y = int(input('Enter Second Number: '))
if x > y:
    s = y
else:
    s = x
for i in range (1,s+1):
    if((x % i == 0) and (y % i == 0)):
        hcf = i
print('The HCF of',x,'and',y,'is',hcf)
#Write a program to Find HCF or GCD of two given numbers