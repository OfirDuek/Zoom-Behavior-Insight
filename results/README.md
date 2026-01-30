# Results

This folder contains exported experiment results in machine-readable formats (CSV/JSON), as required for reproducibility and review.

## Structure

- `baseline_resnet18/` — baseline model results (ResNet18 multi-head)
- `final_deit/` — final model results (DeiT multi-task / multi-head)

Each subfolder includes:
- `*_per_task_metrics.csv` — per-task metrics (one row per attribute)
- `*_overall_metrics.csv` — overall metrics (aggregated across tasks)
- `*_metrics.json` — combined metrics summary (per-task + overall) in JSON format

## Metrics

### Per-task metrics (`*_per_task_metrics.csv`)
Reported for each attribute:
- `accuracy` — fraction of correct predictions for that task
- (If present) `macro_f1` — macro-averaged F1 score for that task

### Overall metrics (`*_overall_metrics.csv`)
Reported across all tasks:
- `avg_accuracy` — mean of per-task accuracies
- `joint_accuracy` (a.k.a exact match) — a sample is counted correct only if **all tasks** are predicted correctly

## Notes

- Baseline numeric results were reconstructed to match the plotted results when raw logs were not available.  
- All plots used in the report/presentation are stored under `visuals/results/`.

## Related

- Figures: `visuals/results/`
- Notebooks: `notebooks/`
