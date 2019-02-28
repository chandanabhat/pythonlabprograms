import random

d = 0
p = 0

while True:
	r=input("press r to roll,q to quit:")

	if r=='r':
		d=random.randint(1,6)
		print("you got:",d)
		if d==6:
			print("congratulaions,you can play now.")
			break
		else:
			print("roll again,till you get 6")

while True:
	r=input("press r to roll,q to quit:")

	if r=='r':
		d=random.randint(1,6)
		print("you got:",d)
	snl={8:37,13:34,40:68,52:81,76:97,11:2,25:4,38:9,65:46,89:70,93:64}

		p=p+d
		if p>100:
			p=p-d
			print("wait,till you get",100-p,"or less.")

		print("your new position is :",p)

		if p==100:
			print("hurray!you won the game")
			exit()
		if p==8:
			p=37
			print("wow,a ladder.sgo up to ",p)
		if p==13:
			p=34
			print("wow,a ladder.go up to",p)
		if p==40:
			p=68
			print("wow,a ladder.go up to",p)
		if p==52:
			p=81
			print("wow,a ladder.go up to",p)
		if p==76:
			p=97
			print("wow,a ladder.go up to",p)
		if p==11:
			p=2
			print("oops!snake is here.go back to",p)
		if p==25:
			p=4
			print("oops!snake is here.go back to",p)
		if p==38:
			p=9
			print("oops!snake is here.go back to",p)
		if p==65:
			p=46
			print("oops!snake is here.go back to",p)
		if p==89:
			p=70
			print("oops!snake is here.go back to",p)
		if p==93:
			p=64
			print("oops!snake is here.go back to",p)

	elif r=='q':
		print("bye!")
		exit()




        	
s