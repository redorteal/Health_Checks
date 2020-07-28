#!/usr/bin/env python3
import shutil


def main():
    disk_stats = shutil.disk_usage("/")
    total = disk_stats[0]/10**9
    print("total GB: {:.2f}".format(total))
    free = disk_stats[2]/10**9
    free_space_percent = free/total*100
    if free_space_percent>60:
        print("Sufficient disk space available: {:.2f}GB".format(free))
    else:
        print("Running low on disk space")

main()
