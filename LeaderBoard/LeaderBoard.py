#Climbing the Leaderboard
#https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

#1 read in inputs and save in list
numberOfPlayers = 0 #number of players on leaderboard
scores = [] #all existing scores
numberOfGames = 0 #number of games played by Alice
alice = [] #scores of Alice's games

def readInput():
	try:
		with open('LeaderBoardInput.txt') as fp:
			lines = fp.readlines() #a list of lines

			for line in lines:
				line = line.strip()
				
			print(lines[0])
			numberOfPlayers = lines[0]
			print(numberOfPlayers)

			scores = lines[1]#.split(" ")
			print(scores)

			numberOfGames = lines[2]
			print(numberOfGames)

			alice = lines[3]
			print(alice)


				#row = line.split(" ")
				#for strNumber in numberRow:
				#	number = int(strNumber)
				#	inputNumbers.append(number)

	except FileNotFoundError as e:
		print("No data file found")

readInput()
