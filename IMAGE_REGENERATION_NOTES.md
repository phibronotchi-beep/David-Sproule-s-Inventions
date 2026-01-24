# Image Regeneration Notes

**Date:** January 21, 2026  
**Operation:** Complete image reset and regeneration setup

## Status

All legacy images have been removed and scripts have been updated to regenerate images to `/images/` directory.

**Current State:** Scripts are configured and ready. Images will be generated when scripts are executed with numpy and matplotlib installed.

## Changes Made

### Commit 1: `dfc5cab` - "Remove legacy images (prepare for clean regeneration)"
- Deleted all 11 image files (8 PNG, 3 SVG)
- Removed images from:
  - `/images/` directory
  - `golden-angle-antenna-GAFAA-public/images/`
  - `golden-angle-antenna-GAFAA-public/docs/assets/`
  - `PNM-public/docs/assets/`
  - `PhiKey-public/docs/assets/`

### Commit 2: `feed61b` - "Regenerate images from source scripts and update references"
- Updated all Python scripts to save images to `/images/` directory
- Modified `generate_visualizations.py` to save SVGs to `/images/`
- Updated all markdown files to reference `/images/` instead of `docs/assets/`
- Created `regenerate_all_images.py` - master script to regenerate all images
- Created `generate_plot_images.py` - generates plot images (phyllotaxis-plot.png, spiral-plot.png, geometric-plot.png)
- Removed `plt.show()` calls from all scripts (headless operation)
- Fixed all relative paths to use repository root detection

## Scripts Updated

### Image Generation Scripts (now save to /images/)
1. `PNM-public/src/pnm_public/spiral_utils.py` → `toy_electrode_array.png`
2. `PhiKey-public/src/phikey_public/geometric_utils.py` → `phikey_121_clean.png`
3. `golden-angle-antenna-GAFAA-public/examples/002-phyllux-gafaa-array-factor-polar.py` → `array_factor_polar.png`
4. `golden-angle-antenna-GAFAA-public/examples/004-phyllux-gafaa-spiral-points-demo.py` → `spiral_positions.png`
5. `golden-angle-antenna-GAFAA-public/src/gafaa_public/phyllotaxis_utils.py` → `gafaa_121_clean.png`
6. `golden-angle-antenna-GAFAA-public/examples/005-phyllux-gafaa-realistic-rf-analysis.py` → `gafaa_rf_121_clean.png`
7. `PNM-public/examples/025-phyllux-pnm-realistic-neural-analysis.py` → `pnm_121_clean.png`
8. `PNM-public/examples/027-phyllux-pnm-crosstalk-optimization.py` → `pnm_crosstalk_121_clean.png`
9. `golden-angle-antenna-GAFAA-public/examples/007-phyllux-gafaa-multi-frequency-comparison.py` → `gafaa_multi_freq_121_clean.png`
10. `generate_visualizations.py` → `gafaa-array-layout.svg`, `pnm-electrode-array.svg`, `phikey-lattice.svg`
11. `generate_plot_images.py` → `phyllotaxis-plot.png`, `spiral-plot.png`, `geometric-plot.png`

## Markdown Files Updated

All image references updated to point to `/images/`:
- `README.md` - Main repository README
- `golden-angle-antenna-GAFAA-public/README.md`
- `PNM-public/README.md`
- `PhiKey-public/README.md`

## To Regenerate Images

Run the following scripts (requires numpy and matplotlib):

```bash
# Regenerate all images
python regenerate_all_images.py

# Generate plot images
python generate_plot_images.py

# Generate SVG visualizations
python generate_visualizations.py
```

All images will be saved to `/images/` directory.

## Image List (Expected After Regeneration)

### PNG Images (11)
- `array_factor_polar.png`
- `phikey_121_clean.png`
- `spiral_positions.png`
- `toy_electrode_array.png`
- `gafaa_121_clean.png`
- `gafaa_rf_121_clean.png`
- `gafaa_multi_freq_121_clean.png`
- `pnm_121_clean.png`
- `pnm_crosstalk_121_clean.png`
- `phyllotaxis-plot.png`
- `spiral-plot.png`
- `geometric-plot.png`

### SVG Images (3)
- `gafaa-array-layout.svg`
- `pnm-electrode-array.svg`
- `phikey-lattice.svg`

## Notes

- All scripts now use headless matplotlib (`Agg` backend where needed)
- All `plt.show()` calls removed
- All images save with `facecolor='white'` for clean backgrounds
- All paths use repository root detection for portability
- All markdown references updated to `/images/` directory
