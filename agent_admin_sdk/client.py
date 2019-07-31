# -*- coding: utf-8 -*-

import api.admin_task.admin_task_client

import api.agent.agent_client

import api.plugin.plugin_client

import api.plugin_version.plugin_version_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.admin_task = api.admin_task.admin_task_client.AdminTaskClient(server_ip, server_port, service_name)
        
        self.agent = api.agent.agent_client.AgentClient(server_ip, server_port, service_name)
        
        self.plugin = api.plugin.plugin_client.PluginClient(server_ip, server_port, service_name)
        
        self.plugin_version = api.plugin_version.plugin_version_client.PluginVersionClient(server_ip, server_port, service_name)
        
