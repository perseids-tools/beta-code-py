# coding: utf-8

import json
import os
import re
import unicodedata

with open(os.path.join(os.path.dirname(__file__), 'vendor/beta-code-json/beta_code_to_unicode.json')) as json_file:
  BETA_CODE_TO_UNICODE_MAP = json.load(json_file)

with open(os.path.join(os.path.dirname(__file__), 'vendor/beta-code-json/unicode_to_beta_code.json')) as json_file:
  UNICODE_TO_BETA_CODE_MAP = json.load(json_file)

def greek_to_beta_code(greek, custom_map=None):
  if custom_map is None:
    custom_map = {}

  updated_map = {}
  updated_map.update(UNICODE_TO_BETA_CODE_MAP)
  updated_map.update(custom_map)

  chars = list(unicodedata.normalize('NFC', greek))
  mapped = list(map(lambda x: updated_map.get(x, x), chars))

  return u''.join(mapped)

def beta_code_to_greek(beta_code, custom_map=None):
  if custom_map is None:
    custom_map = {}

  updated_map = {}
  updated_map.update(BETA_CODE_TO_UNICODE_MAP)
  updated_map.update(custom_map)

  beta_code_characters = list(unicodedata.normalize('NFC', beta_code))
  greek_characters = []
  start = 0

  max_beta_code_character_length = len(max(updated_map.keys(), key=len))

  while start < len(beta_code_characters):
    current_character = beta_code_characters[start]
    new_start = start + 1
    max_length = min(len(beta_code_characters), start + max_beta_code_character_length)

    last = new_start
    while last <= max_length:
      string_slice = u''.join(beta_code_characters[start : last])

      if string_slice in updated_map:
        current_character = updated_map[string_slice]
        new_start = last

      last += 1

    greek_characters.append(current_character)
    start = new_start

  return sigma_to_end_of_word_sigma(u''.join(greek_characters))

def sigma_to_end_of_word_sigma(string):
  regex = re.compile(u'σ(?=[,.:;·\s]|$)')

  return re.sub(regex, u'ς', string)
