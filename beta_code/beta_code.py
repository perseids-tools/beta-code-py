import unicodedata
import json

with open('vendor/beta-code-json/beta_code_to_unicode.json') as json_file:
  BETA_CODE_TO_UNICODE_MAP = json.load(json_file)

with open('vendor/beta-code-json/unicode_to_beta_code.json') as json_file:
  UNICODE_TO_BETA_CODE_MAP = json.load(json_file)

def greek_to_beta_code(greek):
  chars = list(unicodedata.normalize('NFC', greek))
  mapped = list(map(lambda x: UNICODE_TO_BETA_CODE_MAP.get(x, x), chars))

  return u''.join(mapped)

def beta_code_to_greek(string):
  return u'χαῖρε ὦ κόσμε'
