#!/usr/bin/env python3
# -*- coding: utf-8 -*-

string = input('Enter the string: ')
if string and string != ' ':
    print(string.count(' ') + 1)
else:
    print(0)