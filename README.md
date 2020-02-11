# Beta Code Converter for Python

Converts Greek beta code to Greek characters and vice versa.

## Installation

`pip install beta-code`

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

## Updating JSON

```bash
git subtree pull --prefix beta_code/vendor/beta-code-json/ https://github.com/perseids-tools/beta-code-json master --squash
```

In the case of a merge conflict:

```bash
git checkout --theirs vendor/beta-code-json/
git add vendor/beta-code-json
git commit
```

## Publishing

* Install dependencies:

```bash
python3 -m pip install --user --upgrade setuptools wheel
python3 -m pip install --user --upgrade twine
```

* Bump version in `setup.py`
* Commit and push to GitHub
* On GitHub, create a new release
* Run `python3 setup.py sdist bdist_wheel`
* Run `python3 -m twine upload dist/*`

## Notes

For the mappings between beta code and Unicode, see [https://github.com/perseids-tools/beta-code-json](https://github.com/perseids-tools/beta-code-json).

