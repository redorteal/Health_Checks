#!/usr/bin/env python3

import re

with open("/var/lib/update-notifier/updates-available",'r') as f:
    for line in f:
        if "installed" in line:
            pattern = r"^(\d*)""
            result = re.search(pattern, line)
            if result[1] != 0:
                print("{} Updates pending to be installed.".formate(result[1]))
            else:
                print("Good to go. System is up to date.")
f.close()
