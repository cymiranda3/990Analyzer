# 990Analyzer
Analyzer for 990 data

## To Run:
1. Put all EINs into list in `get990CSV.py`.
2. Run `python get990CSV.py` in `terminal`. This downloads all of the 990 files for an EIN for the years 2012-2017 into the `990csv_files` folder.
3. Copy the list of EINs from `get990CSV.py` to `990analysis2.py`.
4. Run `python 990analysis2.py` in terminal. This parses all of the CSVs downloaded and calculates a simple Dietz return. It stores the estimated returns in a file (named according to the EIN list) in `output_files`.

## Note:
- Since 990s include data for up to 4 years prior to the filing year, the file calculates returns for *all years* given in a 990.
- Additionally, sometimes changes will be made to the past figures. Thus, I would recommend looking at the output file and using the most common value for any given year.
- The output files include a "timecode". This refers to the column in the 990 that the estimated return is being calculated from. CY = current year, so the current data on the 990. 1Y = 1 year prior, 2Y = 2 years prior, etc...
