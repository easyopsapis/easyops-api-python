# -*- coding: utf-8 -*-

import ops_automation_sdk.api.job_task.job_task_client

import ops_automation_sdk.api.jobs.jobs_client

import ops_automation_sdk.api.menu.menu_client

import ops_automation_sdk.api.org.org_client

import ops_automation_sdk.api.service_event.service_event_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.job_task = ops_automation_sdk.api.job_task.job_task_client.JobTaskClient(server_ip, server_port, service_name)
        
        self.jobs = ops_automation_sdk.api.jobs.jobs_client.JobsClient(server_ip, server_port, service_name)
        
        self.menu = ops_automation_sdk.api.menu.menu_client.MenuClient(server_ip, server_port, service_name)
        
        self.org = ops_automation_sdk.api.org.org_client.OrgClient(server_ip, server_port, service_name)
        
        self.service_event = ops_automation_sdk.api.service_event.service_event_client.ServiceEventClient(server_ip, server_port, service_name)
        
