# -*- coding: utf-8 -*-

import tool_sdk.api.basic.basic_client

import tool_sdk.api.execute.execute_client

import tool_sdk.api.migrate.migrate_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.basic = tool_sdk.api.basic.basic_client.BasicClient(server_ip, server_port, service_name)
        
        self.execute = tool_sdk.api.execute.execute_client.ExecuteClient(server_ip, server_port, service_name)
        
        self.migrate = tool_sdk.api.migrate.migrate_client.MigrateClient(server_ip, server_port, service_name)
        
