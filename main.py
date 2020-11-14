from bomb import Bomb
import modules


# The driver file for this project.
# Here, we execute all code to solve our bombs.

# -------------------#
# EDGEWORK           #
# -------------------#

current_bomb = Bomb(
	'W16QA5', # serial number
	lit_indicators=[],
	unlit_indicators=['BOB'],
	batteries=3,
	holders=2,

	ports=[

	],

	module_count=5,
	time=60
)


# -------------------#
# SOLVING MODULES    #
# -------------------#
modules.button.solve(current_bomb, 'red', 'hold')
