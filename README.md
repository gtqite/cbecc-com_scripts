# CBECC-Com Python Scripts

This repository is for storing python scripts to be used with CBECC-com. Scripts are primarily written for Jupyter Notebook with instructions in each script on how to use them.

## Getting Started

### Prerequisites

Recommended: [Anaconda](https://www.anaconda.com/distribution/) includes all python environments and IDE needed to run all the scripts.

If not using Anaconda, install the following:
- [Python 3.6](https://www.python.org/downloads/) or later
- [Jupyter Notebook](https://jupyter.org/install)
- [LXML](https://lxml.de/installation.html)
- [Pandas](https://pandas.pydata.org/getpandas.html)

### Running the scripts

1. Open the Jupyter Notebook and navigate to the location on your computer where the CBECC-Com scripts are saved
2. Click on the .ipynb file for the script you want to run.
3. Follow the instructions for each script.

## Currently available scripts

### VAV Box Scripts
- Make_VAV - Creates a text file in the xml format to paste into CBECC-com when opening in text editor.
- Pull Autosized VAV capacities - Extracts the CBECC-com autosized values and hard-codes it back to remove watermark.
- Remove VAV reheat coil capacity - Example script to remove hard-coded capacities so CBECC-com can autosize them.
- Update VAV box inputs in Excel - Allows changing VAV box inputs in Excel and reimports the values back into CBECC-com.

## Authors

* **Ken Takahashi** - *Initial work* - [kentakahas](https://github.com/kentakahas)

## Acknowledgments
