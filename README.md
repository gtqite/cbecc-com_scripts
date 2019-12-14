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

### Python Tutorials
It is recommended to have basic python skills to understand and modify any of the scripts. There are many basic python tutorials available online and sny of them should give you enough knowledge for these scripts.

At minimum, know how to do the following:
- Data Types (string, number, list, dictionary)
- if statement
- for statement
- Exceptions
- LXML - Parsing and writing xml
- Pandas - Creating dataframes

Other Tutorials:
- [LXML Tutorial](https://lxml.de/tutorial.html)
- [Pandas Tutorial](https://www.learndatasci.com/tutorials/python-pandas-tutorial-complete-introduction-for-beginners/)
- [Jupyter Notebook Tutorial](https://www.dataquest.io/blog/jupyter-notebook-tutorial/)


### Running the scripts

1. Open the Jupyter Notebook and navigate to the location on your computer where the CBECC-Com scripts are saved
2. Click on the .ipynb file for the script you want to run.
3. Follow the instructions for each script.

## Currently available scripts

### Parser
- CBECC-Com_Data_Parser - Parses the CBECC-com file into Excel for viewing only. Only terminal units are editable from the VAV Box Scripts folder. More equipment will be available soon.

### VAV Box Scripts
- Make_VAV - Creates a text file in the xml format to paste into CBECC-com when opening in text editor.
- Pull Autosized VAV capacities - Extracts the CBECC-com autosized values and hard-codes it back to remove watermark.
- Remove VAV reheat coil capacity - Example script to remove hard-coded capacities so CBECC-com can autosize them.
- Update VAV box inputs in Excel - Allows changing VAV box inputs in Excel and reimports the values back into CBECC-com.

### Planned scripts
- Space Data Editor
- Fan coil editors
- AHU editor
- Lighting editor
- Central Plant editor

## Basics of Scripting in CBECC-Com

### CBECC-Com XML Structure
TBD
### Parsing and Writing Using LXML
TBD


## Authors

* **Ken Takahashi** - *Initial work* - [kentakahas](https://github.com/kentakahas)

## Acknowledgments
