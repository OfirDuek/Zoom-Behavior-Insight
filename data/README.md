# Data

This folder contains a **small labeled sample** of the dataset used in this project (for quick review and reproducibility on GitHub).

The **full dataset** (all images + labels) is hosted externally due to **size** and **privacy** considerations.

---

## Full dataset (Google Drive)

**Google Drive folder:**  
https://drive.google.com/drive/folders/1kIi7_KhhTJWVCjb3Mw_XnfPoghaPxfcc?usp=drive_link

### Drive structure (expected)

The Drive folder `ZoomBehaviorInsight_Data` contains:

- `train/`
- `validation/`
- `test/`
- `labels.csv` — labels for **all images** across splits

> Folder names are lowercase: `train`, `validation`, `test`.

---

## GitHub sample structure (this folder)

- `real/`
  - Images: [`real/images/`](real/images/)
  - Labels: [`real/labels.csv`](real/labels.csv)
- `synthetic/`
  - Images: [`synthetic/images/`](synthetic/images/)
  - Labels: [`synthetic/labels.csv`](synthetic/labels.csv)

---

## Labels format

All `labels.csv` files follow the same schema:

- `filename` — image file name (must match a file under the corresponding images folder)
- `Gaze` — `{Camera, Not_Camera, Eyes_Closed}`
- `Headphones` — `{With_Headphones, Without_Headphones, Unknown}`
- `Environment` — `{Indoor, Outdoor}`
- `Privacy` — `{Private, Public}`
- `ObjectInHand` — `{Phone, Cup, Pen, Other, None, Unknown}`

---

## Notes

- The GitHub version includes only a **small subset** (real + synthetic) for demonstration.
- The **Drive link above** provides access to the **complete dataset** required for full training/evaluation.
