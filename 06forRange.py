""" investment = float(input("Enter investment amount : "))
print("Year , Interest , Investment ")
for year in range(10):
    interest = investment * 0.07
    investment = investment + interest 
    print("{}   {:.2f}  {:.2f}".format(year,interest,investment)) """

#Odd Even
for number in range(1,21):
    if number % 2 != 0:
        print(number)