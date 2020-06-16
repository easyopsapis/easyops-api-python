# -*- coding: utf-8 -*-

import agent_admin_sdk.api.admin_task.admin_task_client

import agent_admin_sdk.api.agent.agent_client

import agent_admin_sdk.api.org.org_client

import agent_admin_sdk.api.org_init.org_init_client

import agent_admin_sdk.api.plugin.plugin_client

import agent_admin_sdk.api.plugin_version.plugin_version_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.admin_task = agent_admin_sdk.api.admin_task.admin_task_client.AdminTaskClient(server_ip, server_port, service_name)
        
        self.agent = agent_admin_sdk.api.agent.agent_client.AgentClient(server_ip, server_port, service_name)
        
        self.org = agent_admin_sdk.api.org.org_client.OrgClient(server_ip, server_port, service_name)
        
        self.org_init = agent_admin_sdk.api.org_init.org_init_client.OrgInitClient(server_ip, server_port, service_name)
        
        self.plugin = agent_admin_sdk.api.plugin.plugin_client.PluginClient(server_ip, server_port, service_name)
        
        self.plugin_version = agent_admin_sdk.api.plugin_version.plugin_version_client.PluginVersionClient(server_ip, server_port, service_name)
        
