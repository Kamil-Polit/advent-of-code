from time import time

start_time = time()

with open("data.txt", 'r') as f:
	data = f.read()
	floor = 0
	for i in range(len(data)):
		if data[i] == '(':
			floor += 2
		else:
			floor -= 1

print(time() - start_time)
