# -*- coding: UTF-8 -*-

import re

WHITESPACE_TRIM = re.compile('[\W_]+')

def trim_whitespace(text):
    return WHITESPACE_TRIM.sub('', text)

