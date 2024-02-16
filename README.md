# WIW coding challenge round
This repository contains the solution python files and resulting CSV files
as part of the coding challenge.

### Proposed approaches

There are 2 proposed solutions to the coding challenge.

1. Simple solution which uses the pandas library pivot table functionality.
Files as part of this approach are:

```
  a.simple_solution.py -- Code file
  b.result_simple.csv -- Resulting CSV file
```
2. Incremental approach solution which uses hash map functionality to incrementally process rows from each file.
   This approach is meant to be used when the aggregated data set might not fit into memory.
Files as part of this approach are:

```
  a.incremental_solution.py -- Code file
  b.result_incremental.csv -- Resulting CSV file
```

### Pre-requisites

Only pandas library is required for executing code files. All other packages ship as standard with Python3 library

Pandas library can be installed with the following command

```
  pip install pandas
```

