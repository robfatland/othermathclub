"""
Animated 24-cell (icositetrachoron): The "surprise" regular 4-polytope
with no 3D analog. 24 vertices, 96 edges, 96 triangular faces,
24 octahedral cells. Self-dual.

The 24-cell tumbles continuously in 4D via simultaneous rotations in
multiple planes, projected to 3D via perspective projection. Edges are
colored by fixed structural groups based on the vertex coordinate pattern.

Output is an MP4 file.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection
from matplotlib.animation import FuncAnimation, FFMpegWriter
import matplotlib.cm as cm

# ── 24-cell geometry ──────────────────────────────────────────────────────────
# The 24-cell has 24 vertices which can be described as the 24 unit quaternions
# forming the binary tetrahedral group. In Cartesian coordinates, they are:
#
# 8 vertices: permutations of (±1, 0, 0, 0)  — the 4D cross-polytope vertices
# 16 vertices: all combinations of (±½, ±½, ±½, ±½)  — the 4D hypercube vertices (scaled)
#
# All 24 vertices lie on the unit 3-sphere.

# Type A: permutations of (±1, 0, 0, 0) — 8 vertices
type_a = []
for axis in range(4):
    for sign in (-1, 1):
        v = [0.0, 0.0, 0.0, 0.0]
        v[axis] = sign
        type_a.append(v)

# Type B: all (±½, ±½, ±½, ±½) — 16 vertices
type_b = []
for s0 in (-0.5, 0.5):
    for s1 in (-0.5, 0.5):
        for s2 in (-0.5, 0.5):
            for s3 in (-0.5, 0.5):
                type_b.append([s0, s1, s2, s3])

vertices_4d = np.array(type_a + type_b, dtype=float)

# Scale up for better visibility (edge length ≈ 2)
vertices_4d *= 2.0

print(f"24-cell: {len(vertices_4d)} vertices")

# Edges: two vertices are connected if their distance equals the edge length.
# For the unit 24-cell, edge length = 1. After scaling by 2, edge length = 2.
# Compute all pairwise distances and find the minimum nonzero one.
from scipy.spatial.distance import pdist, squareform

dist_matrix = squareform(pdist(vertices_4d))
# Find the edge length (smallest nonzero distance)
nonzero_dists = dist_matrix[dist_matrix > 1e-8]
edge_length = nonzero_dists.min()
print(f"Edge length: {edge_length:.4f}")

# Build edge list
edges = []
for i in range(24):
    for j in range(i + 1, 24):
        if abs(dist_matrix[i, j] - edge_length) < 1e-6:
            edges.append((i, j))

print(f"24-cell: {len(edges)} edges")

# ── Classify edges into structural groups for coloring ────────────────────────
# Group edges by the types of their endpoints:
#   A-A: both endpoints are type A (axis-aligned vertices, indices 0-7)
#   B-B: both endpoints are type B (half-integer vertices, indices 8-23)
#   A-B: one of each type

edges_aa = []
edges_bb = []
edges_ab = []

for idx, (i, j) in enumerate(edges):
    i_is_a = i < 8
    j_is_a = j < 8
    if i_is_a and j_is_a:
        edges_aa.append(idx)
    elif not i_is_a and not j_is_a:
        edges_bb.append(idx)
    else:
        edges_ab.append(idx)

print(f"Edge groups: {len(edges_aa)} A-A, {len(edges_bb)} B-B, {len(edges_ab)} A-B")

# ── Assign fixed colors ──────────────────────────────────────────────────────
# A-A edges (cross-polytope skeleton): gold/amber
# B-B edges (hypercube skeleton): electric blue
# A-B edges (connectors): warm white/silver

COLOR_AA = (1.0, 0.75, 0.1, 0.9)    # gold
COLOR_BB = (0.2, 0.5, 1.0, 0.9)     # electric blue
COLOR_AB = (0.85, 0.85, 0.9, 0.7)   # silver/white (slightly transparent)

edge_colors = [None] * len(edges)
for idx in edges_aa:
    edge_colors[idx] = COLOR_AA
for idx in edges_bb:
    edge_colors[idx] = COLOR_BB
for idx in edges_ab:
    edge_colors[idx] = COLOR_AB

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
def project_4d_to_3d(points_4d, distance=5.0):
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

lim = 3.0
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
    angle_yz = 2 * np.pi * t * 0.618   # golden ratio for nice aperiodicity
    angle_yw = 2 * np.pi * t * 0.4
    angle_zw = 2 * np.pi * t * 0.25
    angle_xy = 2 * np.pi * t * 0.33

    R = rot_xw(angle_xw) @ rot_yz(angle_yz) @ rot_yw(angle_yw) @ rot_zw(angle_zw) @ rot_xy(angle_xy)
    rotated_4d = (R @ vertices_4d.T).T

    # Project to 3D
    projected, w_coords = project_4d_to_3d(rotated_4d, distance=5.0)

    # Draw edges with fixed structural colors
    segments = []
    seg_colors = []
    for idx, (i, j) in enumerate(edges):
        segments.append([projected[i], projected[j]])
        seg_colors.append(edge_colors[idx])

    lc = Line3DCollection(segments, colors=seg_colors, linewidths=2.5, alpha=0.85)
    ax.add_collection3d(lc)

    # Draw vertices: type A (gold) and type B (blue) dots
    proj_a = projected[:8]
    proj_b = projected[8:]
    ax.scatter(proj_a[:, 0], proj_a[:, 1], proj_a[:, 2],
               color=COLOR_AA[:3], s=40, alpha=0.95, zorder=5,
               edgecolors='white', linewidths=0.3)
    ax.scatter(proj_b[:, 0], proj_b[:, 1], proj_b[:, 2],
               color=COLOR_BB[:3], s=25, alpha=0.9, zorder=5,
               edgecolors='white', linewidths=0.3)

    # Camera orbit
    azim = 30 + 360 * t
    elev = 15 + 20 * np.sin(2 * np.pi * t * 1.5)
    ax.view_init(elev=elev, azim=azim)

    if (frame + 1) % FPS == 0:
        sec = (frame + 1) // FPS
        print(f"  {sec}s / {DURATION}s rendered")

# ── Render ────────────────────────────────────────────────────────────────────
print("Rendering animation...")
anim = FuncAnimation(fig, animate, frames=TOTAL_FRAMES, interval=1000 // FPS, blit=False)

writer = FFMpegWriter(fps=FPS, metadata={'title': '24-cell (Icositetrachoron)'}, bitrate=3000)
output_path = '/output/icositetrachoron.mp4'
anim.save(output_path, writer=writer, savefig_kwargs={'facecolor': 'black'})
print(f"\nSaved to {output_path}")
