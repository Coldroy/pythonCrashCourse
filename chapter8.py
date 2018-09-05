#8.1 Message
def display_message():
	print('Nathing')

display_message()

#8.2 Favorite Book
def favorite_book(book):
	print("Really? Your favorite book is "+book+"? Lame.")

favorite_book("Harry Potta")

#8.3 T-shirt

def make_shirt(size,text):

	make_shirt('M','Apenas Desista')
	make_shirt(text='Apenas Desista',size='XXL')

#8.4 Large Shirts

def make_shirt2(size='L',text='I Love Python'):
	print('Printing an '+size+' shirt saying: '+text)

make_shirt2('M')
make_shirt2()

#8.5 Cities

def describe_city(city,country='Brazil'):
	print(city +' is in '+country)

describe_city('Iguatu')
describe_city('Warszawa','Poland')
describe_city(country='England',city='London')
