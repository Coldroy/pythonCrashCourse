#This chapter is about the input function, to read data from user input
#message = input("it is test message, blyat\n")
#print(message+" was the input") 
#7.1 - Rental car basic
enteredCar = input("What brand are you looking for?\nAvailable are Subaru, BMW, Ford and Fiat\n")
cars =["SUBARU","BMW","FORD","FIAT"]
subaru = ["Aquele azul la"]
bmw = ["SERIE 1","SERIE 3", "SERIE 5"]
ford = ["FIESTA","FOCUS","FUSION"]
fiat = ["UNO","TEMPRA","STRADA"]
if (enteredCar.upper() in cars):
	print("This Brand has the following models available: ")
	if (enteredCar.upper() == "BMW"):
		for car in bmw:
			print(car.title(),end=' ')

	if (enteredCar.upper() == "SUBARU"):
		for car in subaru:
			print(car.title(),end=' ')

	if (enteredCar.upper() == "FORD"):
		for car in ford:
			print(car.title(),end=' ')
	if (enteredCar.upper() == "FIAT"):
		for car in fiat:
			print(car.title(),end=' ')
else:
	print ("Invalid brand entered")
print()
#Need to improve this code to do less checkings and use less arrays
#7.2 - Restaurant seating
howMany = input("Welcome to chili's, how many people to be seated?\n")

if (howMany.isalpha()):

	print("Invalid input!")
else:
	if (int(howMany) > 8):
		print("A table will be available in the next hour or so.")
	else:
		print("Ok, please follow me right this direction")

#Its important to notice that math.isnan is not correct for this example. This function is to be used only to check 0/0
#and similar results

#7.3 Multiple of 10

value = input("Enter the number to be checked if is multiple of 10\n")
if (value.isalpha()):
	print("Invalid input!")
else:
	if int(value) % 10 ==0:
		print ("That is a multiple of 10!")
	else:
		print("Not a multiple of 10")
