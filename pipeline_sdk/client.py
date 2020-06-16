# -*- coding: utf-8 -*-

import pipeline_sdk.api.build.build_client

import pipeline_sdk.api.org.org_client

import pipeline_sdk.api.pipeline.pipeline_client

import pipeline_sdk.api.project.project_client

import pipeline_sdk.api.provider.provider_client

import pipeline_sdk.api.template.template_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.build = pipeline_sdk.api.build.build_client.BuildClient(server_ip, server_port, service_name)
        
        self.org = pipeline_sdk.api.org.org_client.OrgClient(server_ip, server_port, service_name)
        
        self.pipeline = pipeline_sdk.api.pipeline.pipeline_client.PipelineClient(server_ip, server_port, service_name)
        
        self.project = pipeline_sdk.api.project.project_client.ProjectClient(server_ip, server_port, service_name)
        
        self.provider = pipeline_sdk.api.provider.provider_client.ProviderClient(server_ip, server_port, service_name)
        
        self.template = pipeline_sdk.api.template.template_client.TemplateClient(server_ip, server_port, service_name)
        
