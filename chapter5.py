cars = ['BMW','Mercedes','Toyota','Subaru']
for car in cars:
	if car == "Mercedes":
		print(car.upper())
	else:
		print(car.lower())
cars2 = ["FIAT","Renault","BMW", "Peugeout", "Toyota"]
for car in cars2:
	if car in cars:
		print(car+" is in first array")
	else:
		print(car+" is not in first array")
