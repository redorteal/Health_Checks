#!/usr/bin/env python3

import sys
import re

log_file = sys.argv[1]
logs = open(log_file)

for log in logs:
    pattern = r"([\w\.]*)([\[\]\w :]) [ERROR]"
    if "ERROR" in log:
        result = re.search(pattern, log)
<<<<<<< HEAD
        pass
=======
        print("This service failed due to error: {}".format(result[1]))
        
>>>>>>> new_branch
