# Task Sheet Repository

This repository contains scripts for performing statistical and similarity analyses  on multiple scenario datasets.  
All outputs are automatically saved to the outputs/ and synthetic/ directories.               

------------------------------------------------------------------------------------
Project Structure
------------------------------------------------------------------------------------

01_Task_sheet/
├── src/
│   ├── compare.py                 # Task 1a: K-S Statistic
│   ├── system_states.py           # Task 1b: System States Summary
│   ├── common_ks_state.py         # Task 1c: Common-State K-S
│   ├── plot_cdfs.py               # Task 1d: CDF of K-S values
│   ├── euclidean_distance.py      # Task 2a: Euclidean Distances
│   ├── plot_histograms.py         # Task 2b: Histograms
│   ├── tsne_plot.py               # Task 2c: t-SNE
│   ├── pca_plot.py                # Task 2d: PCA
│   ├── train.py                   # Task 3: GAN Training
│   ├── tsheet2_data_preparation.py # Task Sheet 2 – Task 1a: normalisation + subsets + synthetic
│   ├── tsheet2_min_max.py          # Task Sheet 2 – Task 1b: MinMax statistic
│   ├── tsheet2_gradient.py         # Task Sheet 2 – Task 1b: Gradient statistic
│   ├── tsheet2_steadytime.py       # Task Sheet 2 – Task 1b: Steadytime statistic
│   ├── tsheet2_entropy.py          # Task Sheet 2 – Task 1b: Shannon entropy
│   ├── tsheet2_plotting.py         # Task Sheet 2 – Task 1b: CDF/CCDF plots
│   ├── tsheet2_task2_cusum.py      # Task Sheet 2 – Task 2a: CUSUM detector
│   ├── ewma_detector.py            # Task Sheet 2 – Task 2b: EWMA detector
│   ├── fusion.py                   # Task Sheet 2 – Task 2c: Fusion logic
│   ├── sheet2_detector.py          # Task Sheet 2 – Task 2d: Detector selector
│   ├── sheet2_statistics.py        # Executes all Task Sheet 2 – Task 1 statistics
│   ├── toolbox.py                  # Unified toolbox
│
├── data/
│   ├── EpicLog_Scenario 1_19_Oct_2018_14_44.csv
│   ├── EpicLog_Scenario 2_19_Oct_2018_14_56.csv
│   ├── EpicLog_Scenario 3_19_Oct_2018_15_02.csv
│   ├── EpicLog_Scenario 4_19_Oct_2018_15_23.csv
│   ├── EpicLog_Scenario 5_19_Oct_2018_15_45.csv
│   ├── EpicLog_Scenario 6_19_Oct_2018_16_06.csv
│   ├── EpicLog_Scenario 7_07_Nov_2018_14_40.csv
│   └── EpicLog_Scenario 8_07_Nov_2018_14_57.csv
│
├── outputs/                        # Auto-generated output directory
├── synthetic/                      # Generated synthetic datasets (Task 3)
└── README.md                       # This file


=================================================================================
                                Prerequisites
=================================================================================

Before running the scripts, set up a Python environment.
Python 3.8+ is required.


=================================================================================
                                Required Libraries
=================================================================================

Create a requirements.txt file in the project root with the following contents:

pandas
numpy
matplotlib
scikit-learn
torch

Then install all dependencies with:

    pip install -r requirements.txt


*************************************************************************************
                                Description of Tasks & Outputs
*************************************************************************************

All outputs are automatically saved to the `outputs/` and `synthetic/` directories.

=================================================================================
## Task Sheet 1: Statistical Analysis
=================================================================================

### Task 1a — K-S Statistic  
**Script:** `compare.py`  
**Output:** `task01_KS_Statistic.csv`  
Computes detailed Kolmogorov–Smirnov statistics between all scenario pairs for each sensor.

---

### Task 1b — System States Summary  
**Script:** `system_states.py`  
**Output:** `task1b_system_states_summary.txt`  
Summarizes unique and common system states.

---

### Task 1c — Common State K-S  
**Script:** `common_ks_state.py`  
**Output:** `task1c_common_state_avg_ks.csv`  
Computes average K-S statistic per sensor within the most common system state.

---

### Task 1d — CDF Plots  
**Script:** `plot_cdfs.py`  
**Outputs:**  
- `task1d_cdf_without_states.png`  
- `task1d_cdf_with_states.png`

---

### Task 2a — Euclidean Distance  
**Script:** `euclidean_distance.py`  
**Output:** `task2a_euclidean_distances.csv`

---

### Task 2b — Histogram Visualization  
**Script:** `plot_histograms.py`  
**Outputs:**  
- `task2b_histogram_full_range.png`  
- `task2b_histogram_focused_stacked.png`

---

### Task 2c — t-SNE Visualization  
**Script:** `tsne_plot.py`  
**Outputs:**  
- `task2c_tsne_plot_perplexity_5.png`  
- `task2c_tsne_plot_perplexity_30.png`  
- `task2c_tsne_plot_perplexity_60.png`

---

### Task 2d — PCA Visualization  
**Script:** `pca_plot.py`  
**Output:** `task2d_pca_plot.png`

=================================================================================
## Task Sheet 1 – Task 3: Synthetic Data (GAN)
=================================================================================

### Task 3a — GAN Architecture  
**Script:** `train.py`  
**Output directory:** `synthetic/`  
Implements the generator and discriminator for ICS synthetic data.

