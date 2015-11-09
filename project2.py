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
vaccLocation=[[25,25],[25,26],[26,25],[26,26]]

fig=plott.figure()
ax1=fig.add_subplot(1,1,1)
plott.ion()

#the two variables below are so the pyplot screen doesn't constantly resize.
#The white points indicate the room border 
xborderpoint=[0,0,roomSize, roomSize]
yborderpoint=[roomSize, 0, roomSize, 0]


#Sets up a room of size roomSize and fills it with people.
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

#generateNewLocation() generates new location for every moving person. It checks whether they are in bounds on the room
#and whether they are too close to a vaccinated person.
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

#	print "New Location Set"
	return peopleLocation2

#checkInfected() checks whether a person within a certain pixel radius is infected and infects non infected people
#within that radius based on some probability
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
							
							#There is a 30% chance that someone will be infected if within range
							if random.randint(1,10)>7: 
								zombieLocation.append(people[personNumber])
								peopleLocation.pop(personNumber)
#								print "Infected!"
							#print "XXXXXXX"
					except:
						#print "ERROR personNumber:", personNumber, "\nlen(peopleLocation)", len(peopleLocation)
						print "*"*20
						personNumber+=-2
						#raise SystemExit

#plotting() is responsible for plotting the all the people in pyplot and animating the plot
#Note: I should replace all the variables with one large list of length 3. That will make my code cleaner.
def plotting(i):
	xcoordpeople=[]
	ycoordpeople=[]
	xcoordzombie=[]
	ycoordzombie=[]
	xcoordvacc=[]
	ycoordvacc=[]

	ax1.clear()
	for x in peopleLocation:
		xcoordpeople.append(x[0])
		ycoordpeople.append(x[1])
	#print peopleLocation
	for y in zombieLocation:
		xcoordzombie.append(y[0])
		ycoordzombie.append(y[1])
	for z in vaccLocation:
		xcoordvacc.append(z[0])
		ycoordvacc.append(z[1])

	ax1.scatter(xborderpoint,yborderpoint,c="white")
	ax1.scatter(xcoordpeople, ycoordpeople,c="black")
	ax1.scatter(xcoordzombie, ycoordzombie,c="red")
	ax1.scatter(xcoordvacc, ycoordvacc,c="blue")
	
	plott.draw()	


#vaccinate() will create a list of vaccinated people and specify their properties
def vaccinate():
	randomperson=random.randint(0,len(peopleLocation)-1)
	vaccLocation.append(peopleLocation[randomperson])
	peopleLocation.pop(randomperson)
	

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

	#Vaccinate a random person every 3rd timeStep
	if timeStep%3 == 0: vaccinate()

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
	
