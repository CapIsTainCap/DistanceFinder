# Distance Finder with Python
import math 

def distance():
	print("\nDistance Finder\n")
	x1 = float(input("Enter the first x coordinate (x1): "))
	y1 = float(input("Enter the first y coordinate (y1): "))
	x2 = float(input("Enter the second x coordinate (x2): "))
	y2 = float(input("Enter the second y coordinate (y2): "))

	def res():
		restart = input("Do you want to try again? [yes/no]: ")
		if restart.lower() == "yes":
			distance()
		elif restart.lower() == "no":
			print("Thank you for using this application.")
		else:
			print("Please enter either yes or no.")
			res()
	
	print("The distance between (",x1,",",y1,") and (",x2,",",y2,") is " , math.sqrt((x2-x1)**2 + (y2-y1)**2),"units.")
	res()

distance()


