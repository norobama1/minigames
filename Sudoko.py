#solve sudoko using backtracking
#our puzzle is a list of lists,where each inner list is a row in our sudoko puzzle
def find_next_empty(puzzle):
#find the next row,col on the puzzle thats not filled yet -->rep with -1
#return row,col tuple (None,None) if there is none
    for r in range(9):
          for c in range(9):
               if puzzle[r][c] ==-1:
                return r,c
    return None,None #if no spaces left

def is_valid(puzzle,guess,row,col):
    #figure out whether the guess at the row/col is valid guess or not
    #for row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    #for columns
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    
    #for the square
    row_starts = (row//3)*3 
    col_starts = (col//3)*3

    for r in range(row_starts,row_starts+3):
       for c in range(col_starts,col_starts+3):
           if puzzle[r][c] == guess:
            return False
    
    #otherwise 
    return True


def solve_sudoko(puzzle):
    #step 1: choose somewhere on the puzzle to make a guess
    row,col = find_next_empty(puzzle)
      
    if row is None:
        return True
    
    #step 2: if there is place to put a number ,then make a guess bte 1 and 9
    for guess in range(1,10):
        #step 3:check if this is valid guess
        if is_valid(puzzle,guess,row,col):
            #if valid then place that guess on the puzzle
            puzzle[row][col] = guess

            #step 4: recursively call our function
            if solve_sudoko(puzzle):
                return True
        
        #step 5: if not valid or if ur guess does not solve the puzzle
        #then we use backtracking and try a new number
        puzzle[row][col] = -1

    #step 6:if none of the numbers that we try work
    return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],
        
        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoko(example_board))
    print(example_board)