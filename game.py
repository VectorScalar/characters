#Main Game File

from Player import *
from Commands import *
from util import *
from item import *
from weapon import *
import pygame
from pygame.locals import *

def help(player, args):
  for command in commands:
		print (command)

commands = {
	'help' : help,
	'exit' : exit,
	'inv' : inv,
	'movement' : movement,
	'startDisplay' : startDisplay
}

invisible = {
	'quit' : exit,
}

player = Player("Default", 1, 1, 1)

def nameInput(prompt):
	name = raw_input(prompt)
	name.strip()
	return name

def getName():

	tempName = ("")
	while 1:
		tempName = nameInput("What is your name?")

		if len(tempName) < 1:
			continue

		yes = yesOrNo(tempName + ", is that your name?")

		if yes:
			return tempName
		else:
			continue


def isValidCMD(cmd):
	if cmd in commands:
		return True
	elif cmd in invisible:
		return True
	return False

def runCMD(cmd, args, player):
	if cmd in commands:
		commands[cmd](player, args)
	elif cmd in invisible:
		invisible[cmd](player, args)


def main(player):

	player.name = getName()

	while (not player.dead):
		line = raw_input(">> ")
		words = line.split()
		words.append("Invalid Command")

		if isValidCMD(words[0]):
			runCMD(words[0], words[1], player)

potion = Item("Potion", 5, 2)
lizard = Item("Magical Lizard", 900000)

player.inventory.add(potion)
player.inventory.add(lizard)

def pygameinit(KeyEvents):
	pass

main(player)
