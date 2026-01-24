"""
Simulation-based; empirical validation required per provisional application prepared for filing Jan 21, 2026.

Generate SVG visualizations of GAFAA antenna arrays.
"""

import numpy as np
from src.gafaa_public.rf_utils import phyllotactic_positions
from src.gafaa_public.svg_utils import generate_array_svg

def main():
    # Parameters for 5G mmWave array
    frequency_hz = 28e9  # 28 GHz
    wavelength = 299792458.0 / frequency_hz
    n_elements = 121
    spacing_factor = 0.5
    
    # Generate positions
    x, y = phyllotactic_positions(n_elements, wavelength, spacing_factor)
    
    # Generate color gradient based on radial distance
    r = np.sqrt(x**2 + y**2)
    r_norm = (r - np.min(r)) / (np.max(r) - np.min(r))
    
    # Color map: blue to red based on radius
    colors = []
    for r_val in r_norm:
        # Interpolate from blue (#0066CC) to red (#FF0000)
        blue = int(0x00 + (0xFF - 0x00) * r_val)
        green = int(0x66 + (0x00 - 0x66) * r_val)
        red = int(0xCC + (0x00 - 0xCC) * r_val)
        colors.append(f"#{red:02X}{green:02X}{blue:02X}")
    
    # Generate SVG
    svg_content = generate_array_svg(
        (x, y),
        'gafaa_array_layout.svg',
        element_size=3.0,
        width=1000,
        height=1000,
        colors=colors
    )
    
    print("SVG visualization generated: gafaa_array_layout.svg")
    print(f"Array has {n_elements} elements")
    print(f"Frequency: {frequency_hz/1e9:.2f} GHz")
    print(f"Wavelength: {wavelength*1000:.2f} mm")

if __name__ == "__main__":
    main()
