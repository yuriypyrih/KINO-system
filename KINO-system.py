# ICSD16157 YURIY PYRIH
import random

print "Welcome to the KINO"

KINOtable = ((0,2.5),(0,1,5),(0,0,2.5,25),(0,0,1,4,100),
(0,0,0,2,20,450),(0,0,0,1,7,50,1600),(0,0,0,1,3,20,100,5000),
(0,0,0,0,3,10,50,1000,15000),(0,0,0,0,1,5,25,200,4000,40000),
(2,0,0,0,0,2,20,80,500,10000,100000),(2,0,0,0,0,1,10,50,250,1500,15000,500000),
(4,0,0,0,0,0,5,25,150,2500,25000,1000000))

#Input the numbers 1-12
while True :
	numbers = int(raw_input("How many numbers do you like play with? [1-12]: "))
	if numbers>0 and numbers<13 :
		break
	print "Invalid number";

#Input the range 1-80 for each previous number
list = []
print "Now choose a KINO number for " + str(numbers) + " numbers"
counter = 1
while counter <= numbers :
	while True :
		print "KINO number:" + str(counter) + ")"
		KINOnumber = int(raw_input("Choose[1-80]: "))
		if KINOnumber>0 and KINOnumber<81 :
			if KINOnumber in list :
				print "You have already wrote that number!\n"
				break
			list.append(KINOnumber)
			counter += 1
			break
		print "Invalid number\n"

#Choosing the amount of money
while True :
	money = int(raw_input("Choose the amount of money to play (1,2,5,10) euro : "))
	if money in (1,2,5,10) :
		break
	print "Invalid amount of money.."
		
#Choosing KINO numbers randomly by the system
KINOrandoms = [];
chosen = 1
while chosen<=20 :
	temp = random.randint(1,80)
	if temp not in KINOrandoms :
		KINOrandoms.append(temp)
		chosen += 1

#Print the KINO numbers to console
showKINO = ""
for KINOnum in KINOrandoms :
	showKINO += str(KINOnum) + " "
print "\nKINO random numbers: " + showKINO

#Caclulate and Print the award
successes = 0;
for point in list :
	if point in KINOrandoms :
		successes += 1
award = money * KINOtable[numbers-1][successes]
print "Your award is " + str(award) + " euro!"


#Just for clarity
raw_input("\n\npress Enter to exit..");