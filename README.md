# Zoom Behavior Insight

A project for detecting study-focus signals from Zoom-like webcam frames and producing interpretable outputs:
**gaze**, **headphones**, **background environment/privacy**, and **object in hand**.

## Project goal
Given a webcam-style image, the model outputs a structured multi-task prediction (one label per attribute) to describe engagement-related cues in an interpretable way.

## Repository structure
- `presentations/` – Project presentations (PDF + PPTX)
- `notebooks/` – Notebooks used for the interim submission:
  - `5_1_data_generation.ipynb` – Synthetic data generation (SDXL Turbo + Inpainting/background replacement)
  - `5_2_eda.ipynb` – Dataset EDA (distributions, unknown rates, imbalance checks)
  - `5_3_baseline_evaluation.ipynb` – Baseline model evaluation + metrics export
- `docs/` – Documentation
  - `Labeling_Guidelines.pdf` – Labeling guidelines
- `data/` – Small labeled sample used for repository demonstration
  - `real/` – Real images sample + labels
  - `synthetic/` – Synthetic images sample + labels

## Quick links
- Presentations: `presentations/`
- Notebooks: `notebooks/`
- Labeling guidelines: `docs/Labeling_Guidelines.pdf`
- Data sample: `data/`

## Data note (privacy)
This repository includes only a **small sample** of labeled data for demonstration and reproducibility.
Full real-data releases depend on privacy/consent constraints. Synthetic data has no such limitation.
