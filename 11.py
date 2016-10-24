#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = input('Enter the string: ')
first = s.split('h', 1)
second = first[1].rsplit('h', 1)
print(s.replace(second[0], second[0][::-1]))