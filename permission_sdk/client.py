# -*- coding: utf-8 -*-

import permission_sdk.api.menu.menu_client

import permission_sdk.api.permission.permission_client

import permission_sdk.api.role.role_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.menu = permission_sdk.api.menu.menu_client.MenuClient(server_ip, server_port, service_name)
        
        self.permission = permission_sdk.api.permission.permission_client.PermissionClient(server_ip, server_port, service_name)
        
        self.role = permission_sdk.api.role.role_client.RoleClient(server_ip, server_port, service_name)
        
