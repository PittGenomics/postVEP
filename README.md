# postVEP

Python package helps you analyze Variant Effect Predictor (VEP) result.

## Prerequisite

- Python 3

## Installation

- `pip install .`

## Quick Start

``` python
    from postVEP import VEPresult
    r = VEPresult('./example/output_with_plugin.tsv')
    # r.data is a pandas DataFrame
```