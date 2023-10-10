import datetime
tday=datetime.date.today()
print("Today's date is: " ,tday)


import time
timestamp = time.strftime('%H:%M:%S')
print("The time is:" ,timestamp)
h = int(time.strftime('%H'))
m = int(time.strftime('%M'))
s = int(time.strftime('%S'))
if(h>=3 and h<=12):
    print("Good Morning")
elif(h>12 and h<=16):
    print("Good Afternoon")    
elif(h>16 and h<=19):
    print("Good Evening")  
elif(h>19 and h<=23 or h==0):
    print("Good Night")   


  
      
    

