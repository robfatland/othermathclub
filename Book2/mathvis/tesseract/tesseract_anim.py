"""
Animated tesseract (4D hypercube): The hypercube performs a sequence of
discrete 90-degree rotations in 4D. Each rotation is in a randomly chosen
plane involving the w-axis, producing the visual effect of one face of the
inner cube passing through the corresponding face of the outer cube.
Between rotations, the tesseract rests at its "home position" where it
appears as two concentric cubes connected at vertices.

Each edge has a fixed color throughout the animation:
- Outer cube edges (12): bright yellow
- Inner cube edges (12): deep blue (contrast)
- Connecting edges (8): each a unique color

Output is an MP4 file.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection
from matplotlib.animation import FuncAnimation, FFMpegWriter

# ── Tesseract geometry ────────────────────────────────────────────────────────
# 16 vertices of a 4D hypercube: all combinations of ±1 in 4 dimensions
vertices_4d = np.array([[x, y, z, w]
                        for x in (-1, 1)
                        for y in (-1, 1)
                        for z in (-1, 1)
                        for w in (-1, 1)], dtype=float)

# Edges connect vertices that differ in exactly one coordinate (Hamming distance 1)
edges = []
for i in range(16):
    for j in range(i + 1, 16):
        diff = np.sum(np.abs(vertices_4d[i] - vertices_4d[j]))
        if diff == 2:  # ±1 differs in one coord → distance = 2
            edges.append((i, j))

print(f"Tesseract: {len(vertices_4d)} vertices, {len(edges)} edges")

# ── Classify edges by their role in the home position ─────────────────────────
# In the home position (no rotation applied):
#   w = +1 vertices project as the OUTER cube (larger perspective scale)
#   w = -1 vertices project as the INNER cube (smaller perspective scale)
#   Edges connecting w=+1 to w=-1 are the 8 connective edges

outer_edges = []   # both endpoints have w = +1
inner_edges = []   # both endpoints have w = -1
connect_edges = [] # one endpoint w = +1, one w = -1

for idx, (i, j) in enumerate(edges):
    wi = vertices_4d[i, 3]
    wj = vertices_4d[j, 3]
    if wi == 1 and wj == 1:
        outer_edges.append(idx)
    elif wi == -1 and wj == -1:
        inner_edges.append(idx)
    else:
        connect_edges.append(idx)

print(f"Edge classification: {len(outer_edges)} outer, {len(inner_edges)} inner, {len(connect_edges)} connecting")

# ── Assign fixed colors to each edge ─────────────────────────────────────────
# Outer cube: bright yellow
YELLOW = (1.0, 0.92, 0.0, 1.0)

# Inner cube: deep blue (high contrast against yellow on black)
BLUE = (0.1, 0.4, 1.0, 1.0)

# 8 connecting edges: unique colors from a perceptually distinct palette
CONNECT_COLORS = [
    (1.0, 0.2, 0.2, 1.0),   # red
    (0.0, 0.9, 0.4, 1.0),   # green
    (0.9, 0.1, 0.9, 1.0),   # magenta
    (0.0, 0.9, 0.9, 1.0),   # cyan
    (1.0, 0.5, 0.0, 1.0),   # orange
    (0.6, 1.0, 0.2, 1.0),   # lime
    (0.8, 0.4, 1.0, 1.0),   # violet
    (1.0, 0.7, 0.8, 1.0),   # pink
]

# Build the color array indexed by edge position
edge_colors = [None] * len(edges)
for idx in outer_edges:
    edge_colors[idx] = YELLOW
for idx in inner_edges:
    edge_colors[idx] = BLUE
for k, idx in enumerate(connect_edges):
    edge_colors[idx] = CONNECT_COLORS[k]

# ── 4D rotation matrix in an arbitrary plane involving w ──────────────────────
def rot_4d(plane, theta):
    """
    Rotation by angle theta in one of 6 planes involving the w-axis.
    Planes: 'xw+', 'xw-', 'yw+', 'yw-', 'zw+', 'zw-'
    The sign indicates direction of rotation.
    """
    c, s = np.cos(theta), np.sin(theta)
    R = np.eye(4)

    axis = plane[0]  # 'x', 'y', or 'z'
    sign = 1 if plane[2] == '+' else -1
    s *= sign

    if axis == 'x':
        R[0, 0] = c;  R[0, 3] = -s
        R[3, 0] = s;  R[3, 3] = c
    elif axis == 'y':
        R[1, 1] = c;  R[1, 3] = -s
        R[3, 1] = s;  R[3, 3] = c
    elif axis == 'z':
        R[2, 2] = c;  R[2, 3] = -s
        R[3, 2] = s;  R[3, 3] = c

    return R

# All 6 possible "face-through-face" rotation choices
ROTATION_PLANES = ['xw+', 'xw-', 'yw+', 'yw-', 'zw+', 'zw-']

# ── Perspective projection from 4D to 3D ─────────────────────────────────────
def project_4d_to_3d(points_4d, distance=3.0):
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

# Each 90-degree transformation takes this many seconds
TRANSFORM_SECONDS = 2.0
FRAMES_PER_TRANSFORM = int(FPS * TRANSFORM_SECONDS)

# How many transformations fit in the total duration
NUM_TRANSFORMS = TOTAL_FRAMES // FRAMES_PER_TRANSFORM

# Pre-generate the random sequence of rotation planes
rng = np.random.default_rng(seed=42)
transform_sequence = rng.choice(ROTATION_PLANES, size=NUM_TRANSFORMS)

print(f"Total frames: {TOTAL_FRAMES}")
print(f"Duration: {DURATION}s at {FPS} fps")
print(f"Transforms: {NUM_TRANSFORMS} (each {TRANSFORM_SECONDS}s)")
print(f"Sequence: {list(transform_sequence[:10])}...")

# ── Easing function ──────────────────────────────────────────────────────────
def ease_in_out(t):
    """Smooth ease-in-out (cubic)."""
    if t < 0.5:
        return 4 * t * t * t
    else:
        return 1 - (-2 * t + 2) ** 3 / 2

# ── Set up figure (no coordinate system) ─────────────────────────────────────
fig = plt.figure(figsize=(10, 10), facecolor='black')
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

    # Determine which transformation we're in and how far through it
    transform_idx = frame // FRAMES_PER_TRANSFORM
    frame_within = frame % FRAMES_PER_TRANSFORM
    t_local = frame_within / FRAMES_PER_TRANSFORM  # 0 to 1

    # Apply easing for smooth acceleration/deceleration
    eased_t = ease_in_out(t_local)

    # The rotation angle goes from 0 to pi/2 (90 degrees) within each transform
    angle = eased_t * (np.pi / 2)

    # Get the current rotation plane
    if transform_idx < NUM_TRANSFORMS:
        plane = transform_sequence[transform_idx]
    else:
        plane = transform_sequence[-1]

    # Build the cumulative rotation: all previous transforms are at pi/2,
    # plus the current one at the interpolated angle
    R_total = np.eye(4)
    for i in range(min(transform_idx, NUM_TRANSFORMS)):
        R_total = rot_4d(transform_sequence[i], np.pi / 2) @ R_total
    # Add current in-progress rotation
    R_total = rot_4d(plane, angle) @ R_total

    rotated_4d = (R_total @ vertices_4d.T).T

    # Project to 3D
    projected, w_coords = project_4d_to_3d(rotated_4d, distance=3.0)

    # Draw edges with fixed colors
    segments = []
    seg_colors = []
    for idx, (i, j) in enumerate(edges):
        segments.append([projected[i], projected[j]])
        seg_colors.append(edge_colors[idx])

    lc = Line3DCollection(segments, colors=seg_colors, linewidths=6.0, alpha=0.85)
    ax.add_collection3d(lc)

    # Draw vertices (white dots)
    ax.scatter(projected[:, 0], projected[:, 1], projected[:, 2],
               color='white', s=40, alpha=0.9, zorder=5)

    # Slow camera orbit
    global_t = frame / TOTAL_FRAMES
    azim = 45 + 180 * global_t
    elev = 20 + 10 * np.sin(2 * np.pi * global_t)
    ax.view_init(elev=elev, azim=azim)

    if (frame + 1) % FPS == 0:
        sec = (frame + 1) // FPS
        print(f"  {sec}s / {DURATION}s rendered")

# ── Render ────────────────────────────────────────────────────────────────────
print("Rendering animation...")
anim = FuncAnimation(fig, animate, frames=TOTAL_FRAMES, interval=1000 // FPS, blit=False)

writer = FFMpegWriter(fps=FPS, metadata={'title': 'Tesseract'}, bitrate=3000)
output_path = '/output/tesseract.mp4'
anim.save(output_path, writer=writer, savefig_kwargs={'facecolor': 'black'})
print(f"\nSaved to {output_path}")
