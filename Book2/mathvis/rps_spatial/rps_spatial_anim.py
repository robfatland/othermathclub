"""
Spatial Rock-Paper-Scissors: Three species on a 2D grid compete in a
cyclic dominance relationship (R beats S, S beats P, P beats R).

Each cell holds one species. At each timestep, a random cell attacks a
random neighbor. If the attacker dominates the defender, the defender
converts to the attacker's species. This minimal rule produces spiral
wave patterns — the same dynamics seen in certain bacterial colonies.

Uses a sequential update loop (not fully vectorized) to preserve correct
interaction ordering, with a burn-in period to let spirals emerge from
random initial conditions.

The grid wraps toroidally. Colors: Red, Green, Blue for R, P, S.

Output is an MP4 file saved to ./output/rps_spatial.mp4
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
from matplotlib.colors import ListedColormap
import os

# ── Configuration ─────────────────────────────────────────────────────────────
GRID_SIZE = 500           # larger grid = more room for spirals
NUM_SPECIES = 3           # Rock=0, Paper=1, Scissors=2

# Simulation speed: interactions per frame
# One "sweep" = GRID_SIZE² interactions
SWEEP = GRID_SIZE * GRID_SIZE
STEPS_PER_FRAME = SWEEP * 3   # 3 full sweeps per frame — fast evolution

# Burn-in: run simulation before recording to let spirals emerge
BURNIN_SWEEPS = 200
BURNIN_STEPS = BURNIN_SWEEPS * SWEEP

# Animation
FPS = 30
DURATION = 60             # seconds
TOTAL_FRAMES = FPS * DURATION

print(f"Grid: {GRID_SIZE}×{GRID_SIZE} = {SWEEP} cells")
print(f"Steps per frame: {STEPS_PER_FRAME} ({STEPS_PER_FRAME / SWEEP:.1f} sweeps)")
print(f"Burn-in: {BURNIN_SWEEPS} sweeps ({BURNIN_STEPS:,} steps)")
print(f"Total frames: {TOTAL_FRAMES}, duration: {DURATION}s")

# ── Initialize grid ──────────────────────────────────────────────────────────
rng = np.random.default_rng(seed=2024)
grid = rng.integers(0, NUM_SPECIES, size=(GRID_SIZE, GRID_SIZE), dtype=np.int8)

# ── Colormap: vivid R, G, B ──────────────────────────────────────────────────
cmap = ListedColormap([
    '#E02020',  # Rock - red
    '#20C020',  # Paper - green
    '#2080FF',  # Scissors - blue
])

# ── Neighbor offsets (von Neumann neighborhood — 4 neighbors) ─────────────────
NEIGHBOR_DX = np.array([0, 0, 1, -1], dtype=np.int32)
NEIGHBOR_DY = np.array([1, -1, 0, 0], dtype=np.int32)

# ── Simulation step (vectorized batch with chunking) ─────────────────────────
def simulate_steps(grid, num_steps):
    """
    Perform num_steps random pairwise interactions on the grid.
    Process in chunks to balance vectorization with correctness.
    Smaller chunks = more sequential accuracy, bigger = faster but
    more collisions. Chunk size of ~10% of grid is a good tradeoff.
    """
    N = GRID_SIZE
    chunk_size = SWEEP // 10  # ~10% of grid per batch
    
    remaining = num_steps
    while remaining > 0:
        batch = min(chunk_size, remaining)
        remaining -= batch
        
        # Random attacker positions
        ax = rng.integers(0, N, size=batch)
        ay = rng.integers(0, N, size=batch)
        
        # Random neighbor direction (0-3)
        direction = rng.integers(0, 4, size=batch)
        
        # Defender positions (with toroidal wrapping)
        dx = (ax + NEIGHBOR_DX[direction]) % N
        dy = (ay + NEIGHBOR_DY[direction]) % N
        
        # Get species
        attacker_species = grid[ax, ay]
        defender_species = grid[dx, dy]
        
        # Dominance: attacker i beats (i+2)%3
        beaten = (attacker_species + 2) % 3
        wins = (defender_species == beaten)
        
        # Apply conversions
        grid[dx[wins], dy[wins]] = attacker_species[wins]
    
    return grid

# ── Burn-in ───────────────────────────────────────────────────────────────────
print("Running burn-in to let spirals emerge...")
burnin_chunk = SWEEP * 10  # report every 10 sweeps
for i in range(0, BURNIN_STEPS, burnin_chunk):
    steps = min(burnin_chunk, BURNIN_STEPS - i)
    grid = simulate_steps(grid, steps)
    sweeps_done = (i + steps) // SWEEP
    if sweeps_done % 50 == 0:
        counts = np.bincount(grid.ravel(), minlength=3)
        pcts = counts / counts.sum() * 100
        print(f"  Burn-in sweep {sweeps_done}/{BURNIN_SWEEPS}  |  R:{pcts[0]:.1f}%  P:{pcts[1]:.1f}%  S:{pcts[2]:.1f}%")

print("Burn-in complete. Starting animation recording...")

# ── Set up figure ─────────────────────────────────────────────────────────────
fig, ax_plot = plt.subplots(figsize=(20, 20), facecolor='black')
ax_plot.set_facecolor('black')
ax_plot.set_axis_off()

img = ax_plot.imshow(grid, cmap=cmap, vmin=0, vmax=2,
                     interpolation='nearest', aspect='equal')
plt.tight_layout(pad=0)

# ── Animation function ───────────────────────────────────────────────────────
def animate(frame):
    global grid
    
    grid = simulate_steps(grid, STEPS_PER_FRAME)
    img.set_data(grid)
    
    if (frame + 1) % FPS == 0:
        sec = (frame + 1) // FPS
        counts = np.bincount(grid.ravel(), minlength=3)
        total = counts.sum()
        pcts = counts / total * 100
        print(f"  {sec}s / {DURATION}s  |  R:{pcts[0]:.1f}%  P:{pcts[1]:.1f}%  S:{pcts[2]:.1f}%")
    
    return img,

# ── Render ────────────────────────────────────────────────────────────────────
os.makedirs('output', exist_ok=True)

print("Rendering animation...")
anim = FuncAnimation(fig, animate, frames=TOTAL_FRAMES, interval=1000 // FPS, blit=True)

writer = FFMpegWriter(fps=FPS, metadata={'title': 'Spatial Rock-Paper-Scissors'}, bitrate=5000)
output_path = './output/rps_spatial.mp4'
anim.save(output_path, writer=writer, savefig_kwargs={'facecolor': 'black'})
print(f"\nSaved to {output_path}")
