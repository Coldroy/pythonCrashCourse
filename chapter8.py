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

#8.6 Formatted city names

def city_country(city,country):
	return city.title()+', '+country.title()
	

print(city_country('Santiago','Chile'))
print(city_country('Wroclaw','Poland'))
print(city_country('London','England'))

#8.7 Make Album

def make_album(artist,title,num_tracks=''):
	album = {artist:title,'tracks':num_tracks}
	return album

print(make_album('Blind Guardian','At the edge of time'))
print(make_album('MGMT','Little Dark Age',12))

#8.7 User Albuns
# Need to improve with validations and better if comparison
while True:
	print ('Press q to exit at any time')
	artist = input('What artist shall be used? ')
	if artist == 'q':
		break
	title = input('What is the album title? ')
	if title == 'q':
		break
	print(make_album(artist,title))

#8.8 Magicians
def show_magicians(magicians):
	for magician in magicians:
		print('Magician name: '+magician)

show_magicians(['Karl','Rubick','Saruman'])
