# -*- coding: utf-8 -*-

import api.build.build_client

import api.org.org_client

import api.pipeline.pipeline_client

import api.project.project_client

import api.provider.provider_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.build = api.build.build_client.BuildClient(server_ip, server_port, service_name)
        
        self.org = api.org.org_client.OrgClient(server_ip, server_port, service_name)
        
        self.pipeline = api.pipeline.pipeline_client.PipelineClient(server_ip, server_port, service_name)
        
        self.project = api.project.project_client.ProjectClient(server_ip, server_port, service_name)
        
        self.provider = api.provider.provider_client.ProviderClient(server_ip, server_port, service_name)
        
