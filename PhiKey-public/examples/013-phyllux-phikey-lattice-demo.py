"""
Simulation-based; empirical validation required per provisional application prepared for filing Jan 21, 2026.
"""
import matplotlib.pyplot as plt
from src.phikey_public.geometric_utils import toy_lattice_growth

def main():
    nodes = toy_lattice_growth(n_nodes=121)
    
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.scatter(nodes[:, 0], nodes[:, 1], s=20)
    ax.set_aspect("equal")
    ax.set_title("Toy Geometric Lattice Growth Demo")
    ax.axis("off")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
