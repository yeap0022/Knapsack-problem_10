# -*- coding: utf-8 -*-
"""

@author: Yeap Yew Ming
Reference: https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
"""
# Upload file #
file1 = open("./data/ks_4.txt") 
input_data = file1.read()
file1.close()

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])
lines = input_data.split('\n')

firstLine = lines[0].split()
item_count = int(firstLine[0])
capacity = int(firstLine[1])

items = []

for i in range(1, item_count+1):
    line = lines[i]
    parts = line.split()
    items.append(Item(i-1, int(parts[0]), int(parts[1])))

value = []
weight = []
item = []
taken = [0 for x in range(item_count)]
Bag = [[0 for x in range(item_count+1)] for x in range(capacity+1)]

for i in items:
    item.append(i.index)
    value.append(i.value)
    weight.append(i.weight)
    
# Filling up knapsack starts here #   
for i in range(1,len(value)+1): 
    for w in range(1,capacity+1): 
        if i == 0 or w == 0: 
            Bag[w][i] = 0
        elif weight[i-1] <= w: 
            Bag[w][i] = max(value[i-1] + Bag[w-weight[i-1]][i-1],  Bag[w][i-1]) 
        else: 
            Bag[w][i] = Bag[w][i-1]
            
i=item_count
w=capacity
take_ind=[]

# Determine the items to be taken #
while i>0:
    if Bag[w][i] == Bag[w][i-1]:
        i=i-1
    elif Bag[w][i] != Bag[w][i-1]:
        w=w-weight[i-1]
        take_ind.append(i)
        i=i-1

take_ind = sorted(take_ind);

for i in take_ind:
    taken[i-1] = 1

max_weight = sum([a*b for a,b in zip(taken,weight)]);
print("Maximum weight is %s" % max_weight)
print("Pick item number",",".join(str(p) for p in take_ind))
        
