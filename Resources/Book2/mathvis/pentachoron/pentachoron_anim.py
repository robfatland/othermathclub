"""
Animated 5-cell (pentachoron): The 4D analog of the tetrahedron.
5 vertices, 10 edges (every vertex connected to every other — K₅).
10 triangular faces, 5 tetrahedral cells.

The 5-cell tumbles continuously in 4D via simultaneous rotations in
multiple planes, projected to 3D via perspective projection. Each of
the 10 edges has a unique fixed color throughout the animation.

Output is an MP4 file.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection
from matplotlib.animation import FuncAnimation, FFMpegWriter

# ── 5-cell geometry ───────────────────────────────────────────────────────────
# The 5-cell can be constructed as a regular simplex in 4D.
# One standard embedding: place vertices at the 5 points of a regular simplex
# centered at the origin in R⁴.
#
# Start with the standard simplex vertices in R⁵ (unit vectors e₁..e₅),
# then project to a 4D hyperplane through the centroid.
# Alternatively, use these known coordinates for a regular 5-cell centered
# at the origin with unit edge length (scaled up for visibility):

# Regular simplex in 4D: vertices equidistant from origin and from each other
# Using the construction: take the 4D simplex with vertices at
# permutations/combinations that give equal distances.
_raw = np.array([
    [ 1,  1,  1, -1/np.sqrt(5)],
    [ 1, -1, -1, -1/np.sqrt(5)],
    [-1,  1, -1, -1/np.sqrt(5)],
    [-1, -1,  1, -1/np.sqrt(5)],
    [ 0,  0,  0, np.sqrt(5) - 1/np.sqrt(5)],
], dtype=float)

# Center at origin and normalize so edge length ≈ 2 for good visual scale
centroid = _raw.mean(axis=0)
vertices_4d = _raw - centroid

# Scale so the edge length is about 2 (matching tesseract visual scale)
edge_len = np.linalg.norm(vertices_4d[0] - vertices_4d[1])
vertices_4d *= 2.0 / edge_len

# Verify regularity
distances = []
for i in range(5):
    for j in range(i+1, 5):
        distances.append(np.linalg.norm(vertices_4d[i] - vertices_4d[j]))
print(f"5-cell edge lengths: min={min(distances):.4f}, max={max(distances):.4f} (should be equal)")

# All 10 edges: complete graph on 5 vertices
edges = [(i, j) for i in range(5) for j in range(i+1, 5)]
print(f"5-cell: {len(vertices_4d)} vertices, {len(edges)} edges")

# ── Assign fixed unique colors to each edge ───────────────────────────────────
# 10 distinct colors on a black background
EDGE_COLORS = [
    (1.0, 0.92, 0.0, 1.0),   # yellow
    (0.1, 0.4, 1.0, 1.0),    # blue
    (1.0, 0.2, 0.2, 1.0),    # red
    (0.0, 0.9, 0.4, 1.0),    # green
    (0.9, 0.1, 0.9, 1.0),    # magenta
    (0.0, 0.9, 0.9, 1.0),    # cyan
    (1.0, 0.5, 0.0, 1.0),    # orange
    (0.6, 1.0, 0.2, 1.0),    # lime
    (0.8, 0.4, 1.0, 1.0),    # violet
    (1.0, 0.7, 0.8, 1.0),    # pink
]

# ── 4D rotation matrices ─────────────────────────────────────────────────────
def rot_xy(theta):
    """Rotation in the XY plane."""
    c, s = np.cos(theta), np.sin(theta)
    return np.array([
        [ c, -s,  0,  0],
        [ s,  c,  0,  0],
        [ 0,  0,  1,  0],
        [ 0,  0,  0,  1],
    ])

def rot_xw(theta):
    """Rotation in the XW plane."""
    c, s = np.cos(theta), np.sin(theta)
    return np.array([
        [ c,  0,  0, -s],
        [ 0,  1,  0,  0],
        [ 0,  0,  1,  0],
        [ s,  0,  0,  c],
    ])

def rot_yz(theta):
    """Rotation in the YZ plane."""
    c, s = np.cos(theta), np.sin(theta)
    return np.array([
        [ 1,  0,  0,  0],
        [ 0,  c, -s,  0],
        [ 0,  s,  c,  0],
        [ 0,  0,  0,  1],
    ])

def rot_yw(theta):
    """Rotation in the YW plane."""
    c, s = np.cos(theta), np.sin(theta)
    return np.array([
        [ 1,  0,  0,  0],
        [ 0,  c,  0, -s],
        [ 0,  0,  1,  0],
        [ 0,  s,  0,  c],
    ])

def rot_zw(theta):
    """Rotation in the ZW plane."""
    c, s = np.cos(theta), np.sin(theta)
    return np.array([
        [ 1,  0,  0,  0],
        [ 0,  1,  0,  0],
        [ 0,  0,  c, -s],
        [ 0,  0,  s,  c],
    ])

# ── Perspective projection from 4D to 3D ─────────────────────────────────────
def project_4d_to_3d(points_4d, distance=4.0):
    """
    Perspective projection from 4D to 3D.
    The 'camera' sits at w = -distance, looking toward the origin.
    """
    w = points_4d[:, 3]
    scale = distance / (distance - w)
    projected = points_4d[:, :3] * scale[:, np.newaxis]
    return projected, w

# ── Animation config ─────────────────────────────────────────────────────────
FPS = 30
DURATION = 30  # seconds
TOTAL_FRAMES = FPS * DURATION

print(f"Total frames: {TOTAL_FRAMES}")
print(f"Duration: {DURATION}s at {FPS} fps")

# ── Set up figure (no coordinate system) ─────────────────────────────────────
fig = plt.figure(figsize=(10, 10), facecolor='black')
ax = fig.add_subplot(111, projection='3d', facecolor='black')
ax.set_axis_off()

lim = 2.0
ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)
ax.set_zlim(-lim, lim)

# ── Animation function ───────────────────────────────────────────────────────
def animate(frame):
    ax.cla()
    ax.set_axis_off()
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_zlim(-lim, lim)
    ax.set_facecolor('black')

    t = frame / TOTAL_FRAMES

    # Simultaneous rotations in multiple 4D planes at incommensurate speeds
    # This produces a rich tumbling motion that never exactly repeats
    angle_xw = 2 * np.pi * t * 1.0
    angle_yz = 2 * np.pi * t * 0.7
    angle_yw = 2 * np.pi * t * 0.4
    angle_zw = 2 * np.pi * t * 0.3
    angle_xy = 2 * np.pi * t * 0.5

    R = rot_xw(angle_xw) @ rot_yz(angle_yz) @ rot_yw(angle_yw) @ rot_zw(angle_zw) @ rot_xy(angle_xy)
    rotated_4d = (R @ vertices_4d.T).T

    # Project to 3D
    projected, w_coords = project_4d_to_3d(rotated_4d, distance=4.0)

    # Draw edges with fixed colors
    segments = []
    seg_colors = []
    for idx, (i, j) in enumerate(edges):
        segments.append([projected[i], projected[j]])
        seg_colors.append(EDGE_COLORS[idx])

    lc = Line3DCollection(segments, colors=seg_colors, linewidths=6.0, alpha=0.85)
    ax.add_collection3d(lc)

    # Draw vertices as larger white dots (only 5, so make them prominent)
    ax.scatter(projected[:, 0], projected[:, 1], projected[:, 2],
               color='white', s=80, alpha=0.95, zorder=5,
               edgecolors='gray', linewidths=0.5)

    # Slow camera orbit
    azim = 30 + 360 * t
    elev = 20 + 15 * np.sin(2 * np.pi * t * 2)
    ax.view_init(elev=elev, azim=azim)

    if (frame + 1) % FPS == 0:
        sec = (frame + 1) // FPS
        print(f"  {sec}s / {DURATION}s rendered")

# ── Render ────────────────────────────────────────────────────────────────────
print("Rendering animation...")
anim = FuncAnimation(fig, animate, frames=TOTAL_FRAMES, interval=1000 // FPS, blit=False)

writer = FFMpegWriter(fps=FPS, metadata={'title': '5-cell (Pentachoron)'}, bitrate=3000)
output_path = '/output/pentachoron.mp4'
anim.save(output_path, writer=writer, savefig_kwargs={'facecolor': 'black'})
print(f"\nSaved to {output_path}")
