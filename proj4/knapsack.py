import re
import time

def dynamic(capacity, weights, values, total_items):
	F = [[0 for x in range (capacity + 1)] for y in range (total_items + 1)]
	for i in range(total_items + 1):
		for j in range(capacity + 1):
			if i == 0 or j == 0:
				F[i][j] = 0
			elif j - weights[i-1] >= 0:
				F[i][j] = max(F[i-1][j], values[i-1] + F[i-1][j-weights[i-1]])
			else:
				F[i][j] = F[i-1][j]

	i = total_items
	j = capacity
	optimal_solution = []
	while(i > 0 and j > 0):
		if(F[i][j] > F[i-1][j]):
			optimal_solution.append(i)
			i = i - 1
			j = j - weights[i]
		else:
			i = i - 1

	optimal_solution.reverse()

	return F[total_items][capacity], optimal_solution


def main():
	
	# Getting the capacity of the file 
	# Putting the contents of the file into the CAPACITY variable
	capacity_input = raw_input("Enter file containing the capacity: ")
	capacity_file = open(capacity_input)
	capacity = capacity_file.read()
	capacity_file.close()
	capacity = int(capacity)


	# Getting the weights of the file
	# Putting the contents of weights into the WEIGHTS list
	weights_input = raw_input("Enter file containing the weights: ")
	weights_file = open(weights_input, 'r')
	weights_file = weights_file.read()
	weights = re.findall(r"[-+]?\d*\.\d+|\d+", weights_file)
	weights = map(int, weights)


	# Getting the values of the file
	# Putting the contents of values into the VALUES list
	values_input = raw_input("Enter file containing the values: ")
	values_file = open(values_input, 'r')
	values_file = values_file.read()
	values = re.findall(r"[-+]?\d*\.\d+|\d+", values_file)
	values = map(int, values)

	# Total amount of items given
	total_items = len(values)

	print("")
	print("Knapsack capacity = " + str(capacity) + ". " + "Total number of items = " + str(total_items))
	print("")

	dynamic_start = time.time()
	dynamic_value, dynamic_solution = dynamic(capacity, weights, values, total_items)
	dynamic_end = time.time()
	dynamic_time = dynamic_end - dynamic_start
	print("Dynamic Programming Optial value: " + str(dynamic_value))
	print("Dynamic Programming Optimal subset: " + str(dynamic_solution))
	print("Dynamic Programming Time Taken: " + str(dynamic_time))


	return 0

main()