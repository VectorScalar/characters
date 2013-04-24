class Character(object):
  def __init__(self, name, hp, strength):
	    self.name = name
	    self.hp = hp
	    self.str = strength
	    self.dead = False

	def update(self):
		if self.hp < 0:
			self.dead = True
			self.hp = 0
