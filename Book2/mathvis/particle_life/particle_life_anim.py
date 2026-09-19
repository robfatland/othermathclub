"""
Particle Life: N species of particles in continuous 2D space with
asymmetric attraction/repulsion interactions. Each species pair (i, j)
has a single interaction coefficient a[i][j] ∈ [-1, 1] that determines
whether species i is attracted to (+) or repelled by (-) species j.

Simple physics: particles have position and velocity, experience forces
from nearby particles of all species, and are subject to friction.
From these minimal rules, complex emergent structures arise — cells,
pursuit/evasion, symbiotic clusters, and division-like behavior.

Output is an MP4 file.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
from matplotlib.colors import to_rgba

# ── Configuration ─────────────────────────────────────────────────────────────
NUM_SPECIES = 6
PARTICLES_PER_SPECIES = 150
NUM_PARTICLES = NUM_SPECIES * PARTICLES_PER_SPECIES

# World is a toroidal (wrapping) square
WORLD_SIZE = 10.0

# Physics parameters
MAX_RADIUS = 2.5       # interaction range
FRICTION = 0.5         # velocity damping per timestep (0 = no friction, 1 = full stop)
FORCE_SCALE = 0.5      # overall force multiplier
DT = 0.03             # timestep (1.5x faster evolution)

# Interaction force profile: ramps up from 0 at r=0 to peak at r=β,
# then ramps down to 0 at r=MAX_RADIUS
BETA = 0.3            # fraction of MAX_RADIUS where force peaks

# Animation
FPS = 30
DURATION = 180        # seconds
TOTAL_FRAMES = FPS * DURATION
STEPS_PER_FRAME = 4   # physics steps between each rendered frame

print(f"Particles: {NUM_PARTICLES} ({NUM_SPECIES} species × {PARTICLES_PER_SPECIES})")
print(f"Total frames: {TOTAL_FRAMES}, duration: {DURATION}s")
print(f"Physics steps per frame: {STEPS_PER_FRAME}")

# ── Generate random interaction matrix ────────────────────────────────────────
rng = np.random.default_rng(seed=77)

# Interaction coefficients: a[i][j] = how species i feels about species j
# Range [-1, 1]. Asymmetric — a[i][j] ≠ a[j][i] in general.
interaction_matrix = rng.uniform(-1.0, 1.0, size=(NUM_SPECIES, NUM_SPECIES))

# Make self-interaction mildly repulsive (prevents collapse into points)
for i in range(NUM_SPECIES):
    interaction_matrix[i, i] = rng.uniform(-0.5, -0.1)

print("Interaction matrix:")
print(np.array2string(interaction_matrix, precision=2, suppress_small=True))

# ── Initialize particles ──────────────────────────────────────────────────────
# Species assignment
species = np.repeat(np.arange(NUM_SPECIES), PARTICLES_PER_SPECIES)

# Random initial positions
positions = rng.uniform(0, WORLD_SIZE, size=(NUM_PARTICLES, 2))

# Zero initial velocity
velocities = np.zeros((NUM_PARTICLES, 2))

# ── Species colors ────────────────────────────────────────────────────────────
SPECIES_COLORS = [
    '#FF4444',  # red
    '#44FF44',  # green
    '#4488FF',  # blue
    '#FFDD00',  # yellow
    '#FF44FF',  # magenta
    '#00DDDD',  # cyan
]

species_rgba = np.array([to_rgba(c) for c in SPECIES_COLORS])
particle_colors = species_rgba[species]

# ── Force profile ─────────────────────────────────────────────────────────────
def force_magnitude(r, attraction):
    """
    Compute force magnitude given normalized distance r ∈ [0, 1]
    and attraction coefficient ∈ [-1, 1].
    
    Profile:
    - r < β: repulsive core (universal, regardless of attraction)
      ramps from strong repulsion at r=0 to 0 at r=β
    - r ≥ β: interaction region
      ramps from 0 at r=β to attraction at midpoint, back to 0 at r=1
    """
    if r < BETA:
        # Repulsive core: linear ramp from -1 at r=0 to 0 at r=β
        return r / BETA - 1.0
    else:
        # Attraction/repulsion zone: bell-shaped
        # Peak at midpoint between β and 1
        return attraction * (1.0 - abs(2.0 * (r - BETA) / (1.0 - BETA) - 1.0))

# Vectorized version for performance
def compute_forces(positions, species, interaction_matrix):
    """Compute all pairwise forces with toroidal wrapping."""
    N = len(positions)
    forces = np.zeros((N, 2))
    
    for i in range(NUM_SPECIES):
        mask_i = (species == i)
        pos_i = positions[mask_i]
        n_i = pos_i.shape[0]
        
        for j in range(NUM_SPECIES):
            mask_j = (species == j)
            pos_j = positions[mask_j]
            n_j = pos_j.shape[0]
            
            attraction = interaction_matrix[i, j]
            
            # Compute displacement vectors (with toroidal wrapping)
            # Shape: (n_i, n_j, 2)
            dx = pos_j[np.newaxis, :, :] - pos_i[:, np.newaxis, :]
            
            # Wrap to nearest image
            dx = dx - WORLD_SIZE * np.round(dx / WORLD_SIZE)
            
            # Distances
            dist = np.sqrt((dx * dx).sum(axis=2))  # (n_i, n_j)
            
            # Normalized distance (0 to 1 within MAX_RADIUS)
            r_norm = dist / MAX_RADIUS
            
            # Only interact within MAX_RADIUS
            in_range = (r_norm > 0.001) & (r_norm < 1.0)
            
            # Compute force magnitudes
            f_mag = np.zeros_like(dist)
            r_valid = r_norm[in_range]
            
            # Vectorized force profile
            f = np.zeros_like(r_valid)
            core_mask = r_valid < BETA
            shell_mask = ~core_mask
            
            # Core: repulsive
            f[core_mask] = r_valid[core_mask] / BETA - 1.0
            
            # Shell: attraction/repulsion
            r_shell = r_valid[shell_mask]
            f[shell_mask] = attraction * (1.0 - np.abs(2.0 * (r_shell - BETA) / (1.0 - BETA) - 1.0))
            
            f_mag[in_range] = f
            
            # Direction vectors (normalized)
            dx_norm = np.zeros_like(dx)
            safe_dist = np.where(dist > 0.001, dist, 1.0)
            dx_norm[:, :, 0] = dx[:, :, 0] / safe_dist
            dx_norm[:, :, 1] = dx[:, :, 1] / safe_dist
            
            # Sum forces on species i from species j
            force_x = (f_mag * dx_norm[:, :, 0]).sum(axis=1)
            force_y = (f_mag * dx_norm[:, :, 1]).sum(axis=1)
            
            forces[mask_i, 0] += force_x
            forces[mask_i, 1] += force_y
    
    return forces * FORCE_SCALE

# ── Physics step ──────────────────────────────────────────────────────────────
def step(positions, velocities):
    """Advance simulation by one timestep."""
    forces = compute_forces(positions, species, interaction_matrix)
    
    # Update velocity with force and friction
    velocities = velocities * (1.0 - FRICTION) + forces * DT
    
    # Update position
    positions = positions + velocities * DT
    
    # Wrap positions (toroidal boundary)
    positions = positions % WORLD_SIZE
    
    return positions, velocities

# ── Set up figure ─────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(20, 20), facecolor='black')
ax.set_facecolor('black')
ax.set_xlim(0, WORLD_SIZE)
ax.set_ylim(0, WORLD_SIZE)
ax.set_aspect('equal')
ax.set_axis_off()

scatter = ax.scatter(positions[:, 0], positions[:, 1],
                     c=particle_colors, s=12, alpha=0.85, linewidths=0)

# ── Animation function ───────────────────────────────────────────────────────
def animate(frame):
    global positions, velocities
    
    # Run multiple physics steps per frame
    for _ in range(STEPS_PER_FRAME):
        positions, velocities = step(positions, velocities)
    
    scatter.set_offsets(positions)
    
    if (frame + 1) % FPS == 0:
        sec = (frame + 1) // FPS
        print(f"  {sec}s / {DURATION}s rendered")
    
    return scatter,

# ── Render ────────────────────────────────────────────────────────────────────
print("Rendering animation...")
anim = FuncAnimation(fig, animate, frames=TOTAL_FRAMES, interval=1000 // FPS, blit=True)

writer = FFMpegWriter(fps=FPS, metadata={'title': 'Particle Life'}, bitrate=5000)
output_path = '/output/particle_life.mp4'
anim.save(output_path, writer=writer, savefig_kwargs={'facecolor': 'black'})
print(f"\nSaved to {output_path}")
