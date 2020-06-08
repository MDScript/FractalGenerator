import pygame, random as r, math

global multiplier
global angle
global colour
#######################
#      EDITABLES      #
#######################
multiplier = 0.6
angle      = 5
colour = (255,255,255)
#######################

pygame.init()
screen = pygame.display.set_mode((700,700))

def line(colour,srt,end):
	pygame.draw.line(screen,colour,[int(srt[0]),int(srt[1])],[int(end[0]),int(end[1])],1);

class Split:
	def __init__(self,age,c1,c2,length,angle,angle2):

		self.angle2 = angle2
		self.age = age

		self.c1 = c1
		self.c2 = c2
		self.length = length

		self.angle = angle/5
		self.instances = []

		if self.age < 10:
			self.instances = [Split(self.age+1,c2,(c2[0] - (math.sin(self.angle)*self.length), c2[1] - (math.cos(self.angle)*self.length)),self.length*multiplier,(self.angle*5)+self.angle2,self.angle2), 
							  Split(self.age+1,c2,(c2[0] - (math.sin(self.angle)*self.length), c2[1] - (math.cos(self.angle)*self.length)),self.length*multiplier,(self.angle*5)-self.angle2,self.angle2)]
		
	def draw(self):
		line(colour,self.c1,self.c2)
		for i in self.instances:
			i.draw()

split  = Split(1,[350,600],[350,500],100*multiplier, angle,angle)
split2 = Split(1,[350,600],[350,500],100*multiplier,-angle,angle)

done = False
while not done:
	screen.fill ((0,0,0))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	split.draw()
	split2.draw()

	pygame.display.update()

pygame.quit()
