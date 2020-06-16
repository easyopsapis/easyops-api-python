# -*- coding: utf-8 -*-

import micro_app_sdk.api.installed_micro_app.installed_micro_app_client

import micro_app_sdk.api.micro_app_container.micro_app_container_client

import micro_app_sdk.api.object_micro_app.object_micro_app_client

import micro_app_sdk.api.report.report_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.installed_micro_app = micro_app_sdk.api.installed_micro_app.installed_micro_app_client.InstalledMicroAppClient(server_ip, server_port, service_name)
        
        self.micro_app_container = micro_app_sdk.api.micro_app_container.micro_app_container_client.MicroAppContainerClient(server_ip, server_port, service_name)
        
        self.object_micro_app = micro_app_sdk.api.object_micro_app.object_micro_app_client.ObjectMicroAppClient(server_ip, server_port, service_name)
        
        self.report = micro_app_sdk.api.report.report_client.ReportClient(server_ip, server_port, service_name)
        
