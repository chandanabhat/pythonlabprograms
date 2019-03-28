class student:
	h=0

	def __inhit__(self):
		self,h=5

	def my_func(self,k):
		print("hii! i am in the class")
		self.h=k
		print(self.h)
o=student()
print(o.h)
o.my_func(7)
o.my_func(6)