from bomb import Bomb
import modules


# The driver file for this project.
# Here, we execute all code to solve our bombs.

# -------------------#
# EDGEWORK           #
# -------------------#

current_bomb = Bomb(
	'EJ4PA3', # serial number
	lit_indicators=['CLR'],
	unlit_indicators=['IND'],
	batteries=5,
	holders=3,

	ports=[

	],

	module_count=5,
	time=60
)


# -------------------#
# SOLVING MODULES    #
# -------------------#
modules.button.solve(current_bomb, 'red', 'hold')
