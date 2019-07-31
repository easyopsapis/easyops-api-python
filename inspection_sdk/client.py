# -*- coding: utf-8 -*-

import api.collector.collector_client

import api.history.history_client

import api.info.info_client

import api.metric_group.metric_group_client

import api.task.task_client

import api.template.template_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.collector = api.collector.collector_client.CollectorClient(server_ip, server_port, service_name)
        
        self.history = api.history.history_client.HistoryClient(server_ip, server_port, service_name)
        
        self.info = api.info.info_client.InfoClient(server_ip, server_port, service_name)
        
        self.metric_group = api.metric_group.metric_group_client.MetricGroupClient(server_ip, server_port, service_name)
        
        self.task = api.task.task_client.TaskClient(server_ip, server_port, service_name)
        
        self.template = api.template.template_client.TemplateClient(server_ip, server_port, service_name)
        
