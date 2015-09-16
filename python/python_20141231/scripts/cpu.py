#!/usr/bin/python
# -*- coding:UTF-8 -*-

import commands
def cpuMonitor():

    cmd = "sar 1 1| grep 平均时间 | awk '{print $3,$5,$6,$8}'"

    status, result = commands.getstatusoutput(cmd)

    print result, status
