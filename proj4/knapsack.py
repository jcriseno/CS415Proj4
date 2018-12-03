import re
import time
from decimal import *

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


def greedy(capacity, weights, values, total_items):
    optimal_value = 0
    greedy_solution = []
    wprop = 0 # "weight proportionate (to value)"
    take = [] # init list for wprop
    getcontext().prec = 6
    # for loop will index from 0 - total_items
    # adds wprop to take list
    for i in range(total_items):
        wprop = Decimal(int(values[i]))/Decimal(int(weights[i]))
        take.append(float(wprop))


    while capacity > 0:
        most = max(take) #find max wprop from take list
        most_index = take.index(most) #find index
        capacity -= weights[most_index]
        if capacity < 0:
            break
        optimal_value += values[most_index]
        take.remove(most)
        take.insert(most_index, 0)
        greedy_solution.append(most_index + 1)

    greedy_solution.sort()

    return optimal_value, greedy_solution


def main():
	
    # Getting the capacity of the file
    # Putting the contents of the file into the CAPACITY variable
    #capacity_input = raw_input("Enter file containing the capacity: ")
    #capacity_file = open(capacity_input)
    capacity_file = open("p07_c.txt")
    capacity = capacity_file.read()
    capacity_file.close()
    capacity = int(capacity)
    
    
    # Getting the weights of the file
    # Putting the contents of weights into the WEIGHTS list
    #weights_input = raw_input("Enter file containing the weights: ")
    #weights_file = open(weights_input, 'r')
    weights_file = open("p07_w.txt")
    weights_file = weights_file.read()
    weights = re.findall(r"[-+]?\d*\.\d+|\d+", weights_file)
    weights = map(int, weights)
    
    
    # Getting the values of the file
    # Putting the contents of values into the VALUES list
    #values_input = raw_input("Enter file containing the values: ")
    #values_file = open(values_input, 'r')
    values_file = open("p07_v.txt")
    values_file = values_file.read()
    values = re.findall(r"[-+]?\d*\.\d+|\d+", values_file)
    values = map(int, values)

    # Total amount of items given
    total_items = len(values)

    print("")
    print("Knapsack capacity = " + str(capacity) + ". " + "Total number of items = " + str(total_items))
    print("")

    # Dynamic Programming Solution
    dynamic_start = time.time()
    dynamic_value, dynamic_solution = dynamic(capacity, weights, values, total_items)
    dynamic_end = time.time()
    dynamic_time = dynamic_end - dynamic_start
    print("Dynamic Programming Optimal value: " + str(dynamic_value))
    print("Dynamic Programming Optimal subset: {" + str(dynamic_solution) + "}")
    print("Dynamic Programming Time Taken: " + str(dynamic_time))
    print ""
    
    # Greedy Approach Solution
    gstart = time.clock()
    greedy_value, greedy_solution = greedy(capacity, weights, values, total_items)
    gstop = time.clock()
    print "Greedy Approach Optimal value: ", greedy_value
    print "Greedy Approach Optimal subset: ", greedy_solution
    print "Greedy Approach Time Taken: ", gstop - gstart


    return 0

main()
