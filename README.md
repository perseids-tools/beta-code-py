# Beta Code Converter for Python

Converts Greek Beta Code to Greek characters and vice versa.

## Installation

`pip install beta-code`

(See project on [PyPI](https://pypi.org/project/beta-code/))

## Usage

```python
import beta_code

beta_code.greek_to_beta_code(u'χαῖρε ὦ κόσμε')
# => 'xai=re w)= ko/sme'

beta_code.beta_code_to_greek(u'mh=nin a)/eide qea\\ *phlhi+a/dew *)axilh=os')
# => 'μῆνιν ἄειδε θεὰ Πηληϊάδεω Ἀχιλῆος'
```

### With additional mappings

```python
beta_code.beta_code_to_greek(u'f2a/nac', custom_map={ u'f2': u'ϝ' })
# => 'ϝάναξ'
```

## Tests

`python -m unittest tests/test_beta_code.py`

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
python3 -m venv venv
. ./venv/bin/activate
pip3 install -r requirements.txt
```

* Bump version in `setup.py`
* Commit and push to GitHub
* On GitHub, create a new release
* Run `pip3 install wheel`
* Run `python3 setup.py sdist bdist_wheel`
* Run `python3 -m twine upload dist/*`

## Notes

For the mappings between Beta Code and Unicode, see [https://github.com/perseids-tools/beta-code-json](https://github.com/perseids-tools/beta-code-json).
