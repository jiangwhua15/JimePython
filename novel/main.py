# -*- coding: utf-8 -*-

__author__ = 'jime'


import sys
import os
from scrapy.cmdline import execute

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

execute(['scrapy', 'crawl', 'baidu'])

