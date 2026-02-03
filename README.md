# Zoom Behavior Insight

Detecting study-focus signals from Zoom-like webcam frames using a **multi-task Computer Vision** model.  
From a single frame, the model predicts an interpretable **behavior vector** across five tasks:

- **Gaze** (camera / not_camera / eyes_closed)
- **Headphones** (with_headphones / without_headphones / unknown)
- **Environment** (indoor / outdoor)
- **Privacy** (private / public)
- **Object in hand** (none / cup / phone / pen / other / unknown)

---

## Project summary

Remote learning makes it hard to infer a student’s context from a single screenshot.  
Instead of relying on a single signal (e.g., only gaze), this project predicts a **set of behavioral + environmental attributes** from one image and returns them as a compact output vector.

### Key idea
A **single backbone** (DeiT) with **multiple classification heads** (one per task) enables multi-task inference with interpretable outputs.

---

## Repository structure

This repository is organized into clear, review-friendly folders:

- `scripts/` — standalone Python scripts (demo inference + utilities)
- `assets/` — small demo assets needed to run the demo
- `weights/` — instructions for model weights (weights are not stored in the repo)
- `notebooks/` — experiments, training/evaluation notebooks
- `results/` — evaluation outputs (plots, tables, metrics)
- `docs/` — additional documentation (labeling guidelines, notes)
- `data/` — small labeled samples / dataset structure documentation
- `presentations/` — project presentations and supporting materials
- `visuals/` — figures used in documentation/presentation

> Each folder contains its own `README.md` with details.

---

## Quick Demo (Recommended)

The easiest way to run the model is via the **Demo ZIP Release**, which includes:
- `scripts/` (demo inference code)
- `assets/demo_images/` (2 demo images)
- `weights/val_best.pth` (required checkpoint)

### Option A: Run via Demo ZIP (no repo clone)

1. Open **Releases** in this repository.
2. Download: `ZoomBehaviorInsight_Demo.zip`
3. Extract it.

You must run from the **extracted folder root** (the folder that contains `scripts/`, `assets/`, `weights/`).

Install dependencies:

```bash
pip install torch torchvision timm pillow pandas
```

Run inference:

```bash
python scripts/inference.py
```

### Expected output

The script prints predictions for each demo image:
- `assets/demo_images/web_019.jpg`
- `assets/demo_images/synth_00097.jpg`

For each image it prints predictions for:
- gaze
- headphones
- environment
- privacy
- object

### Common issue: FileNotFoundError

If you see errors like `Image not found` / `FileNotFoundError`, it usually means:
- you did **not** run from the extracted root folder.

✅ Correct: run from the folder that contains `scripts/`, `assets/`, `weights/`  
❌ Wrong: run from inside `scripts/` or any subfolder

---

## Run from repository (alternative)

If you prefer cloning the repository:

1. Clone the repo.
2. Make sure the demo images exist:
   - `assets/demo_images/web_019.jpg`
   - `assets/demo_images/synth_00097.jpg`
3. Add model weights:
   - place `val_best.pth` at: `weights/val_best.pth`
4. Install dependencies (same as above), then run the script from the repository root.

> See `scripts/README.md`, `assets/README.md`, `assets/demo_images/README.md`, and `weights/README.md` for folder-level instructions.

---

## Model and labels

### Backbone
The final model uses a **DeiT (Data-efficient Image Transformer)** backbone in a **multi-task** setup (one classification head per task).

### Tasks and classes

- **Gaze**: `camera`, `not_camera`, `eyes_closed`
- **Headphones**: `with_headphones`, `without_headphones`, `unknown`
- **Environment**: `indoor`, `outdoor`
- **Privacy**: `private`, `public`
- **Object**: `none`, `cup`, `phone`, `pen`, `other`, `unknown`

Label mappings and constants are defined in:
- `scripts/label_utils.py`

---

## Data and generation (high level)

This project combines:
- **Real images** (Zoom-like frames)
- **Synthetic images** generated to cover rare conditions and improve balance across classes

All images are labeled with the five-task behavior vector described above.

---

## Results and visuals

- Quantitative evaluation results and experiment outputs are stored under `results/`.
- Figures and diagrams used for documentation/presentation are stored under `visuals/`.

---

## Presentations

Slides for the project (proposal, interim, final) are available under `presentations/` in both PPT and PDF formats.

---

## What’s included vs. not included

### Included in this repository
- Code (scripts + notebooks)
- Documentation and slides
- Demo assets (small set)
- Results and visual figures

### Not included in this repository
- Full training/evaluation dataset (hosted externally)
- Additional training checkpoints (not required to run inference)

---

## Notes for reviewers (TA / Lecturer)

- The **Demo ZIP Release** is the recommended way to reproduce inference quickly.
- The full training pipeline and experiments are documented in the notebooks and results folders.

---
