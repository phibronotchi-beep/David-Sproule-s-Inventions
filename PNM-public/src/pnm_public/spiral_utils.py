import numpy as np

def toy_electrode_array(n_electrodes: int, spacing_scale: float = 1.0, angle_deg: float = 137.0):
    """
    Generic phyllotactic electrode placement demo.
    
    Educational toy – NOT real PNM geometry.
    """
    indices = np.arange(n_electrodes)
    r = spacing_scale * np.sqrt(indices)
    theta = np.deg2rad(indices * angle_deg)
    
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return np.column_stack([x, y])
