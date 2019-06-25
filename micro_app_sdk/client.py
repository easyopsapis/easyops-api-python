# -*- coding: utf-8 -*-

import api.micro_app.micro_app_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.micro_app = api.micro_app.micro_app_client.MicroAppClient(server_ip, server_port, service_name)
        
