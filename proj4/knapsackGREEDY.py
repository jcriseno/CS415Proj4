import re
import time
import numpy as np
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
    
        wprop = 0
        take = []
        print values[0]
        for i in range(total_items):
            #print(str.format('{0:6f}', (values[i]/weights[i])))
            getcontext().prec = 6
            #wprop = Decimal(7)/Decimal(3)
            wprop = Decimal(int(values[i]))/Decimal(int(weights[i]))
            #wprop = values[i]/weights[i]
            print(wprop)
            take.append(float(wprop))
        
        while (capacity > 164)
            most = 0
        
        print take
        
        return take 


def main():

	# Getting the capacity of the file 
	# Putting the contents of the file into the CAPACITY variable
    #capacity_input = raw_input("Enter file containing the capacity: ")
    #capacity_file = open(capacity_input)
    capacity_file = open("p01_c.txt")
	capacity = capacity_file.read()
	capacity_file.close()
    capacity = int(capacity)


	# Getting the weights of the file
	# Putting the contents of weights into the WEIGHTS list
    #weights_input = raw_input("Enter file containing the weights: ")
    #weights_file = open(weights_input, 'r')
    weights_file = open("p01_w.txt")
	weights_file = weights_file.read()
	weights = re.findall(r"[-+]?\d*\.\d+|\d+", weights_file)
    weights = map(int, weights)


	# Getting the values of the file
	# Putting the contents of values into the VALUES list
    #values_input = raw_input("Enter file containing the values: ")
	#values_file = open(values_input, 'r')
	values_file = open("p01_v.txt")
    values_file = values_file.read()
	values = re.findall(r"[-+]?\d*\.\d+|\d+", values_file)
    values = map(int, values)

	# Total amount of items given
	total_items = len(values)
        
        print "Capacity: ", capacity
        print "Weights: ", weights
        print "Values: ", values
        print "Number of items: ", total_items
        
        print "Knapsack capacity = ", capacity, ". Total number of items = ", total_items, "\n"

        # Greedy Approach Solution
        take_list = []
        gstart = time.clock()
        greedy(capacity, weights, values, total_items)
        gstop = time.clock()
        print "Take list: ", take_list
        print "Greedy Approach Optimal value: "
        print "Greedy Approach Optimal subset: "
        print "Greedy Approach Time Taken: ", gstop - gstart


	return 0

main()
