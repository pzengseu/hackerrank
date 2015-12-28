#!/usr/bin/env python

import os
[os.system('kill ' + num) for num in open('timing.log', 'r').read().split()]