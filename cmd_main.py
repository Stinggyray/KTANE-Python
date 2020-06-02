from bomb import Bomb
import modules
import standalone_modules.adjacentletters

solve_methods = {
	"adjacentletters": standalone_modules.adjacentletters.solve,
	"adventuregame": None,
	"alphabet": None,
	"astrology": None,
	"backgrounds": None,
	"bigcircle": None,
	"binaryleds": None,
	"bitwise": None,
	"blindalley": None,
	"booleanvenndiagram": None,
	"bulb": None,
	"button": modules.button.solve,
	"caesarcipher": modules.caesarcipher.solve,
	"cheapcheckout": None,
	"complicatedwires": modules.complicatedwires.solve,
	"combinationlock": None,
	"creation": None,
	"cryptography": None,
	"emojimath": None,
	"flags": None,

}

params = {

}

# A version of this project's driver file, but available for use
# from the command line.
