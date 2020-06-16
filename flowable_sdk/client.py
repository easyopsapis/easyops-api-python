# -*- coding: utf-8 -*-

import flowable_sdk.api.deployment.deployment_client

import flowable_sdk.api.history.history_client

import flowable_sdk.api.process_definition.process_definition_client

import flowable_sdk.api.process_instance.process_instance_client

import flowable_sdk.api.task.task_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.deployment = flowable_sdk.api.deployment.deployment_client.DeploymentClient(server_ip, server_port, service_name)
        
        self.history = flowable_sdk.api.history.history_client.HistoryClient(server_ip, server_port, service_name)
        
        self.process_definition = flowable_sdk.api.process_definition.process_definition_client.ProcessDefinitionClient(server_ip, server_port, service_name)
        
        self.process_instance = flowable_sdk.api.process_instance.process_instance_client.ProcessInstanceClient(server_ip, server_port, service_name)
        
        self.task = flowable_sdk.api.task.task_client.TaskClient(server_ip, server_port, service_name)
        
