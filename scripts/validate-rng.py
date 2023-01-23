#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import requests
from io import StringIO
from lxml import etree

PATH_LETTERS = "data/letters/"
schema = requests.get('https://tei-c.org/release/xml/tei/custom/schema/relaxng/tei_all.rng').text

#relaxng_doc = etree.parse(StringIO(schema))
relaxng_doc = etree.fromstring(bytes(schema, encoding='utf-8'))
tei_relaxng = etree.RelaxNG(relaxng_doc)

def validateTei(tei_relaxng , path_corpus):
    for f in sorted(os.listdir(path_corpus)):
        if f != ".DS_Store":
            mytree = etree.parse(open(os.path.join(path_corpus, f)))
            try:
                result = tei_relaxng.assert_(mytree)
            except AssertionError as err:
                print('FATAL ERROR in ' + f)
                print('TEI validation error:' + err)
    return is_valid

if not validateTei(tei_relaxng, PATH_LETTERS): print("Validation FAILED.")
else: print("Is valid.")
