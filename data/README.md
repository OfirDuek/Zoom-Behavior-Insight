# Data

This folder contains a small labeled sample of the dataset used in this project.

## Structure

- `real/`
  - Images: [`real/images/`](real/images/)
  - Labels: [`real/labels.csv`](real/labels.csv)
- `synthetic/`
  - Images: [`synthetic/images/`](synthetic/images/)
  - Labels: [`synthetic/labels.csv`](synthetic/labels.csv)

## Labels format

Both `labels.csv` files share the same schema:

- `filename` — image file name (must match a file under the corresponding `images/` folder)
- `Gaze` — `{Camera, Not_Camera, Eyes_Closed}`
- `Headphones` — `{With_Headphones, Without_Headphones, Unknown}`
- `Environment` — `{Indoor, Outdoor}`
- `Privacy` — `{Private, Public}`
- `ObjectInHand` — `{Phone, Cup, Pen, Other, None, Unknown}`

## Notes

- Only a small subset is included in this repository for demonstration and reproducibility.
- The full dataset is stored separately and is not included here.
