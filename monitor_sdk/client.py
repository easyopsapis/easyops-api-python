# -*- coding: utf-8 -*-

import api.collector.collector_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.collector = api.collector.collector_client.CollectorClient(server_ip, server_port, service_name)
        
