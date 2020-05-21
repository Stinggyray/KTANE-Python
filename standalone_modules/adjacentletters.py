# All the adjacent letters in KTANE.
arrays = {
	"A": ["GJMOY", "HKPRW"],
	"B": ["IKLRT", "CDFYZ"],
	"C": ["BHIJW", "DEMTU"],
	"D": ["IKOPQ", "CJTUW"],
	"E": ["ACGIJ", "KSUWZ"],
	"F": ["CERVY", "AGJPQ"],
	"G": ["ACFNS", "HOQYZ"],
	"H": ["LRTUX", "DKMPS"],
	"I": ["DLOWZ", "EFNUV"],
	"J": ["BQTUW", "EHIOS"],
	"K": ["AFPXY", "DIORZ"],
	"L": ["GKPTZ", "ABRVX"],
	"M": ["EILQT", "BFPWX"],
	"N": ["PQRSV", "AFGHL"],
	"O": ["HJLUZ", "IQSTX"],
	"P": ["DMNOX", "CFHKR"],
	"Q": ["CEOPV", "BDIKN"],
	"R": ["AEGSU", "BNOXY"],
	"S": ["ABEKQ", "GMVYZ"],
	"T": ["GVXYZ", "CJLSU"],
	"U": ["FMVXZ", "BILNY"],
	"V": ["DHMNW", "AEJQX"],
	"W": ["DFHMN", "GLQRT"],
	"X": ["BDFKW", "AJNOV"],
	"Y": ["BCHSU", "EGMTW"],
	"Z": ["JNRSY", "CLMPV"],
}


def calc_letters(letterlist):
	if None in letterlist:
		print("Invalid arguments. Please try again.")
		return

	for i in range(3):
		for j in range(4):
			cur_lists = arrays[letterlist[i][j]]
			works = False

			for letter in cur_lists[0]:
				if (j > 0 and letterlist[i][j - 1] == letter) or (j < 3 and letterlist[i][j + 1] == letter):
					works = True
					break

			for letter in cur_lists[1]:
				if (i > 0 and letterlist[i - 1][j] == letter) or (i < 2 and letterlist[i + 1][j] == letter):
					works = True
					break

			print(letterlist[i][j] if works else ".", end="")
		print()


def get_input_row():
	row = input()

	if len(row) != 4:
		print("Invalid argument. Please enter that again.")
		return get_input_row()

	return list(row.upper())


print("Input your buttons in this format:")
print("""ABCD
EFGH
IJKL
""")

letters = [get_input_row(), get_input_row(), get_input_row()]

print("Your input:")
print(letters)
print()
print('Buttons to press:')

calc_letters(letters)
