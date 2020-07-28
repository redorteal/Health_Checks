#!/usr/bin/env python3

import sys
import re

log_file = sys.argv[1]

logs = open(log_file)

for log in logs:
    pattern = ""
