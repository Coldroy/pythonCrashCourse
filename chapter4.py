guests =  []
guests.append("Ednaldo Pereira")
guests.append("Pedro Bial")
guests.append("Boneco do Posto")
guests.append("Coxinha")
for guest in guests:
	print("Que maravilha! O convidadeo "+guest.title()+" chegou a festa!")
	print("Trás a bebida que pisca!")
print("Chegou quem tinha que chegar, segue o baile")
#
#
#
# Listas numericas
#
#
#
for number in range(0,5):
	print ("Numero no range: "+str(number))
print("\n")
for number in range(-5,-1):
	print ("Numero no range: "+str(number))
print("\n")
for number in range(-1,-5,-1):
	print ("Numero no range: "+str(number))
print("\n")
numeric_list = []
for number in range (1,11):
	numeric_list.append(number**2)
print (max(numeric_list))
print (min(numeric_list))
print (sum(numeric_list))
for number in range (1,1000000):
	numeric_list.append(number)
print (sum(numeric_list))
#
#
#
#Fatias da lista
#
#
#
whole_list = ["minhoca","mandinca","maniroba","macaxeira","momentinho","mandarim","marmelada","minguante"]
print(whole_list[3:6])
print(whole_list[:6])
print(whole_list[6:])
print(whole_list[-4:])
print("\n")
limite = 3
for element in whole_list[:limite*-1]:
	print(element)
#
#
#
#Tuplas
#
#
#
tuple_eg = (1,3,5)
print(tuple_eg[0])
