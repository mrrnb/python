#!/usr/bin/env python
# coding: utf-8

bonus1 = 100000 * 0.1
bonus2 = bonus1 + 100000 * 0.075
bonus4 = bonus2 + 200000 * 0.05
bonus6 = bonus4 + 200000 * 0.03
bonus10 = bonus6 + 400000 * 0.015

i = int(raw_input('Input Your GAIN: '))
if i <= 100000:
    bonus = i * 0.1
elif i <= 200000:
    bonus = bonus1 + (i - 100000) * 0.075
elif i <= 400000:
    bonus = bonus2 + (i - 200000) * 0.05
elif i <= 600000:
    bonus = bonus4 + (i - 400000) * 0.03
elif i <= 1000000:
    bonus = bonus6 + (i - 600000) * 0.015
else:
    bonus = bonus10 + (i - 1000000) * 0.015

print 'bonus = ',bonus


