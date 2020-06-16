# -*- coding: utf-8 -*-

import patch_manager_sdk.api.org.org_client

import patch_manager_sdk.api.patch.patch_client

import patch_manager_sdk.api.patch_task.patch_task_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.org = patch_manager_sdk.api.org.org_client.OrgClient(server_ip, server_port, service_name)
        
        self.patch = patch_manager_sdk.api.patch.patch_client.PatchClient(server_ip, server_port, service_name)
        
        self.patch_task = patch_manager_sdk.api.patch_task.patch_task_client.PatchTaskClient(server_ip, server_port, service_name)
        
