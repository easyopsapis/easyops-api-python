# -*- coding: utf-8 -*-

import api.deploy.deploy_client

import api.instance.instance_client

import api.strategy.strategy_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.deploy = api.deploy.deploy_client.DeployClient(server_ip, server_port, service_name)
        
        self.instance = api.instance.instance_client.InstanceClient(server_ip, server_port, service_name)
        
        self.strategy = api.strategy.strategy_client.StrategyClient(server_ip, server_port, service_name)
        
