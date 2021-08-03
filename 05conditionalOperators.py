""" num1,operator,num2 = input("Enter calculation : ").split()
num1 = int(num1)
num2 = int(num2)
if operator == "+":
    print("{}{}{}={}".format(num1,operator,num2,(num1+num2)))
elif operator == "-":
    print("{}{}{}={}".format(num1,operator,num2,(num1-num2)))
elif operator == "*":
    print("{}{}{}={}".format(num1,operator,num2,(num1*num2)))
elif operator == "/":
    print("{}\n {}\n {}\n =\n {}".format(num1,operator,num2,(num1/num2)))
else:
    print('Invalid operation') """

""" #logical operators
age = int(input("Enter age : "))
if age < 5:
    print("Go to kindergarten")
elif age >= 5 and age < 18:
    print("Go to grade : {}".format(age-5))
else:
    print("Go to college") """

#ternary operator
age  = int(input("Enter age : "))
can_vote = True if age >= 18 else False
print("Can Vote? {}".format(can_vote))