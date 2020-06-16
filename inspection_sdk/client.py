# -*- coding: utf-8 -*-

import inspection_sdk.api.collector.collector_client

import inspection_sdk.api.history.history_client

import inspection_sdk.api.info.info_client

import inspection_sdk.api.metric_group.metric_group_client

import inspection_sdk.api.task.task_client

import inspection_sdk.api.template.template_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.collector = inspection_sdk.api.collector.collector_client.CollectorClient(server_ip, server_port, service_name)
        
        self.history = inspection_sdk.api.history.history_client.HistoryClient(server_ip, server_port, service_name)
        
        self.info = inspection_sdk.api.info.info_client.InfoClient(server_ip, server_port, service_name)
        
        self.metric_group = inspection_sdk.api.metric_group.metric_group_client.MetricGroupClient(server_ip, server_port, service_name)
        
        self.task = inspection_sdk.api.task.task_client.TaskClient(server_ip, server_port, service_name)
        
        self.template = inspection_sdk.api.template.template_client.TemplateClient(server_ip, server_port, service_name)
        
