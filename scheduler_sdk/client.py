# -*- coding: utf-8 -*-

import scheduler_sdk.api.task.task_client

import scheduler_sdk.api.task_history.task_history_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.task = scheduler_sdk.api.task.task_client.TaskClient(server_ip, server_port, service_name)
        
        self.task_history = scheduler_sdk.api.task_history.task_history_client.TaskHistoryClient(server_ip, server_port, service_name)
        
