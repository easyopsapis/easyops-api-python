# -*- coding: utf-8 -*-

import api.container.container_client

import api.view.view_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.container = api.container.container_client.ContainerClient(server_ip, server_port, service_name)
        
        self.view = api.view.view_client.ViewClient(server_ip, server_port, service_name)
        
