# -*- coding: utf-8 -*-

import next_builder_sdk.api.build.build_client

import next_builder_sdk.api.micro_app.micro_app_client

import next_builder_sdk.api.project.project_client

import next_builder_sdk.api.storyboard.storyboard_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.build = next_builder_sdk.api.build.build_client.BuildClient(server_ip, server_port, service_name)
        
        self.micro_app = next_builder_sdk.api.micro_app.micro_app_client.MicroAppClient(server_ip, server_port, service_name)
        
        self.project = next_builder_sdk.api.project.project_client.ProjectClient(server_ip, server_port, service_name)
        
        self.storyboard = next_builder_sdk.api.storyboard.storyboard_client.StoryboardClient(server_ip, server_port, service_name)
        
