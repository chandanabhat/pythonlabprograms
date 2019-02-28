import random
l=['r','p','s']
d={'r':"rock",'p':'paper','s':'scissor'}
uc=0
cs=0
while True:
	#take input from the user
	u=input("enter your choice , press n to discontinue")
	#to exit
	if u=='n':
		print("game over")
		print("computer scores:",cs)
		print("user scores",uc)
		if cs==uc:
			print("tie")
		elif cs > uc:
			print("computer wins")
		else:
			print("user wins")
		exit()
	#input from the computer
	c=random.choice(l)
	print("computer chooses:",d[c])
	print("user chooses:",d[u])
	#compare the user and computer choice
	if u==c:
		print("tie")
	
	elif u=='r' and c=='p':
		print("comp wins")
		cs+=1
	elif u=='r' and c=='s':
		print("user wins")
		uc+=1

	elif u=='p' and c=='s':
		print("user wins")
		uc+=1
	elif u=='p' and c=='r':
		print("comp wins")
		cs+=1
	elif u=='s' and c=='r':
		print("comp wins")
		cs+=1
	elif u=='s' and c=='p':
		print("user wins")
		uc+=1

	

	

		

	