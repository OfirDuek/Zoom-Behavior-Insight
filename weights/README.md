# Weights

This project uses a trained multi-task DeiT model checkpoint.

**Note:** Model weights are not stored in this GitHub repository due to file size.
They are hosted externally and can be downloaded from the link below.

---

## Download

Download the checkpoint from Google Drive:

- **ZoomBehaviorInsight_Weights**: <DRIVE_LINK_HERE>

The required file is:

- `val_best.pth`

---

## Where to place the file

After downloading, create the folder (if missing) and place the file here:

```bash
mkdir -p weights
```

Expected path (from repository root):

- `weights/val_best.pth`

---

## Verify (demo inference)

Once the weights are in place, run the demo inference script from the repository root:

```bash
python scripts/inference.py
```

If everything is set up correctly, the script will print predictions for the demo images in:
- `assets/demo_images/web_019.jpg`
- `assets/demo_images/synth_00097.jpg`

---

## Access note

Make sure the Google Drive link is **public** (anyone with the link can download) and does **not** require a login.
