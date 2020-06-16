# -*- coding: utf-8 -*-

import flow_sdk.api.basic.basic_client

import flow_sdk.api.execute.execute_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.basic = flow_sdk.api.basic.basic_client.BasicClient(server_ip, server_port, service_name)
        
        self.execute = flow_sdk.api.execute.execute_client.ExecuteClient(server_ip, server_port, service_name)
        
