import numpy as np

def pnm_positions(N=121, R=2.5):
    phi = (1 + np.sqrt(5))/2
    theta = np.arange(N) * (360 / phi) % 360
    r = R * np.sqrt(np.arange(N) / N)
    x = r * np.cos(np.deg2rad(theta))
    y = r * np.sin(np.deg2rad(theta))
    return np.column_stack((x, y))

def crosstalk(D, sigma=0.14):
    return np.exp(-D**2 / (2 * sigma**2))

pos = pnm_positions()
D = np.linalg.norm(pos[:, None] - pos[None, :], axis=2)
C = crosstalk(D)
print("Matrix shape:", C.shape)
