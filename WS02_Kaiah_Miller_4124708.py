#function bellow is for question 1
def p(grid,row,col,n):
    print("Checking if ", n, " can be placed at possition, grid[",row, "] [",col, "]")
    #checking if the value of n is equal to the value is the given possiton
    if grid[row-1][col-1] ==  n:
       print("True, the given value, ", n , "IS found at the given possition, grid[ ",row, "] [",col, "]" )
       #prints output, and returns true
       return True
   
    else:
        #first checking if the space contains zero
        #if it does, then there IS a possibility of value n being placed there
        #returns true, however we dont know for sure if the value can be placed there tey
        #the check row and check grid functions can confirm or deny this possibility
        if grid[row-1][col-1] == 0:
            print("The given possition, grid[",row, "] [",col, "] is EMPTY" )
            print("There IS a possibility of value ", n, " being placed here")
            return False
        #if the value is not zero, and not equal to n then it is not possible that n
        #can be placed in the given possition
        else:
            value = grid[row-1][col-1]
            print("False, The given possition, grid[",row, "] [",col, "] contains the value, ",value )
            print("The value ", n, " cannot be placed here")
            return False

#this function checks if a row contains all numbers 1 - 4
def check4rows(grid):
    row = 4
    col = 4
    trueCount = 0
    #iterate through every row
    for r in range(row):
        #iteratre through every col
        #counter to shote the number of times p function returns true
        counter = 0
        for c in range(col):
            num = 1
            #while loop applies a check for each number 1 - 4 in a given possition
            while num <= 4:
                #check if the number is contained in that specific location
                if p(grid,r,c,num):
                   num += 1
                   counter += 1
                else:
                    num +=1
        #check if p function returns true 4 times    
        if counter == 4:
            print("The row contains all numbers 1 - 4, True")
            print("\n")
                #add a counter for trueCount saying the row was satisfied
            trueCount += 1
        else:
            print("The row does NOT contains all numbers 1 - 4, False")
            print("\n")
                
    if trueCount == 4:
        print("Every row satisfies numbers 1 - 4")
        print("\n")
        return True
    else:
        print("Every row does NOT satisfy numbers 1 - 4")
        print("\n")
        return False
            
#this function checks each block of the puzzle for containing numbers 1-4
def check4blocks(grid):
    blockFoundcounter = 0
    print("\n")
    print("Checking block 1")
    blockTwor = 1
    blockTwoc = 1
    c = 0
    r = 0
    counter = 0
    while r <= blockTwor:
        while c <= blockTwoc:
            num = 1
            while num <= 4:
                if p(grid,r,c,num):
                   num += 1
                   counter += 1
                else:
                    num +=1
            c += 1
        r += 1
        c = 0
        
    if counter == 4:
        print("This block contains numbers 1 - 4, True")
        print("\n")
        blockFoundcounter += 1
    else:
        print("This block does NOT contain numbers 1 - 4, False")
        print("\n")

    print("\n")
    print("Checking block 2")
    blockTwor = 1
    blockTwoc = 3
    c = 2
    r = 0
    counter = 0
    while r <= blockTwor:
        while c <= blockTwoc:
            num = 1
            while num <= 4:
                if p(grid,r,c,num):
                   num += 1
                   counter += 1
                else:
                    num +=1
            c += 1
        r += 1
        c = 2
        
    if counter == 4:
        print("This block contains numbers 1 - 4, True")
        print("\n")
        blockFoundcounter += 1
    else:
        print("This block does NOT contain numbers 1 - 4, False")
        print("\n")
    
    print("\n")
    print("Checking block 3")
    blockTwor = 3
    blockTwoc = 1
    c = 0
    r = 2
    counter = 0
    while r <= blockTwor:
        while c <= blockTwoc:
            num = 1
            while num <= 4:
                if p(grid,r,c,num):
                   num += 1
                   counter += 1
                else:
                    num +=1
            c += 1
        r += 1
        c = 0
        
    if counter == 4:
        print("This block contains numbers 1 - 4, True")
        print("\n")
        blockFoundcounter += 1
    else:
        print("This block does NOT contain numbers 1 - 4, False")
        print("\n")
        
    print("\n")
    print("Checking block 4")
    blockTwor = 3
    blockTwoc = 3
    c = 2
    r = 2
    counter = 0
    while r <= blockTwor:
        while c <= blockTwoc:
            num = 1
            while num <= 4:
                if p(grid,r,c,num):
                   num += 1
                   counter += 1
                else:
                    num +=1
            c += 1
        r += 1
        c = 2
        
    if counter == 4:
        print("This block contains numbers 1 - 4, True")
        print("\n")
        blockFoundcounter += 1
    else:
        print("This block does NOT contain numbers 1 - 4, False")
        print("\n")
        
        
    if blockFoundcounter == 4:
        print("\n")
        print("All blocks contain numbers 1 - 4")
        return True
    else:
        print("\n")
        print("All blocks do NOT contain numbers 1 - 4")
        return False
        
        

                
grid = []

grid.append([2,1,0,0])
grid.append([0,3,2,0])
grid.append([0,0,0,4])
grid.append([1,0,0,0])

grid2 = [ [2, 1, 4, 3],
          [4, 3, 2, 1],
          [3, 2, 1, 4],
          [1, 4, 3, 2] ]


print("\n")
print("This is my grid :")
print(grid)

print("\n")
print("This is the output of my p function :")
print( p(grid,2,2,0) )

print("\n")
print("This is the output of my check4rows function :")
check4rows(grid)

print("\n")
print("This is the output of my check4blocks function :")
check4blocks(grid)



print("\n")
print("This is my grid :")
print(grid2)

print("\n")
print("This is the output of my p function :")
print( p(grid2,2,2,0) )

print("\n")
print("This is the output of my check4rows function :")
check4rows(grid2)

print("\n")
print("This is the output of my check4blocks function :")
check4blocks(grid2)



