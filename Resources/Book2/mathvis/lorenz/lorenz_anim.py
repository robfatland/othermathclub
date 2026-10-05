"""
Animated Lorenz attractor: The trajectory grows over time while the
camera rotates ~720 degrees. Color varies as the cosine of the trajectory
vector relative to the z-axis, mapped through the magma colormap.
Output is an MP4 file.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation, FFMpegWriter
import matplotlib.cm as cm

# ── Lorenz integration ────────────────────────────────────────────────────────
def lorenz(xyz, s=10, r=28, b=8/3):
    x, y, z = xyz
    return np.array([s*(y - x), x*(r - z) - y, x*y - b*z])

dt = 0.005
steps = 10000
trajectory = np.empty((steps, 3))
trajectory[0] = [1, 1, 1]
for i in range(1, steps):
    trajectory[i] = trajectory[i-1] + lorenz(trajectory[i-1]) * dt

# ── Precompute colors based on angle to z-axis ───────────────────────────────
# cos(theta) = z / |r| for each point
norms = np.linalg.norm(trajectory, axis=1)
norms[norms == 0] = 1  # avoid division by zero
cos_theta = trajectory[:, 2] / norms

# Normalize to [0, 1] for colormap lookup
cos_normalized = (cos_theta - cos_theta.min()) / (cos_theta.max() - cos_theta.min())
colormap = cm.magma
colors = colormap(cos_normalized)

# ── Animation config ─────────────────────────────────────────────────────────
TOTAL_ROTATION = 720
ROTATION_PER_FRAME = 60
SEGMENT_DURATION = 6
FPS = 30

n_segments = int(np.ceil(TOTAL_ROTATION / ROTATION_PER_FRAME))
total_frames = n_segments * SEGMENT_DURATION * FPS
points_per_frame = max(1, steps // total_frames)

print(f"Segments: {n_segments}, Total frames: {total_frames}")
print(f"Trajectory points per frame: {points_per_frame}")
print(f"Total duration: {total_frames / FPS:.1f} seconds")

# ── Set up figure ─────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(12, 9), facecolor='black')
ax = fig.add_subplot(111, projection='3d', facecolor='black')

for axis in [ax.xaxis, ax.yaxis, ax.zaxis]:
    axis.pane.fill = False
    axis.pane.set_edgecolor('gray')
    axis.label.set_color('white')
    axis._axinfo['tick']['color'] = 'white'
ax.tick_params(colors='white')
ax.set_xlabel('X', color='white')
ax.set_ylabel('Y', color='white')
ax.set_zlabel('Z', color='white')

pad = 5
ax.set_xlim(trajectory[:, 0].min() - pad, trajectory[:, 0].max() + pad)
ax.set_ylim(trajectory[:, 1].min() - pad, trajectory[:, 1].max() + pad)
ax.set_zlim(trajectory[:, 2].min() - pad, trajectory[:, 2].max() + pad)

title = ax.set_title('Lorenz Attractor', color='white', fontsize=16)

# Use a scatter plot so each point can have its own color
scatter = ax.scatter([], [], [], s=0.3, c=[], cmap='magma', alpha=0.9)

# ── Animation function ───────────────────────────────────────────────────────
start_azim = 0

def animate(frame):
    n_points = min((frame + 1) * points_per_frame, steps)

    scatter._offsets3d = (trajectory[:n_points, 0],
                          trajectory[:n_points, 1],
                          trajectory[:n_points, 2])
    scatter.set_array(cos_normalized[:n_points])
    scatter.set_clim(0, 1)

    azim = start_azim + (TOTAL_ROTATION * frame / total_frames)
    elev = 25 + 10 * np.sin(2 * np.pi * frame / total_frames)
    ax.view_init(elev=elev, azim=azim)

    if (frame + 1) % FPS == 0:
        sec = (frame + 1) // FPS
        print(f"  {sec}s / {total_frames // FPS}s rendered")

    return scatter,

# ── Render ────────────────────────────────────────────────────────────────────
print("Rendering animation...")
anim = FuncAnimation(fig, animate, frames=total_frames, interval=1000//FPS, blit=False)

writer = FFMpegWriter(fps=FPS, metadata={'title': 'Lorenz Attractor'}, bitrate=2000)
output_path = '/output/lorenz.mp4'
anim.save(output_path, writer=writer, savefig_kwargs={'facecolor': 'black'})
print(f"\nSaved to {output_path}")
