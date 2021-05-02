from random import seed
from random import randint
from itertools import permutations

def p(grid,row,col,n):
    #print("Checking if ", n, " can be placed at possition, grid[",row, "] [",col, "]")
    #checking if the value of n is equal to the value is the given possiton
    if grid[row-1][col-1] ==  n:
       #print("True, the given value, ", n , "IS found at the given possition, grid[ ",row, "] [",col, "]" )
       #prints output, and returns true
       return True
    else:
        return False


#this function checks each block of the puzzle for containing numbers 1-4
def check4blocks(grid):
    blockFoundcounter = 0
    #print("\n")
    #print("Checking block 1")
    blockTwor = 2
    blockTwoc = 2
    c = 1
    r = 1
    counter = 0
    holder = []
    while r <= blockTwor:
        while c <= blockTwoc:
            num = 1
            while num <= 4:
                if p(grid,r,c,num):
                    if num not in holder:
                        holder.append(num)
                        num += 1
                        counter += 1
                    else:
                        num +=1
                else:
                    num +=1
            c += 1
        r += 1
        c = 1
        
    if counter == 4:
        #print("This block contains numbers 1 - 4, True")
        #print("\n")
        blockFoundcounter += 1
    else:
        #print("This block does NOT contain numbers 1 - 4, False")
        #print("\n")
        pass

    #print("\n")
    #print("Checking block 2")
    blockTwor = 2
    blockTwoc = 4
    c = 3
    r = 1
    counter = 0
    holder = []
    while r <= blockTwor:
        while c <= blockTwoc:
            num = 1
            while num <= 4:
                if p(grid,r,c,num):
                    if num not in holder:
                        holder.append(num)
                        num += 1
                        counter += 1
                    else:
                        num +=1
                else:
                    num +=1
            c += 1
        r += 1
        c = 3
        
    if counter == 4:
        #print("This block contains numbers 1 - 4, True")
        #print("\n")
        blockFoundcounter += 1
    else:
        #print("This block does NOT contain numbers 1 - 4, False")
        #print("\n")
        pass
    
    #print("\n")
    #print("Checking block 3")
    blockTwor = 4
    blockTwoc = 2
    c = 1
    r = 3
    counter = 0
    holder = []
    while r <= blockTwor:
        while c <= blockTwoc:
            num = 1
            while num <= 4:
                if p(grid,r,c,num):
                    if num not in holder:
                        holder.append(num)
                        num += 1
                        counter += 1
                    else:
                        num +=1
                else:
                    num +=1
            c += 1
        r += 1
        c = 1
        
    if counter == 4:
        #print("This block contains numbers 1 - 4, True")
        #print("\n")
        blockFoundcounter += 1
    else:
        #print("This block does NOT contain numbers 1 - 4, False")
        #print("\n")
        pass
        
    #print("\n")
    #print("Checking block 4")
    blockTwor = 4
    blockTwoc = 4
    c = 3
    r = 3
    counter = 0
    holder = []
    while r <= blockTwor:
        while c <= blockTwoc:
            num = 1
            while num <= 4:
                if p(grid,r,c,num):
                    if num not in holder:
                        holder.append(num)
                        num += 1
                        counter += 1
                    else:
                        num +=1
                else:
                    num +=1
            c += 1
        r += 1
        c = 3
        
    if counter == 4:
        #print("This block contains numbers 1 - 4, True")
        #print("\n")
        blockFoundcounter += 1
    else:
        #print("This block does NOT contain numbers 1 - 4, False")
        #print("\n")
        pass
        
        
    if blockFoundcounter == 4:
        #print("\n")
        #print("All blocks contain numbers 1 - 4")
        return True
    else:
        #print("\n")
        #print("All blocks do NOT contain numbers 1 - 4")
        return False

def check4col( grid ): 
    colFoundCounter = 0
    #checking col 1
    col = 1
    row = 1
    counter = 0
    holder = []
    while row <= 4:
        num = 1
        while num <=4:
            if p(grid,row,col,num):
                if num not in holder:
                    holder.append(num)
                    num +=1
                    counter += 1
                else:
                    num +=1
            else:
                num +=1
        row +=1
    if counter == 4:
        colFoundCounter +=1
    
    #checking col 2
    col = 2
    row = 1
    counter = 0
    holder = []
    while row <= 4:
        num = 1
        while num <=4:
            if p(grid,row,col,num):
                if num not in holder:
                    holder.append(num)
                    num +=1
                    counter += 1
                else:
                    num +=1
            else:
                num +=1
        row +=1
    if counter == 4:
        colFoundCounter +=1
        
    #checking col 3
    col = 3
    row = 1
    counter = 0
    holder = []
    while row <= 4:
        num = 1
        while num <=4:
            if p(grid,row,col,num):
                if num not in holder:
                    holder.append(num)
                    num +=1
                    counter += 1
                else:
                    num +=1
            else:
                num +=1
        row +=1
    if counter == 4:
        colFoundCounter +=1

    #checking col 4
    col = 4
    row = 1
    counter = 0
    holder = []
    while row <= 4:
        num = 1
        while num <=4:
            if p(grid,row,col,num):
                if num not in holder:
                    holder.append(num)
                    num +=1
                    counter += 1
                else:
                    num +=1
            else:
                num +=1
        row +=1
        
    if counter == 4:
        colFoundCounter +=1
        
    if colFoundCounter == 4:
        return True
    else:
        return False
    
def generateSolved4x4Sodoku():
    grid = []
    grid.append([0,0,0,0])
    grid.append([0,0,0,0])
    grid.append([0,0,0,0])
    grid.append([0,0,0,0])
    allPossibleRows = list( permutations([1,2,3,4]) )
    upperbound = len(allPossibleRows) - 1
    while check4blocks(grid) != True and check4col(grid) != True:
        grid = []
        row = 1
        while row <= 4:
            grid.append( list(allPossibleRows[randint(0,upperbound)]) )
            row +=1
        #print (grid)
    return grid
        
        
print( generateSolved4x4Sodoku()  )  




