#Climbing the Leaderboard
#https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

#1 read in inputs and save in list
numberOfPlayers = 0 #number of players on leaderboard
scores = [] #all existing scores
numberOfGames = 0 #number of games played by Alice
alice = [] #scores of Alice's games

#READ INPUT ASSIGN TO COLLECTIONS
def readInput():
	try:
		with open('LeaderBoardInput.txt') as fp:
			#wipe existing data
			global numberOfPlayers
			global scores
			global numberOfGames
			global alice

			#read and assign lines to collections
			lines = fp.readlines() #a list of lines
			numberOfPlayers = lines[0].strip()
			scores = lines[1].strip().split(" ")
			numberOfGames = lines[2].strip()
			alice = lines[3].strip().split(" ")

			#process strings to int
			processInput(numberOfPlayers)
			processInput(scores)
			processInput(numberOfGames)
			processInput(alice)

			#print for debugging reasons
			print(numberOfPlayers)
			print(scores)
			print(numberOfGames)
			print(alice)

	except FileNotFoundError as e:
		print("No data file found")

def rankScores():
	for alicesscore in alice:
		pass

def processInput(list):
	for unit in list:
		unit = int(unit)


readInput()
#rankScores()
print(numberOfPlayers)
print(scores)
print(numberOfGames)
print(alice)
print(numberOfGames + numberOfPlayers)

