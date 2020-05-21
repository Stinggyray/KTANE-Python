from bomb import Bomb
import modules


# The driver file for this project.
# Here, we execute all code to solve our bombs.

# -------------------#
# EDGEWORK           #
# -------------------#

current_bomb = Bomb(
	"ABCDEF", # serial number
	lit_indicators=["NSA"],
	unlit_indicators=[],
	batteries=2,
	holders=1,

	ports=[
		[],
		["RJ", "RCA"]
	],

	module_count=15,
	time=20
)


# -------------------#
# SOLVING MODULES    #
# -------------------#
modules.button.solve_button(current_bomb, "why", "red")