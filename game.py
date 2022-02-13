#Python Text RPG
#Nilupul Rathgama ;)

import cmd
import textwrap
import os
import time
import random
import sys
screen_width = 100

##### Player setup #####
class player:
        def _init_(self): 
                self.name = '',
                self.job = '',
                self.hp = 0,
                self.mp = 0,
                status_effects = [],
                self.location = 'b2',
                self.game_over = False,
myPlayer = player()

##### Title Screen #####
def title_screen_selections():
	option = input("> ")
	if option.lower() == ("player"):
		setup_game() #placeholder until written
	elif option.lower() == ("help"):
		help_menu()
	elif option.lower() == ("quit"):
		sys.exit()
	while option.lower() not in ['play', 'help', 'quit']:
		print("Please enter a valid command.")
		option = input("> ")
		if option.lower() == ("player"):
			setup_game() #placeholder until written
		elif option.lower() == ("help"):
			help_menu()
		elif option.lower() == ("quit"):
			sys.exit()
def title_screen():
	os.system('clear')
	print('##############################')
	print('#  Welcome to the text RPG!  #')
	print('##############################')
	print('- Play -           ')
	print('- Help -           ')
	print('- Quit -           ')
	print('-Copyright 2022 nrathgama.me -')
	title_screen_selections()

def help_menu():

	print('##############################')
	print('#  Welcome to the text RPG!  #')
	print('##############################')
	print('- Use up, down, left, right to move -')
	print('- Type your commands to do them -')
	print('- Use "look" to inspect something -')
	print('- Good luck and Have fun! -') 
	title_screen_selections()

##### GAME FUNCTIONALITY #####
def start_game():

##### MAP #####
        """
a1 a2... # PLAYER STARTS AT b2
---------------
|  |  |  |  | a4
---------------
|  |  |  |  | b4 ...
---------------
|  |  |  |  |
---------------
|  |  |  |  |
---------------
        """
ZONENAME = ''
DESCRIPTION = 'description' 
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
		'b1': False, 'b2': False, 'b3': False, 'b4': False,
		'c1': False, 'c2': False, 'c3': False,'c4': False,
		'd1': False, 'd2': False,'d3': False, 'd4': False,
		 }
zonemap = {
	'a1':{
		ZONENAME: "Town Market",
		DESCRIPTION: 'description',
		EXAMINATION: 'examine',
		SOLVED: False,
		UP: '',
		DOWN: 'b1',
		LEFT: '',
		RIGHT: 'a2',
	},

	'a2':{
		ZONENAME: "Town Entrance",
		DESCRIPTION: 'description', 
		EXAMINATION: 'examine',
		SOLVED: False,
		UP: '',
		DOWN: 'b2',
		LEFT: 'a1',
		RIGHT: 'a3',
	},
	'a3':{
		ZONENAME: "Town Square",
		DESCRIPTION: 'description', 
		EXAMINATION: 'examine',
		SOLVED: False,
		UP: '',
		DOWN: 'b3',
		LEFT: 'a2',
		RIGHT: 'a4',
	},
	'a4':{
		ZONENAME: "Town Hall",
		DESCRIPTION: 'description', 
		EXAMINATION: 'examine',
		SOLVED: False,
		UP: '',
		DOWN: 'b4',
		LEFT: 'a3',
		RIGHT: '',
	},
	'b1':{
		ZONENAME: "",
		DESCRIPTION: 'description', 
		EXAMINATION: 'examine',
		SOLVED: False,
		UP: 'a1',
		DOWN: 'c1',
		LEFT: '',
		RIGHT: 'b2',
	},
	'b2':{
                ZONENAME: "Home",
		DESCRIPTION: 'This is yoour Home!', 
		EXAMINATION: 'Your home looks the same - nothing has changed.',
		SOLVED: False,
		UP: 'a2',
		DOWN: 'c2',
		LEFT: 'b1',
		RIGHT: 'b3',
        },

}

##### GAME INTERACTIVITY #####
def print_location():
	print('\n' + ('#' * (4 + len(myPlayer.location))))
	print('#' + myPlayer.location.upper() + '#')
	print('#' + zonemap[myPlayer.location][DESCRIPTION] + '#')
	print('\n' + ('#' * (4 + len(myPlayer.location))))

def prompt():
	print("\n" + "==================================")
	print("What would you like to do?")
	action = input("> ")
	acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look']
	while action.lower() not in acceptable_actions:
		print("Unknown action, try again. \n")
		action = input("> ")
	if action.lower() == 'quit':
		sys.exit()
	elif action.lower()in ['move', 'go', 'travel', 'walk']:
		player_move(action.lower())
	elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
		player_examine(action.lower())
def player_move(myaction):
	ask = "Where would you like to move to?\n"
	dest = input(ask)
	if dest in ['up', 'north']:
		destination = zonemap[myPlayer.location][UP]
		movement_handler(destination)
	elif dest in ['left', 'west']:
		destination = zonemap[myPlayer.location][LEFT]
		movement_handler(destination)	
	elif dest in ['east', 'right']:
		destination = zonemap[myPlayer.location][RIGHT]
		movement_handler(destination)	
	elif dest in ['south', 'down']:
		destination = zonemap[myPlayer.location][DOWN]
		movement_handler(destination)	

def movement_handler(destination):
	print("\n" + "You have moved to the" + destination + ".")
	myPlayer.location = destination
	print_location()

def player_examine(action):
	if zonemap[myPlayer.location][SOLVED]:
		print("You have already exhausted this zone.")
	else:
		print("You can trigger a puzzle here.")


##### GAME FUNCTIONALITY #####
def setup_game():
	return 

def main_game_loop():
	while myPlayer.game_over is False:
		prompt()
		#here handle if puzzle have been solved, boss defeated, explored everything, etc.

def setup_game():
	os.system('clear')
	
	### NAME COLLECTING
	question1 = "Hello, what's your name?\n"
	for character in question1:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	player_name = input("> ")
	myPlayer.name = player_name

	### JOB HANDLING
	question2 = "Hello, what role do you want to play?\n"
	question2added = "(You can play as a warrior, priest, or mage)\n"
	for character in question2:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	for character in question2added:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.01)
	player_job = input("> ")
	valid_jobs = ['warrior', 'mage', 'priest']
	if player_job.lower() in valid_jobs:
		myPlayer.job = player_job
		print("You are now a " + player_job + "!" "\n")
	while player_job.lower() not in valid_jobs:
		player_job = input("> ")
		if player_job.lower() in valid_jobs:
			myPlayer.job = player_job
			print("You are now a " + player_job + "!" "\n")
	
	### PLAYER STATS
	if myPlayer.job is 'warrior':
		self.hp = 120
		self.mp = 20
	if myPlayer.job is 'mage':
		self.hp = 40
		self.mp = 120
	if myPlayer.job is 'priest':
		self.hp = 60
		self.mp = 60

	### INTRODUCTION
	question3 = "Welcome, " + player_name + " the " + player_job + ".\n"
	for character in question3:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	
	speech1 = "Welcome to this fantasy world!\n"
	speech2 = "I hope it greets you well!\n"
	speech3 = "Just make sure you don't get too lost...\n"
	speech4 = "Hahahaha...\n"
	for character in speech1:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.03)
	for character in speech2:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.03)
	for character in speech3:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.1)
	for character in speech4:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.2)

	os.system('clear')
	print("####################")
	print("# Let's start now! #")
	print("####################")
	main_game_loop()
	
title_screen()






