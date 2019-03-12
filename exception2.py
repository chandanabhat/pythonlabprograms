l=[1,2,3,4,5,6]
try:
	s=len(l)
	if s>4:
		raise TypeError
	print(d[1])

except TypeError:
	print("error!!!lenght should be less than or equals to 4")
except NameError:
	print("index out of range")
else:
	for i in l:
		print(i)
finally:
	print("execution done!!!")

