#8.12 Sandwiches
def make_sandwich(*ingredients):
	print('This sandwich contains:')
	for ingredient in ingredients:
		print('- '+ingredient)

make_sandwich('corn')
make_sandwich('cheese','steak')
make_sandwich('ham','cheese','lettuce')

#8.13 User Profile
def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	profile = {}

	profile['first_name'] = first
	profile['last_name'] = last

	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('albert', 'einstein',
			    location='princeton',
			    field='physics')
print(user_profile)

user_profile = build_profile('jon','doe',location='Kiev',age=19,profession='student')

print(user_profile)


def make_car(make,model,**attributes):
	car={}
	car['make']=make
	car['model']=model
	for key,attribute in attributes.items():
		car[key]=attribute
	return car
car = make_car('subaru','outback',color='blue',tow_package=True)
print(car)
