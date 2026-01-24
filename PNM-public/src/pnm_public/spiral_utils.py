# To use: Run this script to generate the image. Output saves to 'images/' relative to this file. Install requirements: pip install numpy matplotlib.
"""
Simulation-based; empirical validation required per provisional application prepared for filing Jan 21, 2026.
"""
import os
import numpy as np
import matplotlib.pyplot as plt

# Section 3: From PNM-public/toy_electrode_array.py
# Set the output directory relative to this file
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.join(SCRIPT_DIR, '..', '..', '..', '..')
IMAGE_DIR = os.path.join(REPO_ROOT, 'images')
os.makedirs(IMAGE_DIR, exist_ok=True)

print(f"Image output directory: {IMAGE_DIR}")

print("Running toy_electrode_array section...")
try:
    N = 121
    golden_angle = 137.508
    theta = np.arange(N) * np.deg2rad(golden_angle)
    r = np.sqrt(theta)

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='polar')
    ax.scatter(theta, r, s=10, c='blue')
    ax.set_rlim(0, r.max() * 1.05)
    ax.plot([0, 2*np.pi], [r.max(), r.max()], color='red', linewidth=1)
    ax.set_title("PNM Phyllotactic Electrode Array (121 electrodes)")
    fig.suptitle("Golden Angle ~137.508° Pattern for Neural Interfaces")
    plt.savefig(os.path.join(IMAGE_DIR, 'toy_electrode_array.png'), dpi=300, bbox_inches='tight')
    plt.close(fig)
    print("Generated: toy_electrode_array.png")
except Exception as e:
    print(f"Error in toy_electrode_array: {e}")
