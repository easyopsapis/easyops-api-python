# -*- coding: utf-8 -*-

import easy_command_sdk.api.task.task_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.task = easy_command_sdk.api.task.task_client.TaskClient(server_ip, server_port, service_name)
        
