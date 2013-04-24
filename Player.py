from character import *
from container import *
from weapon import *
from enemy import *
from pygame.locals import *

class Player(Character):
  def __init__(self, name, hp, strength, int):
		Character.__init__(self, name, hp, strength)
		self.int = int
		self.inventory = Container("Inventory")

	def die(self):
		self.hp = 0
		self.dead = True
		input()

	
