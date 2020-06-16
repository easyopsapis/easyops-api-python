# -*- coding: utf-8 -*-

import collector_center_sdk.api.clazz.clazz_client

import collector_center_sdk.api.collection_config.collection_config_client

import collector_center_sdk.api.configuration.configuration_client

import collector_center_sdk.api.job.job_client

import collector_center_sdk.api.template.template_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.clazz = collector_center_sdk.api.clazz.clazz_client.ClazzClient(server_ip, server_port, service_name)
        
        self.collection_config = collector_center_sdk.api.collection_config.collection_config_client.CollectionConfigClient(server_ip, server_port, service_name)
        
        self.configuration = collector_center_sdk.api.configuration.configuration_client.ConfigurationClient(server_ip, server_port, service_name)
        
        self.job = collector_center_sdk.api.job.job_client.JobClient(server_ip, server_port, service_name)
        
        self.template = collector_center_sdk.api.template.template_client.TemplateClient(server_ip, server_port, service_name)
        
