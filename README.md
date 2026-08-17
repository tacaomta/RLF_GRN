# SITTF_GRN
A Scale-Invariant Task Transformation Framework for Gene Regulatory Network Inference from Time-Series Data
Workflow Overview

The implementation follows a three-step pipeline:

1. Data Generation

Datasets are generated according to the experimental settings described in Tables S1 and S2 of the Supplementary Materials. This includes the predefined network sizes, number of networks, number of profiles per structure, and number of time steps.

2. Data Preparation

The generated data are processed and converted into training, validation, and testing sets using the script gene_toydataset_ann. This step transforms the raw expression trajectories into the unified feature representation required for supervised learning.

3. Model Training and Evaluation

Model training and performance evaluation are conducted using the script gene_models_one_run. This module trains the selected machine learning models and reports the corresponding evaluation metrics.
