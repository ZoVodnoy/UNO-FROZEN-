import pygame, random
pygame.init()

w, h = 600, 400
sc = pygame.display.set_mode((600, 400))
bg = pygame.transform.scale(pygame.image.load("bg.jpg"), (w, h))

class Card:
	def __init__(self, img, pos, type=None):
		self.sprite = pygame.transform.scale(img, (w//5, h//2))
		self.collide = self.sprite.get_rect(topleft=pos)
		self.drag = False

	def move(self):
		ev = pygame.mouse.get_pressed()
		if ev[0]:
			if self.collide.collidepoint(pygame.mouse.get_pos()):
				self.drag = True
				
	def draw(self):
		if not self.drag:
			sc.blit(self.sprite, self.collide)
		else:
			sc.blit(self.sprite, pygame.mouse.get_pos())

colors = ["blue", "red", "yellow", "green"]
cards = [Card(pygame.image.load(f"/home/eugene/Документы/Programming/git/Zalupa/sprites/uno_assets_2d/PNGs/large/{colors[random.randint(0, len(colors)-1)]}_{i}_large.png"), (100+i*15, h-h//2)) for i in range(10)]

while True:
	sc.fill((0, 0, 0))
	sc.blit(bg, (0, 0))
	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			exit()
	for i in cards:
		i.draw()
		i.move()

	pygame.display.update()