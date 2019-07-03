# -*- coding: utf-8 -*-

import api.job_export.job_export_client

import api.job_task.job_task_client

import api.jobs.jobs_client

import api.menu.menu_client

import api.org.org_client

import api.service_event.service_event_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.job_export = api.job_export.job_export_client.JobExportClient(server_ip, server_port, service_name)
        
        self.job_task = api.job_task.job_task_client.JobTaskClient(server_ip, server_port, service_name)
        
        self.jobs = api.jobs.jobs_client.JobsClient(server_ip, server_port, service_name)
        
        self.menu = api.menu.menu_client.MenuClient(server_ip, server_port, service_name)
        
        self.org = api.org.org_client.OrgClient(server_ip, server_port, service_name)
        
        self.service_event = api.service_event.service_event_client.ServiceEventClient(server_ip, server_port, service_name)
        
