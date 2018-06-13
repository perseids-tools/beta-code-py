# coding: utf-8

import json
import os
import re
import unicodedata

with open(os.path.join(os.path.dirname(__file__), 'vendor/beta-code-json/beta_code_to_unicode.json')) as json_file:
  BETA_CODE_TO_UNICODE_MAP = json.load(json_file)

with open(os.path.join(os.path.dirname(__file__), 'vendor/beta-code-json/unicode_to_beta_code.json')) as json_file:
  UNICODE_TO_BETA_CODE_MAP = json.load(json_file)

MAX_BETA_CODE_CHARACTER_LENGTH = len(max(BETA_CODE_TO_UNICODE_MAP.keys(), key=len))

def greek_to_beta_code(greek):
  chars = list(unicodedata.normalize('NFC', greek))
  mapped = list(map(lambda x: UNICODE_TO_BETA_CODE_MAP.get(x, x), chars))

  return u''.join(mapped)

def beta_code_to_greek(beta_code):
  beta_code_characters = list(unicodedata.normalize('NFC', beta_code))
  greek_characters = []
  start = 0

  while start < len(beta_code_characters):
    current_character = beta_code_characters[start]
    new_start = start + 1
    max_length = min(len(beta_code_characters), start + MAX_BETA_CODE_CHARACTER_LENGTH)

    last = new_start
    while last <= max_length:
      string_slice = u''.join(beta_code_characters[start : last])

      if string_slice in BETA_CODE_TO_UNICODE_MAP:
        current_character = BETA_CODE_TO_UNICODE_MAP[string_slice]
        new_start = last

      last += 1

    greek_characters.append(current_character)
    start = new_start

  return sigma_to_end_of_word_sigma(u''.join(greek_characters))

def sigma_to_end_of_word_sigma(string):
  regex = re.compile(u'σ(?=[,.:;·\s]|$)')

  return re.sub(regex, u'ς', string)
