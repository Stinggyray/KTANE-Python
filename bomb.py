import re


# Contains all the edgework stuff about the bomb.


class Bomb:
	def __init__(self, serial_number: str, lit_indicators: list = None, unlit_indicators: list = None,
	             batteries: int = 0, holders: int = 0, ports: list = None, module_count: int = 0, time: float = 0):
		if unlit_indicators is None:
			unlit_indicators = []
		if lit_indicators is None:
			lit_indicators = []
		if ports is None:
			ports = []
		ports = capitalize_list(ports)
		lit_indicators = capitalize_list(lit_indicators)
		unlit_indicators = capitalize_list

		self.serial_number = serial_number
		self.lit_indicators = lit_indicators
		self.unlit_indicators = unlit_indicators
		self.holders = holders
		self.batteries = batteries
		self.ports = ports
		self.module_count = module_count
		self.time = time

		self.aa_batteries = (batteries - holders) * 2
		self.d_batteries = batteries - self.aa_batteries

	def last_digit_serial(self):
		return int(re.match('.+([0-9])[^0-9]*$', self.serial_number).group(1))

	def get_ports_flattened(self):
		return [item for sublist in self.ports for item in sublist]


def capitalize_list(old_list: list):
	for i in range(len(old_list)):
		old_list[i] = old_list[i].upper()
	return old_list
