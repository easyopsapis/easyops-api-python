# -*- coding: utf-8 -*-

import app_store_sdk.api.micro_app.micro_app_client

import app_store_sdk.api.product_line.product_line_client

import app_store_sdk.api.solution.solution_client

import app_store_sdk.api.version.version_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.micro_app = app_store_sdk.api.micro_app.micro_app_client.MicroAppClient(server_ip, server_port, service_name)
        
        self.product_line = app_store_sdk.api.product_line.product_line_client.ProductLineClient(server_ip, server_port, service_name)
        
        self.solution = app_store_sdk.api.solution.solution_client.SolutionClient(server_ip, server_port, service_name)
        
        self.version = app_store_sdk.api.version.version_client.VersionClient(server_ip, server_port, service_name)
        
