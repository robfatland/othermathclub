"""
Animated 120-cell (hecatonicosachoron): The 4D analog of the dodecahedron.
600 vertices, 1200 edges, 720 pentagonal faces, 120 dodecahedral cells.

The 120-cell tumbles continuously in 4D via simultaneous rotations in
multiple planes, projected to 3D via perspective projection. Edges are
colored by their 4D depth (w-coordinate after rotation) using a bright
colormap for visibility against black.

Output: ./output/hecatonicosachoron.mp4
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection
from matplotlib.animation import FuncAnimation, FFMpegWriter
import matplotlib.cm as cm
import os

# ── 120-cell geometry ─────────────────────────────────────────────────────────
phi = (1 + np.sqrt(5)) / 2
phi2 = phi * phi
phi3 = phi * phi * phi
inv_phi = 1 / phi
inv_phi2 = 1 / phi2

def even_perms_all_signs(coords):
    from itertools import permutations
    results = set()
    all_perms = list(permutations([0, 1, 2, 3]))
    for p in all_perms:
        inversions = sum(1 for i in range(4) for j in range(i+1, 4) if p[i] > p[j])
        if inversions % 2 == 0:
            vals = [coords[p[k]] for k in range(4)]
            for s0 in (1, -1):
                for s1 in (1, -1):
                    for s2 in (1, -1):
                        for s3 in (1, -1):
                            results.add((s0*vals[0], s1*vals[1], s2*vals[2], s3*vals[3]))
    return results

def all_perms_all_signs(coords):
    from itertools import permutations
    results = set()
    for perm in permutations(coords):
        for s0 in (1, -1):
            for s1 in (1, -1):
                for s2 in (1, -1):
                    for s3 in (1, -1):
                        results.add((s0*perm[0], s1*perm[1], s2*perm[2], s3*perm[3]))
    return results

# Build vertex set
vertex_set = set()
sqrt5 = np.sqrt(5)

vertex_set |= all_perms_all_signs((0, 0, 2, 2))
vertex_set |= all_perms_all_signs((1, 1, 1, sqrt5))
vertex_set |= all_perms_all_signs((inv_phi2, phi, phi, phi))
vertex_set |= all_perms_all_signs((inv_phi, inv_phi, inv_phi, phi2))
vertex_set |= even_perms_all_signs((0, inv_phi2, 1, phi2))
vertex_set |= even_perms_all_signs((0, inv_phi, phi, sqrt5))
vertex_set |= even_perms_all_signs((inv_phi, 1, phi, 2))

vertices_4d = np.array(list(vertex_set), dtype=float)

# Deduplicate
rounded = np.round(vertices_4d, decimals=8)
_, unique_idx = np.unique(rounded, axis=0, return_index=True)
vertices_4d = vertices_4d[unique_idx]

print(f"120-cell: {len(vertices_4d)} vertices")

# Normalize to common radius
radii = np.linalg.norm(vertices_4d, axis=1)
target_radius = np.median(radii)
vertices_4d = vertices_4d / radii[:, np.newaxis] * target_radius

# Find edge length and build edges via KD-tree
dists_from_0 = np.linalg.norm(vertices_4d - vertices_4d[0], axis=1)
dists_from_0_nonzero = dists_from_0[dists_from_0 > 1e-8]
edge_length = dists_from_0_nonzero.min()
print(f"Edge length: {edge_length:.6f}")

from scipy.spatial import cKDTree
tree = cKDTree(vertices_4d)
pairs = tree.query_pairs(r=edge_length * 1.01)
edges = list(pairs)
print(f"120-cell: {len(edges)} edges")

# ── 4D rotation matrices ─────────────────────────────────────────────────────
def rot_xw(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[ c, 0, 0,-s],[ 0, 1, 0, 0],[ 0, 0, 1, 0],[ s, 0, 0, c]])

def rot_yz(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[ 1, 0, 0, 0],[ 0, c,-s, 0],[ 0, s, c, 0],[ 0, 0, 0, 1]])

def rot_yw(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[ 1, 0, 0, 0],[ 0, c, 0,-s],[ 0, 0, 1, 0],[ 0, s, 0, c]])

def rot_zw(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[ 1, 0, 0, 0],[ 0, 1, 0, 0],[ 0, 0, c,-s],[ 0, 0, s, c]])

def rot_xy(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[ c,-s, 0, 0],[ s, c, 0, 0],[ 0, 0, 1, 0],[ 0, 0, 0, 1]])

# ── Perspective projection ────────────────────────────────────────────────────
def project_4d_to_3d(points_4d, distance=5.0):
    w = points_4d[:, 3]
    scale = distance / (distance - w)
    projected = points_4d[:, :3] * scale[:, np.newaxis]
    return projected, w

# ── Animation config ─────────────────────────────────────────────────────────
FPS = 30
DURATION = 30
TOTAL_FRAMES = FPS * DURATION

print(f"Total frames: {TOTAL_FRAMES}")
print(f"Duration: {DURATION}s at {FPS} fps")

# Bright colormap — plasma is vivid from purple through yellow
colormap = cm.plasma

# ── Set up figure ─────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(20, 20), facecolor='black')
ax = fig.add_subplot(111, projection='3d', facecolor='black')
ax.set_axis_off()

lim = 3.5
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

    angle_xw = 2 * np.pi * t * 0.5
    angle_yz = 2 * np.pi * t * 0.309
    angle_yw = 2 * np.pi * t * 0.2
    angle_zw = 2 * np.pi * t * 0.13
    angle_xy = 2 * np.pi * t * 0.17

    R = rot_xw(angle_xw) @ rot_yz(angle_yz) @ rot_yw(angle_yw) @ rot_zw(angle_zw) @ rot_xy(angle_xy)
    rotated_4d = (R @ vertices_4d.T).T

    projected, w_coords = project_4d_to_3d(rotated_4d, distance=5.0)

    w_min, w_max = w_coords.min(), w_coords.max()
    w_range = w_max - w_min
    if w_range < 1e-8:
        w_norm = np.full(len(w_coords), 0.5)
    else:
        w_norm = (w_coords - w_min) / w_range

    segments = []
    seg_colors = []
    for i, j in edges:
        segments.append([projected[i], projected[j]])
        avg_w = (w_norm[i] + w_norm[j]) / 2
        seg_colors.append(colormap(avg_w))

    lc = Line3DCollection(segments, colors=seg_colors, linewidths=1.8, alpha=1.0)
    ax.add_collection3d(lc)

    azim = 30 + 180 * t
    elev = 15 + 15 * np.sin(2 * np.pi * t)
    ax.view_init(elev=elev, azim=azim)

    if (frame + 1) % FPS == 0:
        sec = (frame + 1) // FPS
        print(f"  {sec}s / {DURATION}s rendered")

# ── Render ────────────────────────────────────────────────────────────────────
os.makedirs('output', exist_ok=True)

print("Rendering animation...")
anim = FuncAnimation(fig, animate, frames=TOTAL_FRAMES, interval=1000 // FPS, blit=False)

writer = FFMpegWriter(fps=FPS, metadata={'title': '120-cell (Hecatonicosachoron)'}, bitrate=5000)
output_path = './output/hecatonicosachoron.mp4'
anim.save(output_path, writer=writer, savefig_kwargs={'facecolor': 'black'})
print(f"\nSaved to {output_path}")
