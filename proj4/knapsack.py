import re
import numpy as np

def dynamic(capacity, weights, values, total_items):
	#F = [[int(0) for x in range(weights + 1)] for x in range(total_items + 1)]
	F = (weights + 1, total_items + 1)
	np.zeroes(F)
	for i in range(total_items + 1):
		for j in range(capacity + 1):
			if i == 0 or j == 0:
				F[i][j] = 0
			elif weights[i-1] <= capacity:
				F[i][j] = max(val[i-1] + F[i-1][j-weight[i-1]], K[i-1][j])
			else:
				F[i][j] = F[i-1][j]

	return F[total_items][capacity]


def main():

	# Getting the capacity of the file 
	# Putting the contents of the file into the CAPACITY variable
	F = (5 + 1, 6 + 1)
	np.zeros(F)
	print(F)
	capacity_input = raw_input("Enter file containing the capacity: ")
	capacity_file = open(capacity_input)
	capacity = capacity_file.read()
	capacity_file.close()


	# Getting the weights of the file
	# Putting the contents of weights into the WEIGHTS list
	weights_input = raw_input("Enter file containing the weights: ")
	weights_file = open(weights_input, 'r')
	weights_file = weights_file.read()
	weights = re.findall(r"[-+]?\d*\.\d+|\d+", weights_file)


	# Getting the values of the file
	# Putting the contents of values into the VALUES list
	values_input = raw_input("Enter file containing the values: ")
	values_file = open(values_input, 'r')
	values_file = values_file.read()
	values = re.findall(r"[-+]?\d*\.\d+|\d+", values_file)

	# Total amount of items given
	total_items = len(values)

	dynamic_value = dynamic(capacity, weights, values, total_items)
	print(dynamic_value)


	return 0

main()