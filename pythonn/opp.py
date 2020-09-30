class HomeMember:
	def __init__(self,angle1,angle2,angle3):
		self.angle1 = angle1
		self.angle2 = angle2
		self.angle3 = angle3

	def is_triangle(self):
		# print(f'Member name is {self.name}\n Member age is {self.age}\n Member height is {self.height}')
		x = int(self.angle1) + int(self.angle2) + int(self.angle3)
		if x == 180:
			return True
		return False
ang1 = input('write first ange of triangle ')
ang2 = input('write second ange of triangle ')
ang3 = input('write third ange of triangle ')

triangle = HomeMember(ang1,ang2,ang3)
print(f'is this a triangle? {triangle.is_triangle()}')