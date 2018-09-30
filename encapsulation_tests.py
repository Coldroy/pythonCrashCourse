class Dog:
	def __init__(self,test_att):
		self.weight = test_att
		__color =''
	def set_color(self,color):
		self.__color = color
	def get_color(self):
		print(self.__color)
rex = Dog(59)
rex.set_color('Black')
rex.get_color()
rex.color = 'White'
rex.__color = rex.color
print(rex.__color)
rex.get_color()
