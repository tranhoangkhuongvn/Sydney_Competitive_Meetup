'''
Give an excel cell reference (eg. 'B11' or 'ABC101' convert this to a 0-index coordinate system)

'''

test = 'AAA2'
col = ''
row = ''
for i in range(len(test)):
	if test[i].isdigit():
		row += test[i]
	else:
		col += test[i]


def calculator(letter):
	alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

	number = 0

	if len(letter) == 1:
		position = alphabet.find(letter[0]) + 1
		number = position

	if len(letter) == 2:
		position1 = alphabet.find(letter[0]) + 1
		position2 = alphabet.find(letter[1]) + 1
		number = position1 * 26 + position2

	if len(letter) == 3:
		position1 = alphabet.find(letter[0]) + 1
		position2 = alphabet.find(letter[1]) + 1
		position3 = alphabet.find(letter[2]) + 1
		number = position1 * 26 * 26 + position2 * 26 + position3

	number -= 1
	return number

final_col = calculator(col)
final_row = int(row) - 1
print((final_row, final_col))
