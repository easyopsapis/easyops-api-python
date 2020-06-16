# -*- coding: utf-8 -*-

import api_gateway_sdk.api.bootstrap.bootstrap_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.bootstrap = api_gateway_sdk.api.bootstrap.bootstrap_client.BootstrapClient(server_ip, server_port, service_name)
        
