#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = input('Enter the string: ')
new = ''
for i in range(len(s)):
    if i % 3 != 0:
        new += s[i]
print(new)