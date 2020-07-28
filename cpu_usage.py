#!/usr/bin/env python3

import os
import sys
import psutil

def cpu_usage():
    usage_percent = psutil.cpu_percent(interval = 1)
    print("{}% cpu is being used".format(usage_percent))
    #sys.exit(0)

def check_reboot():
    if os.path.exists("/var/run/reboot-required"):
        print("System reboot required.")
    else:
        print("everything ok.")

cpu_usage()
check_reboot()
