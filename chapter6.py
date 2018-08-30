#Dictionaries
wine1 = {"color":"red", "grape":"cabernet sauvignon"}
wine2 = {"color":"white", "grape":"cabernet blanche"}
wine3 = {"color":"red", "grape":"merlot"}
wines = []
wines.append(wine1)
wines.append(wine2)
wines.append(wine3)
for wine in wines:
	print("Color: "+wine['color']+"\tGrape: "+wine['grape'])
print("\n")
for wine in wines:
	wine['region'] = 'California'
for wine in wines:
	print("Color: "+wine['color']+"\tGrape: "+wine['grape']+"\tRegion: "+wine['region'])

#------------------
#Empty dictionary
#-----------------
carpart1 = {}
carpart1['name'] = 'tyre'
carpart1['price'] = 250.0
carpart1['category'] = 'wheels'
carpart2 = dict(carpart1)
carpart2['name'] = 'rim'
carpart2['price'] = 2500
print(carpart1)
print(carpart2)
for key, value in carpart1.items():
	print('\nKey: '+key)
	print('Value: ')
	print (value)
for key in carpart2.keys():
	print('\nOnly key value ' + key)
