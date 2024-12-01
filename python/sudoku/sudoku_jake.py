# In this program we follow Jake's example code very closely. We use the Python set
#   because it is very well suited to solving Sudoku. A set is different from a list
#   in two important ways: First the elements of a set occur only one time. Second
#   the elements of a set are not in any particular order.
#
# In this program the sets are always sets of characters (not integers). These
#   characters are '0', '1', '2', '3', '4', '5', '6', '7', '8', and '9'.
#
# We also use something called a tuple; in our case a 3-tuple. The 3-tuple used
#   here represents the possible characters (1, 2, ..., 9) that could go in an
#   empty cell of the puzzle. The tuple is described below. 

def row_indices(i): return range(i - i % 9, i - i % 9 + 9)

def col_indices(i): return range(i % 9, i % 9 + 81, 9)

def box_indices(i):
    start = 27 * (i // 27) + 3 * ((i % 9) // 3)
    return [i for j in range(3) for i in range(start + 9 * j, start + 9 * j + 3)]

# connected[] is a list of 81 sets { ... } where the list index i is the cell index.
#   Each set contains indices of other cells that -- when populated with a number from
#   1 to 9 -- act as excluder values: Values that may not be placed in cell i. 
connected = [(set.union(set(box_indices(i)), set(row_indices(i)), set(col_indices(i))) - set([i])) for i in range(81)]

solution_count = 0

# solver(p) will recursively find solutions and "yield" them
#   Key idea 1: The 'p' passed to solver(p) is at first the original puzzle (as a string). 
#   Later (recursive) calls to solver(p) will provide guess-versions of p with more of the
#   cells filled in. In this way -- eventually, if all goes well -- solver(p) will be passed
#   a correct solution to the original puzzle. When this happens we should notice and celebrate!
#
#   Key idea 2: When solver(p) receives an incomplete version of the puzzle p it should add
#     one more guess to that puzzle. That is, fill in one empty square with a guess. Here is how:
#       - Build a picture of possible moves first; then test and *yield*

def solver(p):

    global solution_count

    # First thing we could do here is check to see if the puzzle is solved by 'p'
    #   The question is: What is sufficient logic to be sure that our puzzle is ok?
    # if '0' not in p:
    #     print('found', solution_count, ':', p)
    #     solution_count += 1
    #     if solution_count > 20: return

    
    # Accumulate a list L[] of possibilities: Possible next moves in the puzzle
    #   Each possibility is a 3-tuple:
    #     (number of possible guesses, cell index, the set of those possible guesses)
    L = []
    for i in range(81):
        if p[i] == '0':
            vals = set(['1', '2', '3', '4', '5', '6', '7', '8', '9']) - set(p[n] for n in connected[i])
              # working backwards: connected[i] is a set of cells connected to cell i
              # p[n] is the puzzle value at a connected cell (0 or one of {1, 2, ..., 9})
              # set(--etc--) makes a set of excluded possible values at cell i
              # set('123456789') - set(--etc--) is a set of *allowable* guesses at cell i: vals
            if len(vals) == 0: return             # there are no possible values for this empty cell
            else: L.append((len(vals), i, vals))  # expand the 'possibilities' list L
    
    # if all squares are solved: yield the current puzzle (which must be a solution)
    if len(L) == 0 and '0' not in p: yield p
        
    # choose a cell (index) with the smallest number of possibles; recursively call S() for each possible
    else:
        N, i, vals = min(L)   # the guess cell will be the one with the smallest set of possible guesses
        for guess in vals:      #   ...and let's be thorough and try them all
            puzzle_with_new_guess = p[:i] + guess + p[i+1:]       # this glues together 3 strings
            for s in solver(puzzle_with_new_guess):
                yield s     # ...and for each return all solutions


def CheckSolution(a):
    checkset = set('123456789')
    # row check
    for i in range(9):
        bc = (i%3)*3 + (i//3)*27
        row = set([a[i*9+j] for j in range(9)])
        col = set([a[i + 9*j] for j in range(9)])
        box = set([a[bc], a[bc+1], a[bc+2], a[bc+9], a[bc+10], a[bc+11], a[bc+18], a[bc+19], a[bc+20]])
        if not (row == checkset and col == checkset and box == checkset):
            print('NOT A SOLUTION!!!')
            return
    print('SOLUTION OK')
    return

p0 = '000000000000000000000000000000000000000000000000000000000000000000000000000000000'
p1 = '060000008201800500905002000000704602300090005504608000000900301007005906100000050'
p2 = '008632400040000010500904006800000005600000004107000902400751003060000020005826700'
allsolns = solver(p2)
for a in allsolns:
    print(a)
    CheckSolution(a)

