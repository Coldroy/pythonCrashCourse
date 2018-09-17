#8.9 Magicians
def show_magicians(magicians):
	for magician in magicians:
		print('Magician name: '+magician)

show_magicians(['Karl','Rubick','Saruman'])

#8.10 Great Magicians
#These exercises are to show the difference between reference and copy for listing objects
def make_great(magicians):
#Solution 1: This is a more generic way of solving this problem. Like in almost any language we are able to iterate trough a list
#and re-assign the current value with the new one.
	for i,s in enumerate(magicians):
		magicians[i]='The Great '+magicians[i]
#Solution 2: This is a more elegant solution that uses better the python resources to achieve the same result
#This solution uses what is called "Slice Assignment", that is a function designed for replacing values in a list based in an informed slice
#We could, for example, replace just the first two values with magicians[0:2]. Remembering that [:] means full list, this solution
#enables the possibility of appending text to all objects in a single command line. Pretty neat.
#
#	magicians[:] = ['The Great '+magician for magician in magicians]
#

#8.11 Unchanged Magicians

def make_great_unchanged(magicians):
	return ['The Great '+magician for magician in magicians]



magicians_list=['Karl','Rubick','Saruman']

magicians_copy = make_great_unchanged(magicians_list[:])

show_magicians(magicians_copy) 

show_magicians(magicians_list)
make_great(magicians_list)
show_magicians(magicians_list)

	
