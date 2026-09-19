"""
Animated Lissajous knots: 3D Lissajous curves with rational frequency
ratios that form knots. The animation sweeps through a sequence of
parameter sets, morphing smoothly between different knot types.

A Lissajous knot is defined by:
    x(t) = cos(n_x * t + phi_x)
    y(t) = cos(n_y * t + phi_y)
    z(t) = cos(n_z * t + phi_z)

where t ∈ [0, 2π] and the frequency ratios n_x:n_y:n_z determine the
knot type. Phase shifts break degeneracies to avoid self-intersections.

The curve is colored by position along its length (parameter t),
making it easy to visually trace the over/under crossings.

Output is an MP4 file.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection
from matplotlib.animation import FuncAnimation, FFMpegWriter
import matplotlib.cm as cm

# ── Lissajous knot parameters ────────────────────────────────────────────────
# Each entry: (nx, ny, nz, phi_x, phi_y, phi_z, name)
# Phase shifts chosen to produce genuine knots (no self-intersections)

KNOT_PARAMS = [
    # Trefoil-like knots
    (2, 3, 5, 0.0, 0.2, 0.7, "2:3:5 knot"),
    (2, 3, 7, 0.0, 0.1, 0.5, "2:3:7 knot"),
    # More complex knots
    (3, 4, 5, 0.1, 0.3, 0.6, "3:4:5 knot"),
    (2, 5, 3, 0.0, 0.4, 0.8, "2:5:3 knot"),
    (3, 5, 7, 0.1, 0.2, 0.5, "3:5:7 knot"),
    # Wilder curves
    (2, 3, 4, 0.0, 0.3, 0.7, "2:3:4 knot"),
    (3, 4, 7, 0.2, 0.1, 0.6, "3:4:7 knot"),
    (2, 5, 7, 0.0, 0.3, 0.9, "2:5:7 knot"),
    (4, 5, 7, 0.1, 0.2, 0.4, "4:5:7 knot"),
    (3, 5, 8, 0.0, 0.3, 0.7, "3:5:8 knot"),
]

NUM_KNOTS = len(KNOT_PARAMS)

# ── Curve generation ──────────────────────────────────────────────────────────
NUM_POINTS = 2000  # points along the curve

def generate_lissajous(nx, ny, nz, phi_x, phi_y, phi_z, num_points=NUM_POINTS):
    """Generate a 3D Lissajous curve."""
    t = np.linspace(0, 2 * np.pi, num_points, endpoint=False)
    x = np.cos(nx * t + phi_x)
    y = np.cos(ny * t + phi_y)
    z = np.cos(nz * t + phi_z)
    return np.column_stack([x, y, z])

def interpolate_params(params_a, params_b, frac):
    """Smoothly interpolate between two parameter sets."""
    nx_a, ny_a, nz_a, px_a, py_a, pz_a, _ = params_a
    nx_b, ny_b, nz_b, px_b, py_b, pz_b, _ = params_b
    # Interpolate frequencies and phases
    nx = nx_a + (nx_b - nx_a) * frac
    ny = ny_a + (ny_b - ny_a) * frac
    nz = nz_a + (nz_b - nz_a) * frac
    px = px_a + (px_b - px_a) * frac
    py = py_a + (py_b - py_a) * frac
    pz = pz_a + (pz_b - pz_a) * frac
    return nx, ny, nz, px, py, pz

# ── Animation config ─────────────────────────────────────────────────────────
FPS = 30
DURATION = 30  # seconds
TOTAL_FRAMES = FPS * DURATION

# Time per knot: hold for a while, then morph to the next
HOLD_SECONDS = 2.0    # seconds showing the stable knot
MORPH_SECONDS = 1.0   # seconds morphing to the next
CYCLE_SECONDS = HOLD_SECONDS + MORPH_SECONDS
FRAMES_PER_CYCLE = int(FPS * CYCLE_SECONDS)
HOLD_FRAMES = int(FPS * HOLD_SECONDS)
MORPH_FRAMES = int(FPS * MORPH_SECONDS)

print(f"Total frames: {TOTAL_FRAMES}")
print(f"Duration: {DURATION}s at {FPS} fps")
print(f"Knots: {NUM_KNOTS}, cycle: {CYCLE_SECONDS}s (hold {HOLD_SECONDS}s + morph {MORPH_SECONDS}s)")

# ── Easing function ──────────────────────────────────────────────────────────
def ease_in_out(t):
    """Smooth ease-in-out (cubic)."""
    if t < 0.5:
        return 4 * t * t * t
    else:
        return 1 - (-2 * t + 2) ** 3 / 2

# ── Colormap for curve parameterization ──────────────────────────────────────
colormap = cm.hsv  # Full hue cycle along the curve length

# Pre-compute the color array (constant — based on position along curve)
t_norm = np.linspace(0, 1, NUM_POINTS)
curve_colors = [colormap(v) for v in t_norm]

# ── Set up figure ─────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(20, 20), facecolor='black')
ax = fig.add_subplot(111, projection='3d', facecolor='black')
ax.set_axis_off()

lim = 1.4
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

    # Determine which knot and whether we're holding or morphing
    cycle_idx = frame // FRAMES_PER_CYCLE
    frame_in_cycle = frame % FRAMES_PER_CYCLE

    knot_idx = cycle_idx % NUM_KNOTS
    next_knot_idx = (knot_idx + 1) % NUM_KNOTS

    if frame_in_cycle < HOLD_FRAMES:
        # Holding on current knot
        params = KNOT_PARAMS[knot_idx]
        nx, ny, nz, px, py, pz = params[0], params[1], params[2], params[3], params[4], params[5]
        label = params[6]
    else:
        # Morphing to next knot
        morph_frame = frame_in_cycle - HOLD_FRAMES
        morph_t = morph_frame / MORPH_FRAMES
        morph_t = ease_in_out(morph_t)
        nx, ny, nz, px, py, pz = interpolate_params(
            KNOT_PARAMS[knot_idx], KNOT_PARAMS[next_knot_idx], morph_t)
        label = f"morphing..."

    # Generate curve
    t = np.linspace(0, 2 * np.pi, NUM_POINTS, endpoint=False)
    x = np.cos(nx * t + px)
    y = np.cos(ny * t + py)
    z = np.cos(nz * t + pz)
    points = np.column_stack([x, y, z])

    # Build line segments colored by position along curve
    segments = []
    seg_colors = []
    for i in range(NUM_POINTS):
        j = (i + 1) % NUM_POINTS
        segments.append([points[i], points[j]])
        seg_colors.append(curve_colors[i])

    lc = Line3DCollection(segments, colors=seg_colors, linewidths=2.0, alpha=0.9)
    ax.add_collection3d(lc)

    # Camera orbit
    global_t = frame / TOTAL_FRAMES
    azim = 30 + 720 * global_t  # Two full rotations over the animation
    elev = 20 + 25 * np.sin(2 * np.pi * global_t * 3)
    ax.view_init(elev=elev, azim=azim)

    # Title showing current knot
    if frame_in_cycle < HOLD_FRAMES:
        ax.set_title(f'Lissajous Knot  {label}',
                     color='white', fontsize=18, pad=20)

    if (frame + 1) % FPS == 0:
        sec = (frame + 1) // FPS
        print(f"  {sec}s / {DURATION}s rendered")

# ── Render ────────────────────────────────────────────────────────────────────
print("Rendering animation...")
anim = FuncAnimation(fig, animate, frames=TOTAL_FRAMES, interval=1000 // FPS, blit=False)

writer = FFMpegWriter(fps=FPS, metadata={'title': 'Lissajous Knots'}, bitrate=4000)
output_path = '/output/lissajous.mp4'
anim.save(output_path, writer=writer, savefig_kwargs={'facecolor': 'black'})
print(f"\nSaved to {output_path}")
