# A Multi-Level Visual Representation Dataset for Large-Scale Non-Financial Information Disclosure

This repository provides access to "A Multi-Level Visual Representation Dataset for Large-Scale Non-Financial Information Disclosure," a comprehensive resource developed to support research into the visual communication strategies employed in corporate sustainability reporting.

The dataset is intrinsically linked to our accompanying research paper, which elucidates the methodology and primary findings. Constructed from an extensive collection of 13,791 sustainability reports issued by publicly listed companies between 2006 and 2023, this dataset encompasses over 16 million lines of text and 545,751 images.

The core analytical framework focuses on three principal visual dimensions—text, images, and colors—which are further deconstructed into 18 specific sub-elements for granular examination. Researchers utilizing this dataset are kindly requested to cite both the dataset itself and the associated publication (https:doi.org/xxxx/xxxxx).

## How to Use This Dataset

This dataset is designed to support research into the visual aspects of non-financial corporate disclosures. Users can leverage the extracted features to:

（1）Analyze trends in the use of visual elements (text, images, colors) in sustainability reports over time.

（2）Investigate the relationship between visual representation characteristics and firm-level outcomes or stakeholder engagement.

（3）Develop and test models for predicting the impact of visual communication strategies.

（4）Explore the application of the novel indices, NFIVI_FC and NFIVI_EI, for assessing the visual impact of disclosures.

The primary data files, including extracted visual features and calculated indices, are provided in CSV format for ease of use with common data analysis software.

## Data Structure

The dataset is systematically organized into distinct records, primarily housed within the data/ directory and provided in CSV format for broad accessibility and ease of use with common data analysis software. Users should note the following structure and recommended practices when engaging with these records.

### Core Data Records

The core Data Records consist of three main components:

#### 1. Page-Level Metrics
- Named "pages indexs.xlsx"
- Each row represents a single page from a sustainability report
- "year", "code", "pages", the measured values for the 18 distinct visual sub-elements, and the derived page-specific "NFIVI_FC" and "NFIVI_EI". 
- This granular data facilitates in-depth analysis of visual element distribution and impact within individual reports

#### 2. Report-Level Metrics (Core Indicators and Information Entropy Index)
- Available in the file "pdfs indexs.xlsx"
- Each record corresponds to an entire sustainability report (PDF)
- Provides aggregated values for the 18 core visual indicators, the report's publication "year", "code" and the calculated report-level "NFIVI_EI".

#### 3. Report-Level Metrics (Feature-correlation Index via Mahalanobis Distance)
- Found in "NFIVI_FC.xlsx"
- Contains one record per report
- Includes "year", "code", and "NFIVI_FC"
- These report-level datasets enable broader comparative studies across firms, industries, or temporal periods

### Index Calculation Scripts

For researchers interested in the methodological underpinnings and potential replication or extension of the derived indices, Python scripts are provided within the scripts/index_calculation/ subfolder:

- "Page Mahalanobis Distance calculation.py"- Details the calculation of NFIVI_FC at the page level
- "Total Mahalanobis Distance calculation.py"- Covers the report-level NFIVI_FC using Mahalanobis distance
- "Image Information Entropy.py"- Outlines the derivation of the NFIVI_EI for both page and report levels

These index calculation scripts offer transparency into the generation of the key novel metrics.

## Citation

If you use this dataset or the accompanying paper in your research, please cite: (https:doi.org/xxxx/xxxxx).
