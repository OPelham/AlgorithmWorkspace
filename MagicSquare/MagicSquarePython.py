#Forming a Magic Square
#https://www.hackerrank.com/challenges/magic-square-forming/problem

#Magic constant = n. ((N^2 +1)/2) , where n = number of sides
#eg if 3 sides then = 15

#given a 3*3 matrix, make minimum swaps to arrive at magic square
#can convert int a to int b at cost a-b
#solution must have all unique integers 1-9

#input from reads in file 'MagicSquareInput.txt'
#saved in list positions in list relative to position in matrix shown below

#list
#[0, 1, 2, 3, 4, 5, 6, 7, 8]

#matrix
# 0 1 2
# 3 4 5
# 6 7 8

#################################################
#input collection
#TODO check input is valid
#check all meet magic constant
#checks 1-3 = horizontal from top row down
#checks 4-6 = vertical from left col to right
#check 7 = diagonal including top-left
#check 8 = diagonal including top-right
#check 9 = all are unique
#check 10 = min = 1, max = 9

inputNumbers = []
magicConstant = 15
checks = {
	1 : False,
	2 : False,
	3 : False,
	4 : False,
	5 : False,
	6 : False,
	7 : False,
	8 : False,
	9 : False,
	10 : False
}

#read in from file and add to collection
def loadInput():
	try:
		with open('MagicSquareInput.txt') as fp:
			lines = fp.readlines() #a list of lines
			for line in lines:
				line = line.strip()
				print(line)
				numberRow = line.split(" ")
				for strNumber in numberRow:
					number = int(strNumber)
					inputNumbers.append(number)

	except FileNotFoundError as e:
		print("No data file found")

def calculateChecks():
	pass
	#run check 
	checkSums()
	checkNumberRange()
	#report results
	#reset to all false for next run
	checks = {
	1 : False,
	2 : False,
	3 : False,
	4 : False,
	5 : False,
	6 : False,
	7 : False,
	8 : False,
	9 : False,
	10 : False
}

def checkSums():
	if (inputNumbers[0] + inputNumbers[1] + inputNumbers[2] == magicConstant):
		checks[1] = True
	if (inputNumbers[3] + inputNumbers[4] + inputNumbers[5] == magicConstant):
		checks[2] = True
	if (inputNumbers[6] + inputNumbers[7] + inputNumbers[8] == magicConstant):
		checks[3] = True
	if (inputNumbers[0] + inputNumbers[3] + inputNumbers[6] == magicConstant):
		checks[4] = True
	if (inputNumbers[1] + inputNumbers[4] + inputNumbers[7] == magicConstant):
		checks[5] = True
	if (inputNumbers[2] + inputNumbers[5] + inputNumbers[8] == magicConstant):
		checks[6] = True
	if (inputNumbers[0] + inputNumbers[4] + inputNumbers[8] == magicConstant):
		checks[7] = True
	if (inputNumbers[2] + inputNumbers[4] + inputNumbers[6] == magicConstant):
		checks[8] = True

#check all ints are unique and in range
def checkNumberRange():
	#check all are unique
	if len(inputNumbers) > len(set(inputNumbers)):
		checks[9] = True
	#check correct min and max
	numberMin = 999
	numberMax = -999
	for num in inputNumbers:
		if num < numberMin:
			numberMin = num
		if num > numberMax:
			numberMax = num
	if numberMin > 0 & numberMax < 10:
		checks[10] = True









loadInput()

#count = 0
#line []
#for p in inputNumbers:
#	print p

print(checks)
calculateChecks()

print(checks)

#Generate solutions in one step find cheapest in another?
#how generate solutions?
#if 




