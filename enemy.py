from character import *

class Enemy(Character):
  def __init__(self, name, hp, str):
		Character.__init__(self, name, hp, str)

		self.hp = 100

		if self.hp <= 0:
			print ("Enemy Dead")
