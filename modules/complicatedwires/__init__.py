from bomb import Bomb
from termcolor import cprint


# Format: RBSL (letters)
def solve(bomb: Bomb, wires: list):
	cprint('Complicated Wires', 'yellow', attrs=['reverse'])
	cprint('Green: Cut', 'green')
	cprint('Red: Do not cut', 'red')
	print('---')
	cprint('Your wires:', 'blue')
	for wire in wires:
		wire = wire.upper()
		cur_wire_str = ''
		if 'R' in wire:
			cur_wire_str += 'R'
		if 'B' in wire:
			cur_wire_str += 'B'
		if 'S' in wire:
			cur_wire_str += 'S'
		if 'L' in wire:
			cur_wire_str += 'L'
		
		cut = False
		if cur_wire_str in ['', 'S', 'RS']:
			cut = True

		elif cur_wire_str in ['R', 'B', 'RB', 'RBL']:
			if bomb.serial_last_digit() % 2 == 0:
				cut = True

		elif cur_wire_str in ['BL', 'BSL', 'RBS']:
			if 'PARALLEL' in bomb.get_all_ports():
				cut = True

		elif cur_wire_str in ['RL', 'RSL', 'SL']:
			if bomb.batteries > 2:
				cut = True

		cprint(wire + ' | ' + ('Cut' if cut else 'Do not'), 'green' if cut else 'red')

		

