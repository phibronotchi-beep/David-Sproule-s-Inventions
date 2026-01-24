# To use: Run this script to generate the image. Output saves to 'images/' relative to this file. Install requirements: pip install numpy matplotlib.
"""
Simulation-based; empirical validation required per provisional application prepared for filing Jan 21, 2026.
"""
import os
import numpy as np
import matplotlib.pyplot as plt

# Section 1: From golden-angle-antenna-GAFAA-public/array_factor_polar.py
# Set the output directory relative to this file
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.join(SCRIPT_DIR, '..', '..', '..')
IMAGE_DIR = os.path.join(REPO_ROOT, 'images')
os.makedirs(IMAGE_DIR, exist_ok=True)

print(f"Image output directory: {IMAGE_DIR}")

print("Running array_factor_polar section...")
try:
    f = 28e9  # Frequency (28 GHz)
    c = 3e8  # Speed of light
    lambda_ = c / f  # Wavelength
    N = 121  # Number of elements

    # Generate spiral positions
    theta_spiral = np.arange(N) * np.deg2rad(137.508)
    r = np.sqrt(np.arange(N))
    x = r * np.cos(theta_spiral)
    y = r * np.sin(theta_spiral)
    element_positions = np.column_stack((x, y))

    # Grid for polar plot
    theta, phi = np.mgrid[0:np.pi:100j, 0:2*np.pi:100j]

    # Calculate AF
    k = 2 * np.pi / lambda_  # Wave number
    phase = k * (element_positions[:, 0, np.newaxis, np.newaxis] * np.sin(theta) * np.cos(phi) +
                 element_positions[:, 1, np.newaxis, np.newaxis] * np.sin(theta) * np.sin(phi))
    AF = np.sum(np.exp(1j * phase), axis=0) / N
    AF_dB = 20 * np.log10(np.abs(AF) + 1e-10)  # in dB

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='polar')
    contour = ax.contourf(phi, theta * (180/np.pi), AF_dB, levels=30, cmap='viridis')
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)
    ax.set_title("Array Factor Polar Plot (dB)")
    fig.colorbar(contour)
    plt.savefig(os.path.join(IMAGE_DIR, 'array_factor_polar.png'), dpi=300, bbox_inches='tight')
    plt.close(fig)
    print("Generated: array_factor_polar.png")
except Exception as e:
    print(f"Error in array_factor_polar: {e}")
