## Benchmark Aflow Data Sets for Machine Learning
This repository contains the code supplement to *Benchmark AFLOW Data Sets for Machine Learning* by CL Clement, SK Kauwe, and TD Sparks, to be published in Integrating Materials and Manufacturing Innovation. 

The data sets can be downloaded together as a compressed ZIP file at https://doi.org/10.6084/m9.figshare.11954742

### Licensing
The code and downloadable data sets for this project are provided "as-is" under the MIT Licence, which allows for personal, public, and commerical use and modification. However, we ask that you please respect the license of the original data source (aflowlib.org), and refrain from using the data sets for proprietary or commercial purposes. 

### Contents
#### get_aflow_data.py
Functions for downloading compound property and crystal structure data via the AFLOW API. Property values are encoded as JSON files, and structure data as crystallographic information files (CIFs).

#### process_data.py
A script to split property CSV files into separate training, validation, and testing data sets.

#### property_to_csv.py
A script for iterating over each compound, collecting data values by property, and grouping them into CSV files.

#### valid_targets.csv
A single column CSV listing the queriable material properties. 