---

### Task 3b — Custom Loss Function  
Implemented in `train.py` (feature-based loss).

---

### Task 3c — Hyperparameter Tuning  
Implemented in `train.py`.

---

### Task 3d — Training & Outputs  
**Script:** `train.py`  
**Outputs:**  
- `ICS_synthetic_combined.csv`  
- `ICS_synthetic_preview200.csv`

---

### Task 3e — Optimization & Evaluation  
Evaluation included during GAN training.

=================================================================================
## Task Sheet 2: Similarity Statistics & Anomaly Detection
=================================================================================

### Task 1a — Data Preparation  
**Script:** `tsheet2_data_preparation.py`  
Creates normalized Train Day, Real_A, Real_B, and 2.5-day synthetic dataset.

---

### Task 1b — Similarity Statistics  
Scripts:  
- `tsheet2_min_max.py`  
- `tsheet2_gradient.py`  
- `tsheet2_steadytime.py`  
- `tsheet2_entropy.py`  
- `tsheet2_plotting.py`  

Outputs: violation CSVs, CDF/CCDF plots for:  
- MinMax  
- Gradient  
- Steadytime  
- Entropy

---

### Task 2a — Non-parametric CUSUM  
**Script:** `tsheet2_task2_cusum.py`  
Outputs:  
- `cusum_params.csv`  
- `cusum_stats_test.csv`  
- `cusum_alarms_test.csv`  
- `cusum_final_decision.csv`

---

### Task 2b — EWMA Detector  
**Script:** `ewma_detector.py`  
Outputs:  
- `ewma_parameters.csv`  
- `ewma_alarms.csv`

---

### Task 2c — Final Decision Fusion  
**Script:** `fusion.py`  
Aggregates alarms into a global attack decision.

---

### Task 2d — Detector Manager  
**Script:** `sheet2_detector.py`  
Selects between: `--method cusum` or `--method ewma`.

=================================================================================
## Task Sheet 3: Toolbox
=================================================================================

A unified command-line interface for all tasks.  
**Script:** `toolbox.py`

Modes:  
- `analyze` — Task Sheet 1  
- `generate` — GAN training  
- `statistics` — Task Sheet 2 (Task 1)  
- `detect` — Task Sheet 2 (CUSUM/EWMA)

=================================================================================
## Running Scripts Individually (Task Sheet 1)
=================================================================================

You can run any script directly using:

```bash
python3 src/<script_name>.py

# Task 1a: K-S statistic
python3 src/compare.py

# Task 1b: System states summary
python3 src/system_states.py

# Task 1c: Common-state K-S per sensor
python3 src/common_ks_state.py

# Task 1d: CDF plots of K-S values
python3 src/plot_cdfs.py

# Task 2a: Euclidean distances
python3 src/euclidean_distance.py

# Task 2b: Histogram of distances
python3 src/plot_histograms.py

# Task 2c: t-SNE (tuned)
python3 src/tsne_plot.py

# Task 2d: PCA (tuned)
python3 src/pca_plot.py

# Task 3a–e: GAN train + synth CSV
python3 src/train.py


=================================================================================
## Running Scripts Individually (Task Sheet 2)
=================================================================================

### Task 1a: Data Preparation  
python3 src/tsheet2_data_preparation.py

### Task 1b: MinMax Statistic  
python3 src/tsheet2_min_max.py

### Task 1b: Gradient Statistic  
python3 src/tsheet2_gradient.py

### Task 1b: Steadytime Statistic  
python3 src/tsheet2_steadytime.py

### Task 1b: Shannon Entropy Statistic  
python3 src/tsheet2_entropy.py

### Task 1b: Generate CDF/CCDF Plots  
python3 src/tsheet2_plotting.py

### Task 2a: CUSUM Detector  
python3 src/tsheet2_task2_cusum.py

### Task 2b: EWMA Detector  
python3 src/ewma_detector.py --train outputs/ts2_task1a/train_day_norm.csv --test outputs/ts2_task1a/real_B_norm.csv --out-dir outputs/ts2_task2/ewma

### Task 2c: Fusion Logic  
Used internally by the CUSUM script via fusion.py (no direct command).

### Task 2d: Detector Manager (Method Selector)

#### CUSUM:
python3 src/sheet2_detector.py --method cusum

#### EWMA:
python3 src/sheet2_detector.py --method ewma --train outputs/ts2_task1a/train_day_norm.csv --test outputs/ts2_task1a/real_B_norm.csv --out-dir outputs/ts2_task2/ewma

=================================================================================
## Running Through the Toolbox (Task Sheet 3)
=================================================================================

### Run All Task Sheet 1 Analyses
python3 src/toolbox.py -s analyze

### Run GAN Training (Task Sheet 1 – Task 3)
python3 src/toolbox.py -s generate

### Run All Task Sheet 2 Statistics (Task 1a + Task 1b)
python3 src/toolbox.py -s statistics

### Run Detection via Toolbox (Task Sheet 2 – Task 2)

#### CUSUM:
python3 src/toolbox.py -s detect -- --method cusum

#### EWMA:
python3 src/toolbox.py -s detect -- --method ewma --train outputs/ts2_task1a/train_day_norm.csv --test outputs/ts2_task1a/real_B_norm.csv --out-dir outputs/ts2_task2/ewma


