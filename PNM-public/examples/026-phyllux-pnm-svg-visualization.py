"""
Simulation-based; empirical validation required per provisional application prepared for filing (to be filed late January 2026).

Generate SVG visualizations of PNM electrode arrays.
"""

import numpy as np
from src.pnm_public.neural_utils import phyllotactic_electrode_positions, coverage_area
from src.pnm_public.svg_utils import generate_electrode_array_svg

def main():
    # Parameters
    n_electrodes = 121
    electrode_diameter_um = 50.0
    min_spacing_um = 200.0
    
    # Generate positions
    x, y = phyllotactic_electrode_positions(n_electrodes, electrode_diameter_um, min_spacing_um)
    
    # Calculate coverage
    coverage = coverage_area((x, y), electrode_diameter_um)
    
    # Generate color gradient based on radial distance
    r = np.sqrt(x**2 + y**2)
    r_norm = (r - np.min(r)) / (np.max(r) - np.min(r))
    
    # Color map: light blue to dark blue based on radius
    colors = []
    for r_val in r_norm:
        # Interpolate from light blue (#ADD8E6) to dark blue (#00008B)
        red = int(0xAD + (0x00 - 0xAD) * r_val)
        green = int(0xD8 + (0x00 - 0xD8) * r_val)
        blue = int(0xE6 + (0x8B - 0xE6) * r_val)
        colors.append(f"#{red:02X}{green:02X}{blue:02X}")
    
    # Generate SVG with coverage
    svg_content = generate_electrode_array_svg(
        (x, y),
        'pnm_electrode_array_layout.svg',
        electrode_diameter_um=electrode_diameter_um,
        width=1000,
        height=1000,
        colors=colors,
        show_coverage=True,
        coverage_radius_um=coverage['coverage_radius_um']
    )
    
    print("SVG visualization generated: pnm_electrode_array_layout.svg")
    print(f"Array has {n_electrodes} electrodes")
    print(f"Coverage radius: {coverage['coverage_radius_um']:.1f} μm")
    print(f"Coverage area: {coverage['coverage_area_um2']/1e6:.2f} mm²")

if __name__ == "__main__":
    main()
