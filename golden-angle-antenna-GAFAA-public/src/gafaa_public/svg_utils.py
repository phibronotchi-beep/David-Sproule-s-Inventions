"""
Simulation-based; empirical validation required per provisional application prepared for filing (to be filed late January 2026).

SVG visualization utilities for GAFAA antenna arrays.
"""

import numpy as np
from typing import Tuple, Optional


def generate_array_svg(positions: Tuple[np.ndarray, np.ndarray],
                      filename: str,
                      element_size: float = 2.0,
                      width: int = 800,
                      height: int = 800,
                      colors: Optional[list] = None) -> str:
    """
    Generate SVG visualization of antenna array layout.
    
    Args:
        positions: (x, y) tuple of element positions in meters
        filename: Output filename
        element_size: Size of element circles in SVG units
        width: SVG width in pixels
        height: SVG height in pixels
        colors: Optional list of colors for each element
    
    Returns:
        SVG content as string
    """
    x, y = positions
    n_elements = len(x)
    
    # Normalize positions to fit in SVG
    x_norm = x - np.min(x)
    y_norm = y - np.min(y)
    max_dim = max(np.max(x_norm), np.max(y_norm))
    
    # Scale to fit with margin
    margin = 50
    scale = min((width - 2*margin) / max_dim, (height - 2*margin) / max_dim)
    
    x_svg = x_norm * scale + margin
    y_svg = y_norm * scale + margin
    
    # Default colors
    if colors is None:
        colors = ['#FF0000'] * n_elements
    
    # Generate SVG
    svg_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .element {{ stroke: #000000; stroke-width: 1; }}
      .spiral {{ stroke: #0066CC; stroke-width: 0.5; fill: none; opacity: 0.3; }}
    </style>
  </defs>
  
  <!-- Background -->
  <rect width="{width}" height="{height}" fill="#FFFFFF"/>
  
  <!-- Spiral path -->
  <path class="spiral" d="M {x_svg[0]:.2f},{y_svg[0]:.2f} {' '.join([f'L {x_svg[i]:.2f},{y_svg[i]:.2f}' for i in range(1, n_elements)])}"/>
  
  <!-- Antenna elements -->
'''
    
    for i in range(n_elements):
        svg_content += f'  <circle class="element" cx="{x_svg[i]:.2f}" cy="{y_svg[i]:.2f}" r="{element_size}" fill="{colors[i]}"/>\n'
    
    svg_content += f'''
  <!-- Title -->
  <text x="{width/2}" y="30" text-anchor="middle" font-family="Arial" font-size="20" font-weight="bold">
    GAFAA Phyllotactic Antenna Array ({n_elements} elements)
  </text>
</svg>
'''
    
    # Save to file
    with open(filename, 'w') as f:
        f.write(svg_content)
    
    return svg_content
