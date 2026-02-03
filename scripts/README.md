# Scripts

Standalone Python scripts used in this project (outside the notebooks).  
Includes a **demo inference** script, shared label utilities, and a video-to-frames helper.

---

## Folder contents

- **`inference.py`**  
  Runs the trained **multi-task DeiT** model on demo images and prints predictions for:  
  `gaze`, `headphones`, `environment`, `privacy`, `object`.

- **`label_utils.py`**  
  Shared label mappings and constants used across scripts.

- **`extract_frames.py`**  
  Extracts frames from `.avi` videos (used to generate real-image frames from recorded videos).

---

## Demo inference (recommended)

### Expected paths (repository root)

- Demo images:
  - `assets/demo_images/web_019.jpg`
  - `assets/demo_images/synth_00097.jpg`

- Model weights:
  - `weights/val_best.pth`

> **Tip:** If you use the **Demo ZIP Release**, these files are already included in the correct paths.

---

## How to run

### 1) Install dependencies

> Python 3.9+ recommended.

```bash
pip install torch torchvision timm pillow pandas
```

### 2) Run inference

From the **repository root**:

```bash
python scripts/inference.py
```

### Output

The script prints a prediction per task for each demo image:

- `gaze`: `camera` / `not_camera` / `eyes_closed`
- `headphones`: `with_headphones` / `without_headphones` / `unknown`
- `environment`: `indoor` / `outdoor`
- `privacy`: `private` / `public`
- `object`: `none` / `cup` / `phone` / `pen` / `other` / `unknown`

---

## Extract frames from videos (optional utility)

### Install (only if you use this script)

```bash
pip install opencv-python
```

### Run

```bash
python scripts/extract_frames.py \
  --video_folder path/to/videos \
  --output_folder path/to/output_frames \
  --frames_per_video 10
```

### Arguments

- `--video_folder` — folder containing `.avi` videos (searched recursively)
- `--output_folder` — output folder for extracted frames
- `--frames_per_video` — number of frames to save per video (default: 10)

---

## Notes

- These scripts are meant to be **minimal, reproducible, and easy to review**.
- Full training pipeline and experiments are documented in the notebooks and results folders.
