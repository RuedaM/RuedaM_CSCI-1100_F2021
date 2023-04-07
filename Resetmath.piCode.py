#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 15:41:07 2021

@author: maxrueda
"""
import sys
import math
print(math.pi)

math.pi=1
print(math.pi)

sys.modules.pop('math')

math.pi

import math
print(math.pi)