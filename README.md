# SITTF_GRN

A Scale-Invariant Task Transformation Framework for Gene Regulatory Network Inference from Time-Series Data

## Workflow Overview

The implementation follows a three-step pipeline:

### 1. Data Generation

Datasets are generated according to the experimental settings described in Tables S2 and S3 of the Supplementary Materials. This includes the predefined network sizes, number of networks, number of profiles per structure, and number of time steps.

The dataset generation process consists of two types of datasets:

#### 1.1 Toy Dataset

For the toy datasets, the workflow uses `gene_network.py` and `gene_toydataset_ann.py`.

* `gene_network.py` is used to generate the ground-truth gene regulatory networks according to the predefined network structures and experimental settings.
* `gene_toydataset_ann.py` performs data transformation and prepares the generated expression trajectories into the unified feature representation required for supervised learning.

#### 1.2 E. coli Dataset

For the *E. coli* datasets, the gene regulatory networks are generated using **GeneNetWeaver (GNW)**. The generated networks and corresponding time-series expression data are then processed using the same data preparation procedure required for subsequent model training and evaluation.

The following parameters are used for dataset generation:

| Parameter                                   | Value                                           |
| ------------------------------------------- | ----------------------------------------------- |
| Number of time series                       | 10                                              |
| Duration of each time series                | 1000                                            |
| Number of measured points per time series   | 21                                              |
| Coefficient of noise term                   | 0                                               |
| Noise added after the simulation            | Model of noise in microarrays (used for DREAM4) |
| Normalize after adding noise (as in DREAM4) | Yes                                             |

### 2. Data Preparation

The generated data are processed and converted into training, validation, and testing sets using the script `gene_toydataset_ann`. This step transforms the raw expression trajectories into the unified feature representation required for supervised learning.

### 3. Model Training and Evaluation

Model training and performance evaluation are conducted using the script `gene_models_one_run`. This module trains the selected machine learning models and reports the corresponding evaluation metrics.
