#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = input('Enter the string: ')
count_f = s.count('f')
if count_f == 1:
    print(s.find('f'))
elif count_f > 1:
    print(s.find('f'), s.rfind('f'), sep='\n')