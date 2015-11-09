###############################################################################
#Todo:
#*Make it so the size of the room can be changed easily using a roomSize variable
#*Figure out how Desika wants the exponential variable to act
#*Make number of time steps its own variable so it can be changed easier
#*Make my own random number generator, this might improve speed
#*Make my own exponential variable function


import random
import matplotlib.pyplot as plott
import matplotlib.animation as anim
import time

roomSize=50
numberOfPeople=50
peopleLocation=0
zombieLocation=0

fig=plott.figure()
ax1=fig.add_subplot(1,1,1)
axes = plott.gca()
axes.set_xlim([0,roomSize])
axes.set_ylim([0,roomSize])
plott.ion()
#plott.show()
#change 50 to roomsize



def createRoom():
	randomLocation=[0,0]
	people=[]
	switch=0

	for i in range(numberOfPeople):
		while people.count(randomLocation)==1:		
			randomLocation=[random.randint(0,roomSize), random.randint(0,roomSize)]
		people.append(randomLocation)
	
	#print people
	return people

def generateNewLocation(peopleLocation2):
	newLocation=[0,1]
	for personNumber in range(len(peopleLocation2)-1):
		while 1:
			newLocation[0]=peopleLocation2[personNumber][0]+random.randint(-2,2)
			newLocation[1]=peopleLocation2[personNumber][1]+random.randint(-2,2)
			if newLocation[0]<roomSize-1 and newLocation[0]>-1:
				if newLocation[1]<roomSize-1 and newLocation[1]>-1:
					peopleLocation2[personNumber][0]=newLocation[0]
					peopleLocation2[personNumber][1]=newLocation[1]
					#print newLocation
					break

	print "New Location Set"
	return peopleLocation2

def checkInfected(people, zombie):
	personNumber=0
	while personNumber < len(peopleLocation)-1:
		personNumber+=1
		for y in range(-2,2):
			for x in range(-2,2):
				for zombieCheck in zombieLocation:

					try:
						#print "personNumber:", personNumber, "\nlen(peopleLocation)", len(peopleLocation)
						if peopleLocation[personNumber][0]+x==zombieCheck[0] and peopleLocation[personNumber][1]+y==zombieCheck[1]:
							
							if random.randint(1,10)>7: 
								zombieLocation.append(people[personNumber])
								peopleLocation.pop(personNumber)
								print "Infected!"
							#print "XXXXXXX"
					except:
						#print "ERROR personNumber:", personNumber, "\nlen(peopleLocation)", len(peopleLocation)
						print "*"*20
						personNumber+=-2
						#raise SystemExit

def plotting(i):
	xcoordpeople=[]
	ycoordpeople=[]
	xcoordzombie=[]
	ycoordzombie=[]

	ax1.clear()
	for y in peopleLocation:
		xcoordpeople.append(y[0])
		ycoordpeople.append(y[1])
	#print peopleLocation
	for x in zombieLocation:
		xcoordzombie.append(x[0])
		ycoordzombie.append(x[1])
	

	ax1.scatter(xcoordpeople, ycoordpeople)
	ax1.scatter(xcoordzombie, ycoordzombie,c="red")
	plott.draw()	


#the locations of all noninfected people
peopleLocation=createRoom()

#the location of all infected people
zombieLocation=[peopleLocation[random.randint(0,numberOfPeople-1)]]

#Initially, we just set the number of time steps to 1. You can change this
for timeStep in range(7000):
	#Generate New Coordinates ie make everyone move
	peopleLocation=generateNewLocation(peopleLocation)
	zombieLocation=generateNewLocation(zombieLocation)
	#print "Step one\n\nLocation of all people:", peopleLocation, "\n\n"

	#Check if anyone is infected
	checkInfected(peopleLocation, zombieLocation)

	#Stop the movement of time when there are no non infected people
	if len(peopleLocation) == 1:
		print "Time to infected:", timeStep 
		break

	#Plotting the points on a scatter plot
	#Comment out to let program run much faster
	plott.show()#
	plotting(1)#


print len(peopleLocation),"*****************"
print peopleLocation,
	
