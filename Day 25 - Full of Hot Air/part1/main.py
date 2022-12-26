def read_file(namefile):
    with open(namefile, 'r') as f:
        lines = f.read().splitlines()
    return lines


class SNAFU_Reader:
	def __init__(self, _input):
		total_sum = 0
		for number in _input:
			total_sum += self.to_decimal(number)
		print(total_sum)
		number = self.to_SNAFU(total_sum)
		print(number)
		print(self.to_decimal(number))

	def to_decimal(self, number):
		decimal = 0
		for idx, n in enumerate(reversed(number)):
			power = pow(5, idx)
			if '0'<=n<='2':
				n = int(n)
			elif n=='-':
				n = -1
			else:
				n = -2
			decimal += power*n
		return decimal

	def to_SNAFU(self, number):
		snafu_number = []
		while number != 0:
			snafu_number.append(number%5)
			number = number//5

		snafu_number.append(0)
		for idx, n in enumerate(snafu_number):
			if n >=3:
				snafu_number[idx] = n-5
				snafu_number[idx+1] += 1
		if snafu_number[-1] == 0:
			del snafu_number[-1]

		output = ""
		for n in snafu_number:
			if n>=0:
				output = str(n) + output
			elif n == -1:
				output = '-' + output
			else:
				output = '=' + output
		return output

if __name__ == "__main__":
	day_input = read_file("input.txt")

	manager = SNAFU_Reader(day_input)
