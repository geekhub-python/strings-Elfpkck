#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = input('Enter the string: ')
first = s[:sum(divmod(len(s), 2))]
print(s.replace(first, '') + first)