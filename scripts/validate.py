#!/usr/bin/python
# -*- coding: utf8 -*-

import os
from lxml import etree


PATH_DTD = "tei.dtd"
PATH_LETTERS = "data/"


class Validation:

    @staticmethod
    def validate(path_dtd, path_corpus) -> bool:
        dtd, is_valid, n = etree.DTD(open(path_dtd)), True, 0
        for f in sorted(os.listdir(path_corpus)):
            if f != ".DS_Store":
                tree = etree.parse(open(os.path.join(path_corpus, f)))
                valid = dtd.validate(tree)
                if not valid:
                    print(f, ":\n", dtd.error_log.filter_from_errors())
                    is_valid, n = False, n + 1
        print("Issues:", n)
        return is_valid


if __name__ == '__main__':

    Validation.validate(PATH_DTD, PATH_LETTERS)
