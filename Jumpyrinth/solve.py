import string

file = open('2c464e58-9121-11e9-aec5-34415dec71f2.txt', 'r')

text = file.readlines()


length = len(text[0])
dollars = []

for i in range(len(text)):
	for j in range(length):
		if (text[i][j]=='$'):
			dollars.append([i, j])

def run_code(r, c):
	row = r
	col = c
	flag_stack = []
	flag_string = ''

	def get_number(row, col, side):
		r = row
		c = col
		number = ''
		if (side=="right"):
			while (True):
				c += 1
				if (text[r][c] not in string.digits):
					break
				number += text[r][c]
			return int(number)
		elif (side=="left"):
			while (True):
				c -= 1
				if (text[r][c] not in string.digits):
					break
				number += text[r][c]
			return int(number)
		elif (side=="below"):
			while (True):
				r += 1
				if (text[r][c] not in string.digits):
					break
				number += text[r][c]
			return int(number)
		else:
			while (True):
				r -= 1
				if (text[r][c] not in string.digits):
					break
				number += text[r][c]
			return int(number)

	while (True):
		if (text[row][col] == '@'):
			return flag_string
		elif (text[row][col] == '$'):
			row += 1
		elif (text[row][col] == '#'):
			col += 1
		elif (text[row][col] == '('):
			char = flag_stack.pop()
			flag_string = char + flag_string
			number = get_number(row, col, "right")
			col -= number
		elif (text[row][col] == ')'):
			char = flag_stack.pop()
			flag_string  = flag_string + char
			number = get_number(row, col, "left")
			col += number
		elif (text[row][col] == '-'):
			flag_string = flag_string[1:]
			number = get_number(row, col, "below")
			row -= number
		elif (text[row][col] == '+'):
			flag_string = flag_string[:-1]
			number = get_number(row, col, "above")
			row += number
		elif (text[row][col] == '%'):
			flag_string = flag_string[::-1]
			row += 1
		elif (text[row][col] == '['):
			col += 1
			flag_stack.append(text[row][col])
			col += 1
		elif (text[row][col] == ']'):
			col -= 1
			flag_stack.append(text[row][col])
			col -= 1
		elif (text[row][col] == '*'):
			row -= 1
			flag_stack.append(text[row][col])
			row -= 1
		elif (text[row][col] == '.'):
			row += 1
			flag_stack.append(text[row][col])
			row += 1
		elif (text[row][col] == '<'):
			number = get_number(row, col, "right")
			col -= number
		elif (text[row][col] == '>'):
			number = get_number(row, col, "left")
			col += number
		elif (text[row][col] == '^'):
			number = get_number(row, col, "below")
			row -= number
		elif (text[row][col] == 'v'):
			number = get_number(row, col, "above")
			row += number

flags = []
for dollar in dollars:
	flags.append(run_code(dollar[0], dollar[1]))

for flag in flags:
	if (flag[:4]=='{FLG'):
		print ('Final flag is', flag)
