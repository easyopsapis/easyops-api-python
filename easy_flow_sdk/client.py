# -*- coding: utf-8 -*-

import easy_flow_sdk.api.deploy.deploy_client

import easy_flow_sdk.api.instance.instance_client

import easy_flow_sdk.api.strategy.strategy_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.deploy = easy_flow_sdk.api.deploy.deploy_client.DeployClient(server_ip, server_port, service_name)
        
        self.instance = easy_flow_sdk.api.instance.instance_client.InstanceClient(server_ip, server_port, service_name)
        
        self.strategy = easy_flow_sdk.api.strategy.strategy_client.StrategyClient(server_ip, server_port, service_name)
        
