# Gene Data Consolidation Script

## 🧬 Project Overview
This project contains a Python script designed to solve a common data formatting problem in bioinformatics. It processes a single CSV file that incorrectly contains two separate gene expression datasets merged side-by-side.

The script identifies the common genes present in both datasets, cleans the data, and merges them into a single, well-structured CSV file.

## 🎯 Key Features
- **Parses Malformed Data**: Intelligently splits a wide, improperly merged file into two distinct datasets.
- **Data Cleaning**: Trims whitespace and standardizes gene identifiers by removing version suffixes from Ensembl IDs.
- **Data Merging**: Performs an inner merge to find the intersection of genes between the two datasets.
- **Clean Output**: Generates a single, tidy CSV file containing the combined data for the common genes.

## 🚀 How to Run

### 1. Prerequisites
- Python 3
- pandas library

### 2. Setup
1. Clone or download this repository.
2. Install the required library:
   ```bash
   pip install -r requirements.txt
   ```
3. Place your input data file in the project folder. See the "Data Format" section below for details.

### 3. Execution
Navigate to the project directory in your terminal and run the script:
```bash
python process_genes.py
```
A new file, `common_genes_with_values.csv`, will be created with the results.

---
## 📄 Data Format

**Important**: This repository does not contain the full raw data file due to its size and for data privacy best practices.

The script expects a file named `Row read - Copy.csv` in the root directory.

To see the expected structure, you can create a `sample_data.csv` file. This file should contain the same headers as the original data but with only a few rows of sample content. The script can then be temporarily modified to read `sample_data.csv` for testing purposes.