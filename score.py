import os
filepath = os.path.normpath('resc/scores.txt')

def get_scores():
	#get scores from file
	scores = []                         
	with open(filepath) as file:
		line = file.readline().strip()
		while line:
			temp = int(line)
			scores.append(temp)
			line = file.readline().strip()
	return scores

def add_score(time_elapse, score):      # fix 2: added time_elapse
	#add to file
	name = input("Input your name: ")
	data = list()
	with open(filepath, 'r') as file:
		# read a list of lines into data
		line = file.readline().strip()
		while line:
			temp = int(line)
			data.append(temp)
			line = file.readline().strip()
	if score > 0:
		data.append(score)
	data.sort(reverse = True)
	if len(data) > 10:
		data = data[:10]
	scores = ''
	for n in data:
		scores += str(n) + '\n'
	scores.strip()
	with open(filepath, 'w') as file:
		#writes back to file
		file.writelines(scores)