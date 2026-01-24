"""
Simulation-based; empirical validation required per provisional application prepared for filing (to be filed late January 2026).
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
from src.pnm_public.spiral_utils import toy_electrode_array

def toy_crosstalk_matrix(n_electrodes=64):
    """
    Simplified crosstalk visualization.
    Toy model only – educational.
    """
    positions = toy_electrode_array(n_electrodes)
    
    # Toy crosstalk: decays exponentially with distance
    distances = cdist(positions, positions)
    crosstalk = np.exp(-distances / 0.03)  # Arbitrary decay
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Array plot
    ax1.scatter(positions[:, 0], positions[:, 1], s=40, c='blue', edgecolors='black')
    ax1.set_title("Toy Electrode Layout")
    ax1.axis("equal")
    ax1.grid(True, alpha=0.3)
    
    # Crosstalk matrix
    im = ax2.imshow(crosstalk, cmap='hot', origin='lower')
    ax2.set_title("Toy Crosstalk Matrix")
    ax2.set_xlabel("Electrode Index")
    ax2.set_ylabel("Electrode Index")
    plt.colorbar(im, ax=ax2)
    
    plt.tight_layout()
    plt.show()
    
    print(f"Max off-diagonal crosstalk: {np.max(crosstalk[np.triu_indices(n_electrodes, k=1)]):.3f}")

if __name__ == "__main__":
    toy_crosstalk_matrix()
