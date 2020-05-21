from bomb import Bomb
from termcolor import cprint


def solve_button(bomb: Bomb, word: str, color: str):
	cprint('The Button', 'yellow', attrs=['reverse'])
	# Preprocessing
	word = word.upper()
	color = color.upper()

	# True is press and hold
	# False is press and release
	result = None
	if word == "ABORT" and color == "BLUE":
		result = True
	elif bomb.batteries > 1 and word == "DETONATE":
		result = False
	elif color == "WHITE" and "CAR" in bomb.lit_indicators:
		result = True
	elif bomb.batteries > 2 and "FRK" in bomb.lit_indicators:
		result = False
	elif color == "YELLOW":
		result = True
	elif color == "RED" and word == "HOLD":
		result = False
	else:
		result = True

	if result:
		print("Press and hold the button. Then observe the strip color.")
		cprint("Blue: 4", 'blue')
		cprint("Yellow: 5", 'yellow')
		print("Anything else: 1")
	else:
		print("Press and IMMEDIATELY release.")
