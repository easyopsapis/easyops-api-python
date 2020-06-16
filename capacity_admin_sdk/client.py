# -*- coding: utf-8 -*-

import capacity_admin_sdk.api.portrait.portrait_client

import capacity_admin_sdk.api.task.task_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.portrait = capacity_admin_sdk.api.portrait.portrait_client.PortraitClient(server_ip, server_port, service_name)
        
        self.task = capacity_admin_sdk.api.task.task_client.TaskClient(server_ip, server_port, service_name)
        
