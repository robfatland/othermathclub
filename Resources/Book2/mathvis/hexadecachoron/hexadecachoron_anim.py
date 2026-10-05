"""
Animated 16-cell (hexadecachoron): The 4D analog of the octahedron.
8 vertices, 24 edges, 32 triangular faces, 16 tetrahedral cells.
Dual of the tesseract.

The 16-cell's vertices are the 8 points at ±1 along each of the 4 axes.
Two vertices are connected by an edge if they are NOT antipodal (i.e.,
every pair except the 4 axis-opposite pairs).

The 16-cell tumbles continuously in 4D via simultaneous rotations in
multiple planes, projected to 3D via perspective projection. Edges are
colored by which axis pair their endpoints span.

Output is an MP4 file.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection
from matplotlib.animation import FuncAnimation, FFMpegWriter

# ── 16-cell geometry ──────────────────────────────────────────────────────────
# 8 vertices: ±1 along each of the 4 coordinate axes
vertices_4d = np.array([
    [ 1,  0,  0,  0],
    [-1,  0,  0,  0],
    [ 0,  1,  0,  0],
    [ 0, -1,  0,  0],
    [ 0,  0,  1,  0],
    [ 0,  0, -1,  0],
    [ 0,  0,  0,  1],
    [ 0,  0,  0, -1],
], dtype=float)

# Scale up for visibility
vertices_4d *= 1.5

# Edges: connect every pair of vertices EXCEPT antipodal pairs.
# Antipodal pairs are (0,1), (2,3), (4,5), (6,7).
antipodal = {(0,1), (1,0), (2,3), (3,2), (4,5), (5,4), (6,7), (7,6)}

edges = []
for i in range(8):
    for j in range(i + 1, 8):
        if (i, j) not in antipodal:
            edges.append((i, j))

print(f"16-cell: {len(vertices_4d)} vertices, {len(edges)} edges")

# ── Classify edges for coloring ───────────────────────────────────────────────
# Each vertex sits on one axis. An edge connects two different axes.
# There are C(4,2) = 6 axis pairs. Each pair has 4 edges (2 signs × 2 signs).
# Color by which pair of axes the edge spans.

def vertex_axis(idx):
    """Return which axis (0-3) vertex idx lies on."""
    return idx // 2

# 6 axis-pair colors
PAIR_COLORS = {
    (0, 1): (1.0, 0.92, 0.0, 0.9),   # yellow    (x-y)
    (0, 2): (0.2, 0.5, 1.0, 0.9),    # blue      (x-z)
    (0, 3): (1.0, 0.3, 0.2, 0.9),    # red       (x-w)
    (1, 2): (0.0, 0.9, 0.4, 0.9),    # green     (y-z)
    (1, 3): (0.9, 0.2, 0.9, 0.9),    # magenta   (y-w)
    (2, 3): (0.0, 0.9, 0.9, 0.9),    # cyan      (z-w)
}

edge_colors = []
for i, j in edges:
    pair = tuple(sorted([vertex_axis(i), vertex_axis(j)]))
    edge_colors.append(PAIR_COLORS[pair])

# ── 4D rotation matrices ─────────────────────────────────────────────────────
def rot_xw(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([
        [ c,  0,  0, -s],
        [ 0,  1,  0,  0],
        [ 0,  0,  1,  0],
        [ s,  0,  0,  c],
    ])

def rot_yz(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([
        [ 1,  0,  0,  0],
        [ 0,  c, -s,  0],
        [ 0,  s,  c,  0],
        [ 0,  0,  0,  1],
    ])

def rot_yw(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([
        [ 1,  0,  0,  0],
        [ 0,  c,  0, -s],
        [ 0,  0,  1,  0],
        [ 0,  s,  0,  c],
    ])

def rot_zw(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([
        [ 1,  0,  0,  0],
        [ 0,  1,  0,  0],
        [ 0,  0,  c, -s],
        [ 0,  0,  s,  c],
    ])

def rot_xy(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([
        [ c, -s,  0,  0],
        [ s,  c,  0,  0],
        [ 0,  0,  1,  0],
        [ 0,  0,  0,  1],
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

# ── Set up figure (2x bigger, no coordinate system) ──────────────────────────
fig = plt.figure(figsize=(20, 20), facecolor='black')
ax = fig.add_subplot(111, projection='3d', facecolor='black')
ax.set_axis_off()

lim = 2.5
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
    angle_xw = 2 * np.pi * t * 1.0
    angle_yz = 2 * np.pi * t * 0.7
    angle_yw = 2 * np.pi * t * 0.45
    angle_zw = 2 * np.pi * t * 0.3
    angle_xy = 2 * np.pi * t * 0.55

    R = rot_xw(angle_xw) @ rot_yz(angle_yz) @ rot_yw(angle_yw) @ rot_zw(angle_zw) @ rot_xy(angle_xy)
    rotated_4d = (R @ vertices_4d.T).T

    # Project to 3D
    projected, w_coords = project_4d_to_3d(rotated_4d, distance=4.0)

    # Draw edges with fixed colors, thin lines
    segments = []
    seg_colors = []
    for idx, (i, j) in enumerate(edges):
        segments.append([projected[i], projected[j]])
        seg_colors.append(edge_colors[idx])

    lc = Line3DCollection(segments, colors=seg_colors, linewidths=1.2, alpha=0.9)
    ax.add_collection3d(lc)

    # Draw vertices as white dots
    ax.scatter(projected[:, 0], projected[:, 1], projected[:, 2],
               color='white', s=60, alpha=0.95, zorder=5,
               edgecolors='gray', linewidths=0.3)

    # Camera orbit
    azim = 30 + 360 * t
    elev = 20 + 15 * np.sin(2 * np.pi * t * 1.5)
    ax.view_init(elev=elev, azim=azim)

    if (frame + 1) % FPS == 0:
        sec = (frame + 1) // FPS
        print(f"  {sec}s / {DURATION}s rendered")

# ── Render ────────────────────────────────────────────────────────────────────
print("Rendering animation...")
anim = FuncAnimation(fig, animate, frames=TOTAL_FRAMES, interval=1000 // FPS, blit=False)

writer = FFMpegWriter(fps=FPS, metadata={'title': '16-cell (Hexadecachoron)'}, bitrate=3000)
output_path = '/output/hexadecachoron.mp4'
anim.save(output_path, writer=writer, savefig_kwargs={'facecolor': 'black'})
print(f"\nSaved to {output_path}")
