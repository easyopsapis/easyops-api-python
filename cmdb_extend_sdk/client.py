# -*- coding: utf-8 -*-

import cmdb_extend_sdk.api.agent.agent_client

import cmdb_extend_sdk.api.agent_install_script.agent_install_script_client

import cmdb_extend_sdk.api.custom.custom_client

import cmdb_extend_sdk.api.email.email_client

import cmdb_extend_sdk.api.host_resolved.host_resolved_client

import cmdb_extend_sdk.api.instance.instance_client

import cmdb_extend_sdk.api.org.org_client

import cmdb_extend_sdk.api.pipeline.pipeline_client

import cmdb_extend_sdk.api.toolkit.toolkit_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.agent = cmdb_extend_sdk.api.agent.agent_client.AgentClient(server_ip, server_port, service_name)
        
        self.agent_install_script = cmdb_extend_sdk.api.agent_install_script.agent_install_script_client.AgentInstallScriptClient(server_ip, server_port, service_name)
        
        self.custom = cmdb_extend_sdk.api.custom.custom_client.CustomClient(server_ip, server_port, service_name)
        
        self.email = cmdb_extend_sdk.api.email.email_client.EmailClient(server_ip, server_port, service_name)
        
        self.host_resolved = cmdb_extend_sdk.api.host_resolved.host_resolved_client.HostResolvedClient(server_ip, server_port, service_name)
        
        self.instance = cmdb_extend_sdk.api.instance.instance_client.InstanceClient(server_ip, server_port, service_name)
        
        self.org = cmdb_extend_sdk.api.org.org_client.OrgClient(server_ip, server_port, service_name)
        
        self.pipeline = cmdb_extend_sdk.api.pipeline.pipeline_client.PipelineClient(server_ip, server_port, service_name)
        
        self.toolkit = cmdb_extend_sdk.api.toolkit.toolkit_client.ToolkitClient(server_ip, server_port, service_name)
        
