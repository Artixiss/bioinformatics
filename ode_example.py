import scvelo as scv
import scanpy as sc

# 1. Load data
adata = scv.datasets.pancreas()

# 2. Refined Preprocessing
# This handles the filtering (where n_top_genes lives) and the scaling separately 
scv.pp.filter_and_normalize(adata, min_shared_counts=20)

# 3. Compute Moments (The "Smoothing" step for the ODE)
# This is mathematically required to denoise the Spliced/Unspliced counts
scv.pp.moments(adata, n_pcs=30, n_neighbors=30)

# 4. Solve the ODEs (The "Dynamical" model)
scv.tl.recover_dynamics(adata)
scv.tl.velocity(adata, mode='dynamical')
scv.tl.velocity_graph(adata)

# 5. Visualize the "Flow"
scv.pl.velocity_embedding_stream(adata, basis='umap')