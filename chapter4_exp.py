numeric_list = []
for number in range (1,11):
	numeric_list.append(number**2)
print("Lista preenchida")
print (numeric_list)
numeric_copy=numeric_list[:]
while (numeric_list):
	numeric_list.pop()
	print(numeric_list)
print(numeric_copy)
