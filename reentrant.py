import sys
import numpy as np
import time
import random
from collections import deque
    
# --- Constants ---
N = 8  # Board size
MOVES = [
    (2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)
]

# Increase recursion limit for potentially deep calls (if using a recursive solver)
# sys.setrecursionlimit(2000) 

def is_valid(r, c, board_state):
    """Checks if a move (r, c) is on the board and unvisited."""
    return 0 <= r < N and 0 <= c < N and board_state[r][c] == -1

def count_onward_moves(r, c, board_state):
    """Counts the number of valid unvisited moves from a square (r, c)."""
    count = 0
    for dr, dc in MOVES:
        nr, nc = r + dr, c + dc
        if is_valid(nr, nc, board_state):
            count += 1
    return count

def get_sorted_moves_randomized(r, c, board_state):
    """
    Warnsdorff's Rule with tie-breaking: 
    Returns valid next moves sorted by onward moves. 
    Randomly selects a single move from the best choices (those with the minimum onward count).
    """
    possible_moves = []
    for dr, dc in MOVES:
        nr, nc = r + dr, c + dc
        if is_valid(nr, nc, board_state):
            onward_count = count_onward_moves(nr, nc, board_state)
            possible_moves.append((onward_count, nr, nc))
    
    if not possible_moves:
        return None # No moves available

    # Sort by onward_count (Warnsdorff's Rule)
    possible_moves.sort(key=lambda x: x[0])
    
    # Identify the minimum onward count
    min_count = possible_moves[0][0]
    
    # Find all moves that share this minimum count (tie-breaking)
    best_moves = [move for move in possible_moves if move[0] == min_count]
    
    # Randomly select one move from the best options
    _, next_r, next_c = random.choice(best_moves)
    
    return (next_r, next_c)

def find_tour(start_r, start_c, N=8):
    """
    Attempts to find a single, full knight's tour starting at (start_r, start_c)
    using randomized Warnsdorff's Rule.
    """
    board = [[-1 for _ in range(N)] for _ in range(N)]
    
    current_r, current_c = start_r, start_c
    board[current_r][current_c] = 0
    
    total_squares = N * N
    
    for move_num in range(1, total_squares):
        
        next_move = get_sorted_moves_randomized(current_r, current_c, board)
        
        if next_move is None:
            # Dead end reached before completion
            return None, False, move_num # board, is_closed, last_move_num
        
        next_r, next_c = next_move
        
        # Make the move
        board[next_r][next_c] = move_num
        current_r, current_c = next_r, next_c

    # --- Check for Reentrant (Closed) Condition ---
    
    # Check if the last square is a knight's move away from the starting square
    dr = abs(current_r - start_r)
    dc = abs(current_c - start_c)
    
    is_closed = (dr == 1 and dc == 2) or (dr == 2 and dc == 1)
    
    return board, is_closed, total_squares - 1

def print_board(board):
    """Prints the tour board in a readable format."""
    if board is None:
        return
    
    N = len(board)
    np_board = np.array(board)
    
    print("-" * (4 * N + 1))
    for row in np_board:
        print("|", end="")
        for cell in row:
            print(f"{cell:3}", end="|")
        print()
        print("-" * (4 * N + 1))

def solve_reentrant_with_timeout(N=8, timeout_seconds=60):
    """
    Iteratively searches for a closed tour with a time limit.
    Iterates through starting positions to increase the chance of success.
    """
    start_time = time.time()
    last_print_time = start_time
    
    # Generate all possible starting squares and randomize the order
    starting_squares = [(r, c) for r in range(N) for c in range(N)]
    random.shuffle(starting_squares)
    
    # Use a deque to treat starting squares as a rotating list
    start_queue = deque(starting_squares)
    
    attempts = 0
    
    print(f"Starting iterative search for a closed {N}x{N} Knight's Tour (Timeout: {timeout_seconds}s).")

    while time.time() - start_time < timeout_seconds:
        
        current_time = time.time()
        elapsed = current_time - start_time
        
        # Print status update every 5 seconds
        if current_time - last_print_time >= 5:
            print(f"[STATUS] Elapsed Time: {elapsed:.2f}s. Attempts: {attempts}. Trying new tour.")
            last_print_time = current_time
            
        # Select the next starting square and put it at the back of the queue
        start_r, start_c = start_queue.popleft()
        start_queue.append((start_r, start_c))
        
        attempts += 1
        
        # Find a tour from the current starting position
        tour_board, is_closed, last_move = find_tour(start_r, start_c, N)
        
        if tour_board is None:
            # Tour failed to complete (dead end)
            # print(f"Attempt {attempts}: Failed to complete tour from ({start_r}, {start_c}) at move {last_move}.")
            continue
            
        if is_closed:
            # Success! Found a closed tour
            print("\n" + "="*50)
            print(f"SUCCESS! Found a REENTRANT (CLOSED) Knight's Tour!")
            print(f"Start Position: ({start_r}, {start_c})")
            print(f"Total Attempts: {attempts}")
            print(f"Total Time: {elapsed:.2f} seconds")
            print("="*50)
            print_board(tour_board)
            return tour_board

        else:
            # Full tour found, but it is not closed (open tour)
            # print(f"Attempt {attempts}: Found an OPEN tour from ({start_r}, {start_c}). Trying again...")
            pass
            
    # Timeout reached
    print("\n" + "="*50)
    print(f"HALTING: Time limit of {timeout_seconds} seconds reached.")
    print(f"Total Attempts: {attempts}")
    print("No closed tour was found within the time limit.")
    print("="*50)
    return None

# --- Execute the Search ---

# Solve for an 8x8 board with a 60-second limit
solve_reentrant_with_timeout(N=8, timeout_seconds=60)
