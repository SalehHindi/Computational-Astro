#pyplot test

import matplotlib.pyplot as plott
import matplotlib.animation as anim
import time

#plott.ion()

coord=[[0,0], [1,1], [2,3], [3,4], [5,6], [7,8]]
bleak=[100,100]

#plott.scatter(coord[2][0], coord[2][1])
#plott.show()

print coord[2][0], coord[2][1]

lisy=[1]
lisx=[0]

fig=plott.figure()
ax1=fig.add_subplot(1,1,1)
def animate(i):
	xcoord=[]
	ycoord=[]

	plott.plot(lisx,lisy)
	for y in coord:
		xcoord.append(y[0])
		ycoord.append(y[1])
	xcoord.append(i)
	ycoord.append(11)

	ax1.clear()
	ax1.scatter(xcoord, ycoord)
	ax1.scatter(bleak[0], bleak[1])

for x in range(10):
	ani=anim.FuncAnimation(fig, animate, fargs=x, interval=1000)
	plott.show()
