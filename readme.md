# A Multi-Level Visual Representation Dataset for Large-Scale Non-Financial Information Disclosure

This repository provides access to the Non-Financial Information Disclosure Visual Representations Index (NFIVI) dataset, a comprehensive resource developed to support research into the visual communication strategies employed in corporate sustainability reporting.

The dataset is intrinsically linked to our accompanying research paper. Constructed from an extensive collection of 16,260 sustainability reports issued by Chinese listed companies between 2006 and 2025, this dataset encompasses metrics extracted from over 542,000 pages.

The core analytical framework focuses on three principal visual dimensions—Text, Image, and Color—which are further deconstructed into 18 specific granular indicators. Furthermore, the dataset introduces two novel indices to quantify visual composition:

- **NFIVI_FC (Feature-Correlation Index)**: Measures stylistic consistency via Mahalanobis Distance.
- **NFIVI_EI (Information Entropy Index)**: Assesses visual complexity based on color diversity.

Researchers utilizing this dataset are kindly requested to cite both the dataset itself and the associated publication.

## How to Use This Dataset

This dataset is designed to support research into the visual rhetoric and impression management of non-financial corporate disclosures. Users can leverage the extracted features to:

- **Trend Analysis**: Analyze the evolutionary trajectory of visual elements (text density, image types, color usage) in sustainability reports over nearly two decades.
- **Impact Studies**: Investigate the relationship between visual representation characteristics and firm-level outcomes (e.g., ESG ratings, investor sentiment) or stakeholder engagement.
- **Model Development**: Develop and test automated auditing tools or predictive models for corporate communication strategies.
- **Visual Metrics**: Explore the application of the novel indices, NFIVI_FC and NFIVI_EI, as proxies for "Visual Consistency" and "Visual Complexity."

## Data Structure

The dataset is systematically organized into distinct records, primarily provided in `.xlsx` format for broad accessibility and ease of use with common data analysis software.

### Core Data Records

The core dataset consists of three main files designed for multi-scale analysis:

#### 1. Page-Level Metrics

- **Filename**: `pages indices.xlsx`
- **Description**: This file provides granular data where each row represents a single page from a sustainability report.
- **Content**: Includes Year, Stock Code, Page Number, the measured values for the 18 distinct visual sub-elements (e.g., Words per Line, Image Area Ratio, Warm/Cool Colors), and the derived page-specific NFIVI_FC and NFIVI_EI scores.
- **Usage**: Facilitates in-depth analysis of visual element distribution within individual reports.

#### 2. Report-Level Metrics (Aggregated Features & Entropy)

- **Filename**: `pdfs indices.xlsx`
- **Description**: Each record corresponds to an entire sustainability report (PDF).
- **Content**: Provides the arithmetic means of the 18 core visual indicators for the whole document, along with the report's Year, Stock Code, and the calculated report-level NFIVI_EI (Information Entropy Index).

#### 3. Report-Level Metrics (Feature-Correlation Index)

- **Filename**: `NFIVI_FC.xlsx`
- **Description**: A specialized record for the report-level Feature-Correlation Index.
- **Content**: Includes Year, Stock Code, and the final NFIVI_FC score calculated via pairwise Mahalanobis distance.
- **Usage**: Enables broader comparative studies on stylistic consistency across firms, industries, or temporal periods.

### Index Calculation Scripts

For researchers interested in the methodological underpinnings and potential replication or extension of the derived indices, the Python scripts used for calculation are provided:

- `Page Mahalanobis Distance calculation.py`: Details the calculation of NFIVI_FC at the page level (distance from global centroid).
- `Total Mahalanobis Distance calculation.py`: Covers the report-level NFIVI_FC calculation using pairwise Mahalanobis distance to measure internal consistency.
- `Image Information Entropy.py`: Outlines the derivation of the NFIVI_EI (Shannon's Entropy based on color bins) for both page and report levels.

## Citation

If you use this dataset or the accompanying paper in your research, please cite:

Bingjie Li, Binglong Xia, Ze Cheng, Yitong Xu & Zhao Duan. A multi-level visual representation dataset for large-scale non-financial information disclosure. *Scientific Data* (2025). [Insert DOI Link Here]