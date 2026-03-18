# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a single-cell RNA sequencing (scRNA-seq) analysis research project focused on Peripheral Blood Mononuclear Cells (PBMCs). It uses the Python scanpy ecosystem for QC, clustering, and visualization, with some RNA velocity analysis via scvelo.

**Dataset**: PBMCs from a healthy donor sequenced on Illumina NovaSeq 6000 (10x Genomics 3' v3.1), ~5,108 cells.

## Running Scripts

This project has no build system. Run scripts directly:

```bash
python pcmb_example.py       # Main PBMC QC & clustering pipeline
python ode_example.py        # RNA velocity analysis (scvelo, pancreas dataset)
python test2.py              # Simplified QC workflow variant
python ros.py                # Bioinformatics problem sets (Rosalind-style)
jupyter notebook             # Interactive analysis notebook
```

No formal test suite exists.

## Architecture

### Analysis Pipeline (pcmb_example.py, Untitled-1.ipynb)

1. **Load** — `sc.read_10x_mtx()` from `filtered_feature_bc_matrix/`
2. **QC** — Compute per-cell metrics (gene count, UMI, mitochondrial %)
3. **Filter** — min_genes=200, max_genes<6000, pct_counts_mt<15%
4. **Normalize** — `normalize_total()` + `log1p()`
5. **HVG selection** — min_mean=0.0125, max_mean=3, min_disp=0.5
6. **Dimensionality reduction** — PCA (arpack) → neighbors (n=15, pcs=30) → UMAP
7. **Clustering** — Leiden at resolution=0.5
8. **Cell type annotation** — Manual cluster labeling (T-cells, B-cells, Monocytes, NK cells, DCs, Platelets)
9. **Marker genes** — Wilcoxon rank-sum via `sc.tl.rank_genes_groups()`

Processed data is cached as `cache/filtered_feature_bc_matrix-matrix.h5ad` (HDF5/AnnData format).

### Other Scripts

- **ode_example.py** — scvelo RNA velocity on a pancreas dataset (in `data/Pancreas/`); covers moment computation, dynamic model fitting, and velocity embeddings.
- **ros.py** — Standalone bioinformatics utilities: GC content, reverse complement, codon translation (uses `CODON.csv`), Fibonacci/population genetics, sequence alignment. No external dependencies beyond standard library + pandas.

### Data Layout

```
filtered_feature_bc_matrix/   # Raw 10x Genomics MTX input
cache/                        # Cached AnnData (.h5ad) files
data/Pancreas/                # scvelo example dataset
figures/                      # Output plots
txt_files/                    # Text outputs
CODON.csv                     # Genetic code lookup table
```

## Key Dependencies

No requirements.txt exists. Core packages: `scanpy`, `scvelo`, `pandas`, `numpy`, `matplotlib`, `seaborn`.
