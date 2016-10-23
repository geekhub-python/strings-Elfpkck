#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = input('Enter the string: ')
new = ''
for i, l in enumerate(s):
    if i != s.find('h') and i != s.rfind('h'):
        l = l.replace('h', 'H')
    new += l
print(new)