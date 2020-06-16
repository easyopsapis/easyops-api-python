# -*- coding: utf-8 -*-

import anxin_service_sdk.api.permission.permission_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.permission = anxin_service_sdk.api.permission.permission_client.PermissionClient(server_ip, server_port, service_name)
        
