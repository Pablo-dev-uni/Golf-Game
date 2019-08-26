import pygame 
import math
import random
pygame.init()
window = pygame.display.set_mode((1200,500))
pygame.display.set_caption('First Game')



class ball(object):
	def __init__(self, x,y,raduis,colour):
		self.x = x
		self.y = y
		self.raduis = raduis
		self.colour = colour
	def draw(self,window):
		pygame.draw.circle(window,self.colour,(self.x,self.y),self.raduis)		
	 	

def ballPath(startx, starty ,power , ang, time):
	velx = math.cos(ang)*power
	vely = math.sin(ang)*power
	disX = velx*time
	disY = vely*time 
	newx = round(disX+startx)
	newy = round(starty-disY)
	return(newx, newy)
 
def redrawWindow():
	golfball.draw(window)
	pygame.draw.line(window,(225,225,225), line[0],line[1])
	hole.draw(window)
	pygame.display.update()

def findAngle(pos):
	sX = golfball.x
	sY = golfball.y
	try:
		angle = math.atan((sY-pos[1]) / (sX-pos[0]) )
	except:
		angle = math.pi/2
	if pos[1] <sY and pos[0]>sX:
		angle = abs(angle)
	elif pos[1] <sY and pos[0]<sX:
		angle = math.pi- angle
	elif pos[1] > sY and pos[0]<sX:
		angle = math.pi +abs(angle)
	elif pos[1] >sY and pos[0]>sX:
		angle = (math.pi * 2)-angle
	return angle

# Now all the these are the functions used in the later part of the code 

## ALL THE GLOBAL VARIABLES
bci=pygame.image.load("/Users/asad/Desktop/Dev/Background.bmp")

#Starting conditions
x = 0 
y = 0 
time = 0 
power = 0 
angle = 0 
shoot = False

#Starting conditions of the aiming line
xline = 300
yline = 450
vel = 5

#Starting point for the whole
xh = 600
yh = 60
rh = 10
ch = (0,0,0)

#Creates the ball and the hole
hole = ball(xh,yh,rh,ch)
golfball = ball(300,494,5,(255,255,255))


#THE GAME LOOP 


run = True 
while run:
	if shoot == True:
		time += 0.05
		po = ballPath(x,y,power,angle,time)

#CHECKING THE BOUNDRYS
		if po[1]<5:
			shoot = False
		elif po[1]>499:
		 shoot = False
		elif po[0]<5:
			shoot = False
		elif po[0]>1199:
			shoot = False
		else:
			po = ballPath(x,y,power,angle,time)		
		golfball.x = po[0]
		golfball.y = po[1]

		colpix=window.get_at((golfball.x+5,golfball.y+5))

		if colpix == (255,125,54,255):
			shoot = False

#CHECKS IF THE BALL IS IN THE HOL
		if po[0]>= xh and po[0] <=xh:
			if po[1]>=yh and po[1] >= yh:
				hole = ball(xh,yh,rh,ch)
				print("hole in one ")

#STOPS BALL AFTER 10 SECONDS 
		if time>10:
			shoot = False

#FINDS THE DETAILS OF THE AIMING LINE		
	pos  = (xline,yline)
	line = [(golfball.x,golfball.y),pos]

#DRAWS EVERYTHING ON THE SCREEN
	window.blit(bci,[0,0])
	redrawWindow()

#REFRESH RATE OF THE SCREEN
	pygame.time.delay(10)
	
#QUITS THE GAME WHEN THE RED X IS PRESSED
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

#WHEN THE MOUSE IS PRESSED THE BALL IS SHOOT
		if event.type == pygame.MOUSEBUTTONDOWN:
			shoot= True
			x = golfball.x
			y = golfball.y
			time = 0 
			power = math.sqrt((line[0][0]-line[1][0])**2+(line[1][1]-line[0][1])**2)/8
			print(power)
			angle = findAngle(pos)



		
#CONTROLS OF THE AIMING STICK 
	keys = pygame.key.get_pressed()
	
	if keys[pygame.K_LEFT]:
		xline -=vel
	if keys[pygame.K_RIGHT]:
		xline +=vel
	if keys[pygame.K_UP]:
		yline -=vel
	if keys[pygame.K_DOWN]:
		yline +=vel

	


pygame.quit()