# -*- coding: utf-8 -*-

import api.permission.permission_client

import api.role.role_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.permission = api.permission.permission_client.PermissionClient(server_ip, server_port, service_name)
        
        self.role = api.role.role_client.RoleClient(server_ip, server_port, service_name)
        
