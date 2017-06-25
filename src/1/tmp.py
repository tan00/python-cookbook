#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Docstring...
"""

from collections import Iterable
from collections import defaultdict
import os

dictlist = defaultdict(list)
dictlist['a'].append(3)
dictlist['a'].append(4)
dictlist['b'].append(5)
print( dictlist['a'] )
print( dictlist['b'] )


dictset = defaultdict(set)
dictset['a'].add(3)
dictset['a'].add(4)
dictset['a'].add(4)
dictset['b'].add(5)
print( dictlist['a'] )
print( dictlist['b'] )

