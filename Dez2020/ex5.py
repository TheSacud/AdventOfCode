#!/usr/bin/python
# Import a set of airplane seat identifiers (described using binary space partitioning)
# Identify the highest value seat ID according to a formula (seatID = (8*row) + column)

from math import ceil as round_up


with open('ex5.txt','r') as fd:
    highestID = 0
    list_seatID = []

    for bilhete in fd:
        max_row = 127
        min_row = 0
        min_col = 0
        max_col = 7
        
        for row in bilhete[0:7]:
            if row == "F":
                max_row = (min_row + max_row)//2
            else:
                min_row = round_up((min_row + max_row)/2)
            lugar_row = min_row

        for col in bilhete[7:10]:
            if col == "R":
                min_col = round_up((min_col + max_col)/2)
            else:
                max_col = (min_col + max_col)//2
            lugar_col = min_col

        currentID = (lugar_row * 8) + lugar_col
        if currentID > highestID:
            highestID = currentID
        ## parte 2
        list_seatID.append(currentID)

        list_seatID.sort()
        for id in range(list_seatID[0], list_seatID[-1]):
            if id not in list_seatID:
                if(id - 1) in list_seatID and (id + 1) in list_seatID:
                    i = id
    print(i)
    print(str(highestID))

    
