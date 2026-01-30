# Results

This folder contains the exported evaluation outputs of our experiments, saved in **machine-readable formats**
so the project can be reviewed and reproduced without rerunning the full notebooks.

We report results for:
- **Baseline model:** ResNet18 multi-head classifier
- **Final model:** DeiT multi-head classifier

The main task is multi-attribute prediction from a single Zoom-like frame, producing a behavior vector:
**gaze**, **headphones**, **environment**, **privacy**, **object in hand**.

---

## What’s inside?

Each experiment (baseline / final) includes **three files**:

### 1) Per-task metrics (CSV)
**File:** `*_per_task_metrics.csv`  
Contains metrics **per attribute** (one row per task), e.g. accuracy and macro-F1.

**Use case:** quick comparison between tasks (which attribute is easier/harder).

### 2) Overall metrics (CSV)
**File:** `*_overall_metrics.csv`  
Contains overall summary numbers such as:
- **avg_accuracy** – mean accuracy across tasks
- **joint_accuracy** – “exact match”: a sample is correct only if **all tasks** are correct

**Use case:** single-number summary and model-to-model comparison.

### 3) Full metrics (JSON)
**File:** `*_metrics.json`  
A complete export of the experiment metrics in a structured format.
This may include the same values as the CSVs (and optionally additional fields if available).

**Use case:** programmatic parsing / future analysis / plotting.

---

## Baseline: ResNet18

- Per-task metrics (CSV): [`baseline_resnet18_per_task_metrics.csv`](baseline_resnet18/baseline_resnet18_per_task_metrics.csv)
- Overall metrics (CSV): [`baseline_resnet18_overall_metrics.csv`](baseline_resnet18/baseline_resnet18_overall_metrics.csv)
- Full metrics (JSON): [`baseline_resnet18_metrics.json`](baseline_resnet18/baseline_resnet18_metrics.json)

---

## Final model: DeiT

- Per-task metrics (CSV): [`final_deit_per_task_metrics.csv`](final_deit/final_deit_per_task_metrics.csv)
- Overall metrics (CSV): [`final_deit_overall_metrics.csv`](final_deit/final_deit_overall_metrics.csv)
- Full metrics (JSON): [`final_deit_metrics.json`](final_deit/final_deit_metrics.json)

---

## Notes

- These files are meant to match the figures under `visuals/` and support the reported results.
- The repository includes a **small sample** of the dataset under `data/` for review and reproducibility;
  the full dataset is stored separately.
- Naming is kept consistent across models to keep comparisons clear and to support automated parsing.
