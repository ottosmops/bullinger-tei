#!/usr/bin/python
# -*- coding: utf8 -*-

import os
from lxml import etree


PATH_DTD = "tei.dtd"
PATH_LETTERS = "data/letters/"


class Validation:

    @staticmethod
    def validate(path_dtd: str, path_corpus: str) -> bool:
        dtd, is_valid, issues, errors = etree.DTD(open(path_dtd)), True, 0, 0
        for f in sorted(os.listdir(path_corpus)):
            if f != ".DS_Store":
                try:
                    if not dtd.validate(etree.parse(open(os.path.join(path_corpus, f)))):
                        print(f, dtd.error_log.filter_from_errors())
                        is_valid, issues = False, issues + 1
                except:
                    print("FATAL ERROR in", f)
                    errors += 1
        print("Errors:", errors)
        print("Issues:", issues)
        return is_valid


if __name__ == '__main__':

    if not Validation.validate(PATH_DTD, PATH_LETTERS): print("Validation FAILED.")
    else: print("Is valid.")
