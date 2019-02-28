a=float(input("enter first number"))
b=float(input("enter second number"))
c=float(input("enter third number"))

if (a >= b) and (a >= c):
	largest=a
elif (b >= a) and (b >= c):
	largest=b
else:
	largest=c

print("largest number between",a,",",b,"and",c,"is",largest)