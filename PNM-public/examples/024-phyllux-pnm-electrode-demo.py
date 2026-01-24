"""
Simulation-based; empirical validation required per PPA filed Jan 21, 2026.
PPA: "Phyllotactic Multi-Domain System for Neural Interfaces, Wireless Communications, and Cryptographic Security"
"""
import matplotlib.pyplot as plt
from src.pnm_public.spiral_utils import toy_electrode_array

def main():
    electrodes = toy_electrode_array(n_electrodes=121, spacing_scale=0.05)
    
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.scatter(electrodes[:, 0], electrodes[:, 1], s=50, c='blue', edgecolors='black')
    ax.set_aspect("equal")
    ax.set_title("Toy Phyllotactic Electrode Array Demo")
    ax.axis("off")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
