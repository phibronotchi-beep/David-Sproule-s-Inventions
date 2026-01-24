"""
Simulation-based; empirical validation required per provisional application prepared for filing Jan 21, 2026.

SVG visualization utilities for PNM electrode arrays.
"""

import numpy as np
from typing import Tuple, Optional


def generate_electrode_array_svg(positions: Tuple[np.ndarray, np.ndarray],
                                filename: str,
                                electrode_diameter_um: float = 50.0,
                                width: int = 800,
                                height: int = 800,
                                colors: Optional[list] = None,
                                show_coverage: bool = False,
                                coverage_radius_um: Optional[float] = None) -> str:
    """
    Generate SVG visualization of electrode array layout.
    
    Args:
        positions: (x, y) tuple of electrode positions in micrometers
        filename: Output filename
        electrode_diameter_um: Electrode diameter in micrometers
        width: SVG width in pixels
        height: SVG height in pixels
        colors: Optional list of colors for each electrode
        show_coverage: Whether to show coverage circle
        coverage_radius_um: Coverage radius in micrometers
    
    Returns:
        SVG content as string
    """
    x, y = positions
    n_electrodes = len(x)
    
    # Normalize positions to fit in SVG
    x_norm = x - np.min(x)
    y_norm = y - np.min(y)
    max_dim = max(np.max(x_norm), np.max(y_norm))
    
    # Scale to fit with margin
    margin = 50
    scale = min((width - 2*margin) / max_dim, (height - 2*margin) / max_dim)
    
    x_svg = x_norm * scale + margin
    y_svg = y_norm * scale + margin
    radius_svg = (electrode_diameter_um / 2.0) * scale
    
    # Default colors
    if colors is None:
        colors = ['#0066CC'] * n_electrodes
    
    # Coverage circle
    center_x = np.mean(x_svg)
    center_y = np.mean(y_svg)
    coverage_radius_svg = coverage_radius_um * scale if coverage_radius_um else None
    
    # Generate SVG
    svg_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .electrode {{ stroke: #000000; stroke-width: 1; }}
      .spiral {{ stroke: #0066CC; stroke-width: 0.5; fill: none; opacity: 0.3; }}
      .coverage {{ stroke: #FF0000; stroke-width: 2; fill: none; stroke-dasharray: 5,5; opacity: 0.7; }}
    </style>
  </defs>
  
  <!-- Background -->
  <rect width="{width}" height="{height}" fill="#FFFFFF"/>
  
'''
    
    # Coverage circle
    if show_coverage and coverage_radius_svg:
        svg_content += f'  <circle class="coverage" cx="{center_x:.2f}" cy="{center_y:.2f}" r="{coverage_radius_svg:.2f}"/>\n'
    
    # Spiral path
    svg_content += f'  <path class="spiral" d="M {x_svg[0]:.2f},{y_svg[0]:.2f} {" ".join([f"L {x_svg[i]:.2f},{y_svg[i]:.2f}" for i in range(1, n_electrodes)])}"/>\n'
    
    # Electrodes
    svg_content += '\n  <!-- Electrodes -->\n'
    for i in range(n_electrodes):
        svg_content += f'  <circle class="electrode" cx="{x_svg[i]:.2f}" cy="{y_svg[i]:.2f}" r="{radius_svg:.2f}" fill="{colors[i]}"/>\n'
    
    svg_content += f'''
  <!-- Title -->
  <text x="{width/2}" y="30" text-anchor="middle" font-family="Arial" font-size="20" font-weight="bold">
    PNM Phyllotactic Electrode Array ({n_electrodes} electrodes)
  </text>
</svg>
'''
    
    # Save to file
    with open(filename, 'w') as f:
        f.write(svg_content)
    
    return svg_content
