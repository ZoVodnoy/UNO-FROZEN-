
class App:
	def __init__(self):
		self.w, self.h = 800, 600
		self.sc = pygame.display.set_mode((self.w, self.h))
		self.align = self.w // 10 - 2
		self.bg = pygame.transform.scale(pygame.image.load("bg.jpg"), (self.w, self.h))
		self.clock = pygame.time.Clock()
		self.sprites = [pygame.transform.scale(pygame.image.load(f"sprites/uno_assets_2d/PNGs/large/{i}"), (self.w//10, self.h//4)) for i in os.listdir("sprites/uno_assets_2d/PNGs/large")]
		random.shuffle(self.sprites)
		self.players = []
		self.players_counter = 0

	def draw(self):
		self.sc.fill((0, 0, 0))
		self.sc.blit(self.bg, (0, 0))
		

	def run(self):
		while True:
			self.clock.tick(60)
			self.draw()
			for i in pygame.event.get():
				if i.type == pygame.QUIT:
					exit()
				if i.type == pygame.KEYUP:
					if i.key == pygame.K_n:
						self.players.append(Player())
						self.players_counter += 1 
			for i in self.players:
				i.update()

			pygame.display.update()


class Player:
	def __init__(self, name="Bot"):
		self.name = f"{name}_{app.players_counter}"
		self.card_array = [Card(app.sprites[i], (app.align * i, app.h-app.h//4), i) for i in range(len(app.players)*7-7)]
		self.current_card = None
		print(self.name)

	def update(self):
		for i in self.card_array:
			if not i.do_pack and not self.current_card == None:
				i.collide.center = (w//2, h//2)
			else:
				i.move()
			i.draw()


class Card:
	def __init__(self, img, pos, num, type=None): #
		self.sprite = pygame.transform.scale(img, (app.w//10, app.h//4))
		if app.players_counter > 2:
			pos = (pos[0], 0)
		self.collide = self.sprite.get_rect(topleft=pos)
		self.do_pack = random.randint(0, 1)
		self.drag = False
		self.num = num

	def move(self):
		ev = pygame.mouse.get_pos()
		if ev[0]:
			m_pos = pygame.mouse.get_pos()
			if self.collide.collidepoint(m_pos):
				self.drag = True
			if self.drag:
				self.collide.center = m_pos
		else:
			self.drag = False

	def draw(self):
		app.sc.blit(self.sprite, self.collide)
		

if __name__ == '__main__':
	import pygame, random, os
	pygame.init()
	app = App()
	app.run()