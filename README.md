# Statistical Methods to Define Standards and Limitations of Cell Segmentation in Image-Based Spatial Transcriptomics

## Introduction

The goal of this project is to highlight the importance of selecting an optimal cell segmentation model for image-based spatial transcriptomics (ST) data. As ST technologies enable gene expression profiling at near single-cell resolution, accurate cell segmentation in spatial images is essential for correctly assigning transcripts to individual cells. However, the performance of different cell segmentation methods on multi-resolution dataset is often overstated and needs to be re-evaluated systematically.

**There are two aims for the project:**

(1) Aim 1 is to evaluate cell segmentation methods and annotations not only based on morphological accuracy, but also on biological relevance, using low-dimensional embeddings.

(2) Aim 2 investigates how segmentation quality is influenced by variations in transcript abundance, a common challenge in real-world spatial transcriptomics datasets.

## Project Structure
```graphql
├── code
│   ├── aim1_cell_annotation
│   └── aim2_cell_segmentation 
├── data
│   ├── pbmc_dataset
│   ├── xenium_mouse_brain
│   └── xenium_tiny_subset_brain
├── LICENSE
├── pyproject.toml
├── README.md
├── renv
│   ├── activate.R
│   └── settings.json
├── renv.lock
├── src
│   └── STimage_benchmarks
├── STimage_benchmarks.Rproj
├── structure.txt
└── uv.lock

10 directories, 10 files
```

## Repository Usage

### Installation

Clone this project
```bash
git clone https://github.com/guillemchillon/STimage_benchmarks.git
```

This codebase uses `uv`, which can be installed on POSIX systems with,

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

(See [uv](https://astral.sh/uv/) for more details.)

Install dependencies with,

```bash
uv sync
uv pip install -e .
```

#### Updating R Dependencies with `renv`

R dependencies are managed by `renv`, you can restore and update them as follows:

1. Restore the R environment from the `renv.lock` file:

   ```R
   renv::restore()
   ```

3. If edited, ensure the `renv.lock` file is updated to reflect the changes:

   ```R
   renv::snapshot()
   ```

For more details, refer to the [renv documentation](https://rstudio.github.io/renv/).


## Roadmap

### Aim 1: Biologically suitable benchmarking for segmentation models

- [x] Develop statistical methods using UMAP clustering distances to quantify biological distinctiveness of segmented cells.
- [ ] Benchmark current segmentation models on image-based ST datasets using the developed metrics.

### Aim 2: Sensitivity of segmentation models to transcript abundance

- [x] Simulate reduced transcriptomic resolution via controlled transcript downsampling.
- [x] Evaluate segmentation performance across transcript density levels.
- [ ] Identify resolution thresholds for reliable and biologically meaningful segmentation.
