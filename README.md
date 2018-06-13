# Beta Code Converter for Python

## Overview

Converts Greek beta code to Greek characters and vice versa.

## Installation

`pip install beta_code`

## Usage

```python
import beta_code

beta_code.greek_to_beta_code('χαῖρε ὦ κόσμε')
# => 'xai=re w)= ko/sme'

beta_code.beta_code_to_greek('mh=nin a)/eide qea\\ *phlhi+a/dew *)axilh=os')
# => 'μῆνιν ἄειδε θεὰ Πηληϊάδεω Ἀχιλῆος'

```

## Tests

`python -m unittest tests/test_beta_code.py`

### In Python 2

`cd tests/ && python -m unittest test_beta_code`

## Packaging

```bash
python3 -m pip install --user --upgrade setuptools wheel
python3 setup.py sdist bdist_wheel
python3 -m pip install --user --upgrade twine
twine upload dist/*
```

## Notes

For the mappings between beta code and Unicode, see [https://github.com/zfletch/beta-code-json](https://github.com/zfletch/beta-code-json).

