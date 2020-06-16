# -*- coding: utf-8 -*-

import console_gateway_sdk.api.cmdb_service_ctrl.cmdb_service_ctrl_client

import console_gateway_sdk.api.notify_ctrl.notify_ctrl_client

import console_gateway_sdk.api.permission_ctrl.permission_ctrl_client

import console_gateway_sdk.api.user_service_ctrl.user_service_ctrl_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.cmdb_service_ctrl = console_gateway_sdk.api.cmdb_service_ctrl.cmdb_service_ctrl_client.CmdbServiceCtrlClient(server_ip, server_port, service_name)
        
        self.notify_ctrl = console_gateway_sdk.api.notify_ctrl.notify_ctrl_client.NotifyCtrlClient(server_ip, server_port, service_name)
        
        self.permission_ctrl = console_gateway_sdk.api.permission_ctrl.permission_ctrl_client.PermissionCtrlClient(server_ip, server_port, service_name)
        
        self.user_service_ctrl = console_gateway_sdk.api.user_service_ctrl.user_service_ctrl_client.UserServiceCtrlClient(server_ip, server_port, service_name)
        
