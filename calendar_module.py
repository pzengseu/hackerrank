#!/bin/python

import calendar

nums = map(int, raw_input().split())
print (list(calendar.day_name)[calendar.weekday(nums[2], nums[0], nums[1])]).upper()