"""Demo inference script for Zoom Behavior Insight.

This script loads the trained multi-task DeiT checkpoint and runs predictions on a
small set of demo images. The output is a compact "behavior vector" consisting of
five tasks: gaze, headphones, environment, privacy, and object.

Expected repository structure (from repo root):
  - weights/val_best.pth
  - assets/demo_images/web_019.jpg
  - assets/demo_images/synth_00097.jpg
"""

from pathlib import Path

import torch
import torch.nn as nn
import timm
from torchvision import transforms
from PIL import Image

from label_utils import LABEL_MAPS, NUM_CLASSES

ROOT = Path(__file__).resolve().parents[1]

WEIGHTS_PATH = ROOT / "weights" / "val_best.pth"

REAL_IMAGE_PATH = ROOT / "assets" / "demo_images" / "web_019.jpg"
SYNTH_IMAGE_PATH = ROOT / "assets" / "demo_images" / "synth_00097.jpg"

BACKBONE_NAME = "deit_base_patch16_224"


class MultiHeadDeiT(nn.Module):
    """Multi-task DeiT model: one shared backbone + one linear head per task."""

    def __init__(self, backbone_name, num_classes, pretrained=True):
        super().__init__()
        # Create a DeiT backbone that outputs a feature vector (num_classes=0 removes the classifier).
        self.backbone = timm.create_model(backbone_name, pretrained=pretrained, num_classes=0)
        dim = self.backbone.num_features
        # Each task has its own classification head with the relevant number of classes.
        self.heads = nn.ModuleDict({t: nn.Linear(dim, n) for t, n in num_classes.items()})

    def forward(self, x):
        feat = self.backbone(x)
        return {t: head(feat) for t, head in self.heads.items()}


def invert_label_maps():
    """Build id->label mappings for pretty printing predictions."""
    inv = {}
    for task, m in LABEL_MAPS.items():
        inv_task = {}
        for k, v in m.items():
            if v not in inv_task:
                inv_task[v] = k
        inv[task] = inv_task
    return inv


def predict_one(model, eval_tf, inv, device, img_path):
    """Run a forward pass on a single image and return decoded predictions."""
    img = Image.open(img_path).convert("RGB")
    # Preprocess to match DeiT expected input size and normalization.
    x = eval_tf(img).unsqueeze(0).to(device)

    with torch.no_grad():
        out = model(x)

    preds = {}
    for task in ["gaze", "headphones", "environment", "privacy", "object"]:
        logits = out[task][0]
        pred_idx = int(torch.argmax(logits).item())
        preds[task] = inv[task].get(pred_idx, str(pred_idx))

    return preds


def main():
    # Validate that required resources exist before running inference.
    if not WEIGHTS_PATH.exists():
        raise FileNotFoundError(f"Weights not found: {WEIGHTS_PATH}")

    for p in [REAL_IMAGE_PATH, SYNTH_IMAGE_PATH]:
        if not p.exists():
            raise FileNotFoundError(f"Image not found: {p}")

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    eval_tf = transforms.Compose(
        [
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ]
    )

    # Build the model architecture and load trained weights.
    model = MultiHeadDeiT(BACKBONE_NAME, NUM_CLASSES, pretrained=False).to(device)
    state = torch.load(WEIGHTS_PATH, map_location=device)
    model.load_state_dict(state)
    model.eval()

    inv = invert_label_maps()

    print("REAL (web_019.jpg)")
    real_preds = predict_one(model, eval_tf, inv, device, REAL_IMAGE_PATH)
    for k, v in real_preds.items():
        print(f"{k}: {v}")

    print("\nSYNTHETIC (synth_00097.jpg)")
    synth_preds = predict_one(model, eval_tf, inv, device, SYNTH_IMAGE_PATH)
    for k, v in synth_preds.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()