#!/usr/bin/python
from scripts import cpu


class serviceModel:
    interval = 300
    retry = 3
    alert_amount = 5

    
class cpu(serviceModel):
    index_dic = {
        'idle'   : [20,10],
        'system' : [80,90],
        'iowait' : [50,70] 
        }
    graph_list = [ 'idle','ipwait' ]
    script = cpu.cpuMonitor
