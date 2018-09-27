'''
Created on Sep 25, 2018

@author: Thomas Pietra
Operations parctice
'''

print("Welcome to the test score calculator.")
print("\n\n\n\n")
test1=float(input("Please enter the first test score: "))
test2=float(input("Please enter the second test score: "))
test3=float(input("Please enter the third test score: "))

#calculate the average
average=(test1+test2+test3)/3

#display the output
print("Average test score:",average)


input("Press enter to find the slope between two points")

x1=int(input("Please enter x1: "))
x2=int(input("Please enter x2: "))
y1=int(input("Please enter y1: "))
y2=int(input("Please enter y2: "))

dx=x2-x1
dy=y2-y1

print("The slope is",dy,"/",dx)


price=float(input("please input the price: "))
tax=price*0.06
total=price+tax
print("the tax is $",tax,"the total is $",total)