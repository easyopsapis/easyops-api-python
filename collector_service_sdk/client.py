# -*- coding: utf-8 -*-

import collector_service_sdk.api.collector_job.collector_job_client

import collector_service_sdk.api.config.config_client

import collector_service_sdk.api.jobs.jobs_client

import collector_service_sdk.api.key.key_client

import collector_service_sdk.api.metric.metric_client

import collector_service_sdk.api.organization.organization_client

import collector_service_sdk.api.template.template_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.collector_job = collector_service_sdk.api.collector_job.collector_job_client.CollectorJobClient(server_ip, server_port, service_name)
        
        self.config = collector_service_sdk.api.config.config_client.ConfigClient(server_ip, server_port, service_name)
        
        self.jobs = collector_service_sdk.api.jobs.jobs_client.JobsClient(server_ip, server_port, service_name)
        
        self.key = collector_service_sdk.api.key.key_client.KeyClient(server_ip, server_port, service_name)
        
        self.metric = collector_service_sdk.api.metric.metric_client.MetricClient(server_ip, server_port, service_name)
        
        self.organization = collector_service_sdk.api.organization.organization_client.OrganizationClient(server_ip, server_port, service_name)
        
        self.template = collector_service_sdk.api.template.template_client.TemplateClient(server_ip, server_port, service_name)
        
