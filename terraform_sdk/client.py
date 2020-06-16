# -*- coding: utf-8 -*-

import terraform_sdk.api.backend.backend_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.backend = terraform_sdk.api.backend.backend_client.BackendClient(server_ip, server_port, service_name)
        
