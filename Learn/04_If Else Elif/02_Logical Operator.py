# Logical operator are 'AND' ,'OR' ,'NOT' etc

# And:- Checks the both condition are true of false

num1 = 100
num2 = 200
num3 = 300
if (num3 >= num2 and num1 <= num2):
    print("Condition is true")  # 300 > 200 ture and 100 < 200 true
else:
    print("Condition is not true")

# OR:- Checks at least one condition is true

a = 300
b = 200
c = 500
if a > b or a > c:  # 300 > 200 true or 300 > 500 false
    print("one of the conditions is True")

# NOT:- is used to reverse the conditional statement:
age1 = 30
age2 = 100
if not age1 > age2:
    print("age1 is NOT greater than age2")
