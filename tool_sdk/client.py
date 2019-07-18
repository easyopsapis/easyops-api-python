# -*- coding: utf-8 -*-

import api.basic.basic_client

import api.execute.execute_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.basic = api.basic.basic_client.BasicClient(server_ip, server_port, service_name)
        
        self.execute = api.execute.execute_client.ExecuteClient(server_ip, server_port, service_name)
        
