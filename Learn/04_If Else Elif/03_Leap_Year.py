# Leap Year Code in Python
year = int(input("Enter Year"))
leap = 0

if (year % 4 == 0) and (year % 100 != 0):
    leap = True               # example 2012 % 4 = 0 and 2012 % 100 = 12
elif year % 400 == 0:
    leap = True               # example 2000 % 400 = 0
else:
    leap = False
if leap==True:
    print("Leap Year")
else:
    print("Not Leap Year")
          
