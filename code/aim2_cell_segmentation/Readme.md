# Cell Segmentation Methods

## Cellotype
https://github.com/tanlabcode/CelloType

Require GPU resource

## Baysor
https://kharchenkolab.github.io/Baysor/dev/segmentation/

Example command for runing Baysor
```sh
/home/jiyaoz/statsproject/baysor/bin/baysor/bin/baysor run /home/jiyaoz/statsproject/xenium_mouse_brain/grid_transcript/transcripts_x1_y1.parquet \
    -o /home/jiyaoz/statsproject/xenium_mouse_brain/baysor_output/x1_y1 \
    -m 30 \
    -s 5 \
    -x x_location -y y_location -z z_location \
    -g feature_name
```

**Parameters**

- scale 

Specifies the expected radius of a cell. It doesn't have to be precise, but the wrong setup can lead to over- or under-segmentation. This parameter is inferred automatically if cell centers are provided.

- min-molecules-per-cell 

The number of molecules, required for a cell to be considered as real. It really depends on the protocol. For instance, for ISS it's fine to set it to 3, while for MERFISH it can require hundreds of molecules.

**Segmentation Outputs**

- segmentation_counts.loom or segmentation_counts.tsv

Count matrix with segmented stats. In the case of loom format, column attributes also contain the same info as segmentation_cell_stats.csv.

- segmentation.csv

Segmentation info per molecule.

- segmentation_cell_stats.csv

Diagnostic info about cells. The following parameters can be used to filter low-quality cells.

- segmentation_polygons_2d/3d.json.

Polygons used for visualization in GeoJSON format.

# Dataset 

## xenium_mouse_brain
https://www.10xgenomics.com/datasets/xenium-prime-fresh-frozen-mouse-brain

Output description file
https://www.10xgenomics.com/support/software/xenium-onboard-analysis/latest/analysis/xoa-output-understanding-outputs

Example code
https://www.10xgenomics.com/support/software/xenium-onboard-analysis/latest/advanced/example-code

**Scale**

PhysicalSizeX = 0.2125 µm/pixel

PhysicalSizeY = 0.2125 µm/pixel

Image scale: 34154 x 23912 pixel (full resolution)

Physical_width_um = 34154 * 0.2125  # ≈ 7252 µm

Physical_height_um = 23912 * 0.2125  # ≈ 5086 µm

**Files**

- Morphology map

The morphology_focus/directory contains the 2D autofocus projection images for the nuclei DAPI stain image, as well as three additional stain images for Xenium outputs generated with the multimodal cell segmentation assay workflow. These files are in multi-file OME-TIFF format. 

morphology_focus_0000.ome.tif: DAPI image

morphology_focus_0001.ome.tif: boundary (ATP1A1/E-Cadherin/CD45) image

morphology_focus_0002.ome.tif: interior - RNA (18S) image

morphology_focus_0003.ome.tif: interior - protein (alphaSMA/Vimentin) image


- Cell summary file

The cell summary file (cells.csv.gz) in gzipped CSV format contains data to help QC the transcript counts for each identified cell. The file contains one row for each cell, with the following columns:

cell_id, Unique ID of the cell, consisting of a cell prefix and dataset suffix

x_centroid, X location of the cell centroid in µm

y_centroid, Y location of the cell centroid in µm

transcript_counts, Molecule count of gene features with Q-Score ≥ 20

control_probe_counts, Molecule count of negative control probes

genomic_control_counts, Count of genomic control codewords (for Xenium Prime data)

control_codeword_counts, Count of negative control codewords

unassigned_codeword_counts, Count of unassigned codewords

deprecated_codeword_counts, Count of deprecated codewords

total_counts, Sum total of transcript_counts, control_probe_counts, 
control_codeword_counts, genomic_control_counts (for Xenium Prime data), and unassigned_codeword_counts

cell_area, The two-dimensional area covered by the cell in µm2

nucleus_area, The two-dimensional area covered by the nucleus in µm2

nucleus_count, Count of detected nuclei

segmentation_method, Cell segmentation method


- Cell and nucleus segmentation files

The nucleus_boundaries.csv.gz and cell_boundaries.csv.gz are the CSV representation of the nucleus and cell boundaries, respectively. Each row represents a vertex in the boundary polygon of one cell. The boundary points for each cell appear in clockwise order, and the first and the last points are duplicates to indicate a closed polygon. Both files contain the following columns:



# Pipeline (for Baysor) 
(1) see basic information of the dataset (data_inforamtion.ipynb)

(2) grid transcripts and image signals (grid_image_and_transcript.ipynb)

(3) downsample transcripts (downsample_transcript.py)

(4) run baysor on full resoluation and downsample data (run_baysor_resolution.sh / run_baysor.sh)

(5) analysis final results (baysor_visualize_output.ipynb)




