# AI in use: True
# trinket: [untested] | vscode: [untested]
#
# Project 8 — The XOR Universe
# Python Bytes / Curriculum
# Needs: lists, for-loops, if logic, modulo (%)
#
# A one-dimensional universe: a row of cells, each empty (0) or filled (1).
# Time ticks downward, one new row per tick. Each new cell follows one law
# based on its two neighbors: the one to the LEFT and the one to the RIGHT.
#
# We try three laws in turn:
#   AND  -> filled only if BOTH neighbors are filled      (dies out: boring)
#   OR   -> filled if EITHER neighbor is filled           (fills up: boring)
#   XOR  -> filled if EXACTLY ONE neighbor is filled      (interesting!)

WIDTH = 79          # cells across (odd, so there is a true middle)
TICKS = 39          # how many rows of time to run

def show(row):
    # filled = 'o', empty = ' '  (needs a fixed-width terminal font)
    print("".join("o" if cell else " " for cell in row))

# --- The three laws. Each takes the two outer neighbors. ---
def law_and(left, right):
    return 1 if (left == 1 and right == 1) else 0

def law_or(left, right):
    return 1 if (left == 1 or right == 1) else 0

def law_xor(left, right):
    # exclusive or: one neighbor filled, but NOT both
    return 1 if (left != right) else 0

def run(law):
    # Empty Universe, then the Big Bang: one dot in the middle.
    row = [0] * WIDTH
    row[WIDTH // 2] = 1
    show(row)
    for tick in range(TICKS):
        new_row = []
        for i in range(WIDTH):
            left  = row[i - 1]           # Python wraps: index -1 is the last cell
            right = row[(i + 1) % WIDTH] # modulo wraps the right edge back to 0
            new_row.append(law(left, right))
        row = new_row
        show(row)

# Try each law. Comment out AND and OR once you have seen how dull they are.
print("--- AND universe (dies out) ---")
run(law_and)
print("--- OR universe (fills up) ---")
run(law_or)
print("--- XOR universe ---")
run(law_xor)


# ----------------------------------------------------------------------
# Watch what happens (predict first)
# ----------------------------------------------------------------------
# AND: the single dot has no two-filled neighbors, so the universe goes
#      empty on the first tick. Over in one step.
# OR:  the dot spreads both directions and never stops. A solid triangle.
# XOR: predict before you run. The answer is the Sierpinski gasket again —
#      the same fractal as the Chaos Game and the L-System, now from logic.
#
# Note: earlier versions offset each row by half a cell and used only TWO
# parents. Here we keep the cells aligned and generalize to the two outer
# parents of three — same spirit, cleaner to code.
#
# Extensions:
#   - Start from random cells instead of a single dot.
#   - Make WIDTH and TICKS bigger (keep WIDTH odd).
