# postVEP

The Python package helps you analyze Variant Effect Predictor (VEP) result.

## Prerequisite

- Python 3

## Installation

- `pip install .`

## Quick start

``` python
from postVEP import VEPresult
r = VEPresult('./example/output_with_plugin.tsv') # r.data is a pandas DataFrame
print(r.get_all_col_names())
print(r.get_col_info('gnomAD_exomes_ASJ_AF'))
```

## Report issuse

https://github.com/PittGenomics/postVEP/issues
