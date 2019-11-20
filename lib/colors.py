#!/usr/bin/env python3

import sys
import colorama

if sys.platform == 'win32':
    colorama.init()

R = "\033[%s;31m"
B = "\033[%s;34m"
G = "\033[%s;32m"
W = "\033[%s;77m"
Y = "\033[%s;33m"
S = "\033[0;97m"
E = "\033[0m"
BOLD = "\033[1m"
