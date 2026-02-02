# Scripts

This folder contains standalone Python scripts used in the project (outside the notebooks).

## Contents
- `inference.py` — Runs the trained multi-task DeiT model on demo images and prints predictions for: `gaze`, `headphones`, `environment`, `privacy`, `object`.
- `label_utils.py` — Shared label mappings and constants used by the scripts.
- `extract_frames.py` — Extracts frames from `.avi` videos (used to create real-image frames from recorded videos).

## How to run

### 1) Install requirements
```bash
pip install torch torchvision timm pillow pandas

### 2) Prepare model weights
Download the model checkpoint `val_best.pth` from the weights link in the main repository README, then place it here: `weights/val_best.pth`

### 3) Prepare demo images
Make sure these demo images exist in the repository:
- Real: `assets/demo_images/web_019.jpg`
- Synthetic: `assets/demo_images/synth_00097.jpg`

### 4) Run inference
From the repository root:
```bash
python scripts/inference.py
