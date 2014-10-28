#!/usr/bin/env python

import string

def rsttitle(title, punctuation, overline=False):
    trimmed_title = title.strip()
    adornment = punctuation*punctuation
    response = '\n'.join((adornment, trimmed_title, adornment)) if overline \
               else '\n'.join((trimmed_title, adornment))
    return response

