# myname = input("Enter your name")

# def greetings (name):
# 	print("Welcome " + name + "! Hope you are doing fine.")

# greetings(myname)

def sum (a,b):
	c=a+b
	print("The sum of " + str(a) + " and " + str(b) + " is " + str(c) + ".")


def bmi (name,w,h):
	bmi=w/h
	print("The BMI of " + name + " is " + str(bmi) + ".")

bmi("A",70,1.5)
bmi("B",39,1.23)
bmi("C",50,1.4)