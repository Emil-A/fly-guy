from __future__ import division
import time, random 

def welcome():
	# Welcome stament and prompts user to adjust terminal 
	print "Welcome to FLY GUY!"
	print "You are a pilot underattack, dodge the missiles left(1) and right(2) and enter"
	print "                          /\\"
	print " " * 472
	print 
	print "<        Fit screen to arrows and hit enter        >"
	print " " * 472
	print "                          \/"
	useless = (raw_input(""));

def game():
	# Takes first striped character value to use as an icon
	user = (raw_input("Choose a plane -> "));
	print "Hit enter to start!"
	user = user.strip()    
	user = user[:1]
	if user == "" or user == "^":
		user = "*"
	# Variable list
	spaces = 25
	proj2 = 100
	proj3 = 100
	fin_proj = 100
	name = " "
	turns = -1
	lives = 3
	score = 0
	timeout = 10
	room = 20
	start = time.time()
	stop = time.time()
	
	while lives > 0:
		turns += 1
		if room > 2:
			room -= 1
		reason = ""
		score = turns * 100
		if turns % 10 == 0 and turns > 0:
			timeout = timeout / 1.5
		# Loops "^" at random spaces to create illusion of movement
		print(" " * fin_proj + "^")
		print(" " * spaces + user) 
		# Gets random value of spaces to shoot missiles(^) in range close to user 
		proj = random.randint((spaces - room), (spaces + room))
		if proj > 50:
			proj -= room
		# Loops the first and second last missiles (^) every odd turn
		if turns % 2 != 0: 
			print " " * proj3 + "^"
			print " "
			print " " * proj + "^"
			proj2 = proj
			fin_proj = proj3
		# Loops the first and second last missiles (^) every even turn
		if turns % 2 == 0: 
			print " " * proj2 + "^"
			print " "
			print " " * proj + "^"
			proj3 = proj
			fin_proj = proj2
		# Life loss when user takes too long or gets hit
		if stop-start > timeout:
			lives -= 1
			reason = "TIMEOUT"
		if spaces == fin_proj:
			lives -= 1
			fin_proj = 100
			reason = "HIT"
		# Prints shooter
		print " " * proj + "~"
		# Displays info
		print "_" * 51
		life_diplay = "<3" * lives
		print "Score: %s  %s  Time:%ss  Turn:%ss  %s"%(score, life_diplay, round(timeout, 2), round(stop-start, 2), reason)
		print "_" * 51
		# Times users move
		start = time.time()
		move = (raw_input(""));
		stop = time.time()
		# User moves left(1) and right(2) but can't exit area(50 spaces)
		if move.startswith("2"):
			spaces += 1
					
		if move.startswith("1"):
			spaces -= 1
		
		if spaces > 50:
			spaces -= 1
		
welcome()
game()
print "                   GAME OVER!"
play_again = (raw_input("                   Play again? "));
while play_again.startswith("y"):
	game()
	print "                   GAME OVER!"
	play_again = (raw_input("                   Play again? "));
print "               Thanks for playing!"
