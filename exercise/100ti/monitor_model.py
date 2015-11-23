#!/usr/bin/python

from services import *

class defaultModel:
    hostname = None
    ip_address = None
    customized_services = None
    monitor_service = [cpu,'memory','load','network']
    graph_list = ['cpu','memory']


class host1(defaultModel):
    hostname = 'localhost'
    ip_address = '192.168.1.136'
    customized_services = ['mysql']
    

class host2(defaultModel):
    hostname = 'ezreal'
    ip_address = '192.168.1.6'
    customized_services = [cpu,'Nginx']
    customized_services[0].interval = 50

class host3(defaultModel):
    hostname = 'win7'
    ip_address = '192.168.1.229'
    #customized_services = ['MongoDB','Nginx']


enabled_monitors = (
        host1(),
        host2(),
        host3()
        )
for h in enabled_monitors:
    print h.hostname, h.ip_address, h.customized_services
    c = h.monitor_service[0]
    print '\033[43;1m %s \033[0m' % c
    print c.interval
    print c.index_dic
