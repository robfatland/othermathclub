"""
SmoothLife / Lenia hybrid: A continuous-state cellular automaton that
reliably produces dynamic, evolving patterns from random initial conditions.

This uses the SmoothLife formulation (Rafler, 2011) which is more robust
than vanilla Lenia for producing spontaneous persistent dynamics:
- Inner disk measures local density (self)
- Outer ring measures neighborhood density
- Smooth sigmoid transition functions replace hard birth/death thresholds
- Continuous states in [0, 1]

The result: from random initial conditions, blobs form, move, split,
merge, pulse, and interact — indefinitely. No careful tuning of initial
patterns required.

Output: ./output/lenia.mp4

Requires: numpy, matplotlib, ffmpeg
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
from matplotlib.colors import LinearSegmentedColormap
import os

# ── Configuration ─────────────────────────────────────────────────────────────
SIZE = 512            # grid resolution (larger = more detail)
FPS = 30
DURATION = 90         # seconds
TOTAL_FRAMES = FPS * DURATION
STEPS_PER_FRAME = 1   # one step per frame is enough at this dt

# SmoothLife parameters
RA = 21.0            # outer radius (neighborhood ring)
RI = RA / 3.0        # inner radius (self-density disk)
DT = 0.1             # timestep

# Birth/death sigmoid parameters
# b1, b2: birth thresholds (neighborhood density range that causes birth)
# d1, d2: death thresholds (neighborhood density range that sustains life)
B1 = 0.278
B2 = 0.365
D1 = 0.267
D2 = 0.445
ALPHA_N = 0.028      # sigmoid sharpness for neighborhood
ALPHA_M = 0.147      # sigmoid sharpness for cell state

print(f"SmoothLife grid: {SIZE}×{SIZE}")
print(f"Radii: inner={RI:.1f}, outer={RA:.1f}")
print(f"Birth range: [{B1}, {B2}], Death range: [{D1}, {D2}]")
print(f"Total frames: {TOTAL_FRAMES}, duration: {DURATION}s")

# ── Build kernels (inner disk and outer ring) ─────────────────────────────────
def build_kernels(size, ri, ra):
    """Build inner (disk) and outer (ring) kernels in frequency domain."""
    mid = size // 2
    y, x = np.ogrid[-mid:size-mid, -mid:size-mid]
    dist = np.sqrt(x*x + y*y)

    # Inner disk kernel (radius ri)
    inner = np.zeros((size, size))
    inner[dist < ri] = 1.0
    inner_sum = inner.sum()
    if inner_sum > 0:
        inner /= inner_sum

    # Outer ring kernel (between ri and ra)
    outer = np.zeros((size, size))
    outer[(dist >= ri) & (dist < ra)] = 1.0
    outer_sum = outer.sum()
    if outer_sum > 0:
        outer /= outer_sum

    # Precompute FFTs
    inner_fft = np.fft.fft2(np.fft.ifftshift(inner))
    outer_fft = np.fft.fft2(np.fft.ifftshift(outer))

    return inner_fft, outer_fft

inner_fft, outer_fft = build_kernels(SIZE, RI, RA)

# ── Sigmoid functions ─────────────────────────────────────────────────────────
def sigma(x, a, alpha):
    """Smooth step function centered at a with sharpness alpha."""
    return 1.0 / (1.0 + np.exp(-(x - a) * 4.0 / alpha))

def sigma_n(x, a, b, alpha):
    """Smooth interval function: ~1 when a < x < b, ~0 otherwise."""
    return sigma(x, a, alpha) * (1.0 - sigma(x, b, alpha))

def sigma_m(x, y, m, alpha):
    """Smooth linear interpolation controlled by m."""
    return x * (1.0 - sigma(m, 0.5, alpha)) + y * sigma(m, 0.5, alpha)

def transition(n, m):
    """
    SmoothLife transition function.
    n = neighborhood (outer ring) density
    m = inner (self) density
    Returns the target state: how alive the cell should become.
    """
    # Birth function: alive if neighborhood is in [b1, b2]
    birth = sigma_n(n, B1, B2, ALPHA_N)
    # Death (survival) function: stay alive if neighborhood is in [d1, d2]
    survival = sigma_n(n, D1, D2, ALPHA_N)
    # Interpolate based on current state
    return sigma_m(birth, survival, m, ALPHA_M)

# ── Initialize grid with random blobs ─────────────────────────────────────────
rng = np.random.default_rng(seed=2024)
grid = np.zeros((SIZE, SIZE), dtype=np.float64)

# Start with scattered random circular blobs at various densities
for _ in range(80):
    cx = rng.integers(0, SIZE)
    cy = rng.integers(0, SIZE)
    r = rng.uniform(5, 25)
    y, x = np.ogrid[:SIZE, :SIZE]
    dist = np.sqrt((x - cx)**2 + (y - cy)**2)
    mask = dist < r
    # Smooth blob with gaussian profile
    blob = np.exp(-(dist**2) / (2 * (r * 0.5)**2)) * rng.uniform(0.5, 1.0)
    grid = np.maximum(grid, blob * mask)

print(f"Initial mass: {grid.sum():.0f}, active: {(grid > 0.05).sum()}")

# ── Simulation step ───────────────────────────────────────────────────────────
def step(grid):
    """Advance SmoothLife by one timestep."""
    grid_fft = np.fft.fft2(grid)

    # Compute inner (self) and outer (neighborhood) averages
    m = np.real(np.fft.ifft2(grid_fft * inner_fft))  # inner disk average
    n = np.real(np.fft.ifft2(grid_fft * outer_fft))  # outer ring average

    # Compute target state
    target = transition(n, m)

    # Differential update toward target
    grid = np.clip(grid + DT * (2.0 * target - 1.0), 0.0, 1.0)

    return grid

# ── Burn-in ───────────────────────────────────────────────────────────────────
BURNIN = 100
print(f"Running {BURNIN}-step burn-in...")
for i in range(BURNIN):
    grid = step(grid)
    if (i + 1) % 25 == 0:
        mass = grid.sum()
        alive = (grid > 0.05).sum()
        print(f"  Step {i+1}: mass={mass:.0f}, active={alive}")

mass = grid.sum()
alive = (grid > 0.05).sum()
print(f"After burn-in — mass: {mass:.0f}, active: {alive}")

# Safety: if everything died, re-seed
if mass < 50:
    print("Grid collapsed — re-seeding with different parameters...")
    grid = np.zeros((SIZE, SIZE))
    for _ in range(100):
        cx = rng.integers(0, SIZE)
        cy = rng.integers(0, SIZE)
        r = rng.uniform(8, 30)
        y, x = np.ogrid[:SIZE, :SIZE]
        dist = np.sqrt((x - cx)**2 + (y - cy)**2)
        blob = np.exp(-(dist**2) / (2 * (r * 0.4)**2)) * rng.uniform(0.4, 0.9)
        grid = np.maximum(grid, blob * (dist < r))

# ── Custom colormap ───────────────────────────────────────────────────────────
colors_list = [
    (0.00, '#000005'),
    (0.05, '#0d0829'),
    (0.15, '#1b0c5a'),
    (0.25, '#4a0c6b'),
    (0.40, '#781c6d'),
    (0.55, '#b63679'),
    (0.70, '#ed6925'),
    (0.85, '#fbb61a'),
    (1.00, '#fcffa4'),
]
cmap = LinearSegmentedColormap.from_list(
    'smoothlife', [(pos, color) for pos, color in colors_list]
)

# ── Set up figure ─────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(20, 20), facecolor='black')
ax.set_facecolor('black')
ax.set_axis_off()

img = ax.imshow(grid, cmap=cmap, vmin=0, vmax=1,
                interpolation='bilinear', aspect='equal')
plt.tight_layout(pad=0)

# ── Animation function ───────────────────────────────────────────────────────
def animate(frame):
    global grid

    grid = step(grid)
    img.set_data(grid)

    if (frame + 1) % FPS == 0:
        sec = (frame + 1) // FPS
        alive = (grid > 0.05).sum()
        mass = grid.sum()
        print(f"  {sec}s / {DURATION}s  |  active: {alive}  |  mass: {mass:.0f}")

    return img,

# ── Render ────────────────────────────────────────────────────────────────────
os.makedirs('output', exist_ok=True)

print("Rendering animation...")
anim = FuncAnimation(fig, animate, frames=TOTAL_FRAMES, interval=1000 // FPS, blit=True)

writer = FFMpegWriter(fps=FPS, metadata={'title': 'SmoothLife / Lenia'}, bitrate=5000)
output_path = './output/lenia.mp4'
anim.save(output_path, writer=writer, savefig_kwargs={'facecolor': 'black'})
print(f"\nSaved to {output_path}")
