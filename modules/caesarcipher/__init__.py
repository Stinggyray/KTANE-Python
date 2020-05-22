from bomb import Bomb
from caesarcipher import CaesarCipher
from termcolor import cprint


def solve(bomb: Bomb, display: str = None):
	cprint('Caesar Cipher', 'yellow', attrs=['reverse'])
	offset = 0
	if bomb.serial_has_vowel():
		offset -= 1

	offset += bomb.batteries
	if bomb.serial_last_digit() % 2 == 0:
		offset += 1
	if 'CAR' in bomb.get_all_indicators():
		offset += 1
	if 'PARALLEL' in bomb.get_all_ports() and 'NSA' in bomb.lit_indicators:
		offset = 0

	cprint('Offset: ' + str(offset), 'green')
	if display:
		cipher = CaesarCipher(display, offset=offset)
		cprint(cipher.encoded, 'cyan')
