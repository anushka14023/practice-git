# WAP to print all prime number up to 50.

# lower_value = int(input ("Please, Enter the Lowest Range Value: "))  
# upper_value = int(input ("Please, Enter the Upper Range Value: "))  
  
# print ("The Prime Numbers in the range are: ")  
# for number in range (lower_value, upper_value + 1):  
#     if number > 1:  
#         for i in range (2, number):  
#             if (number % i) == 0:  
#                 break  
#         else:  
#             print (number)  

for i in range(1,51):
    if (i >1):
        for j in range(2,i):
            if(i%j ==0):
                break
        else:
            print(i)    

