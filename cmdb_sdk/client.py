# -*- coding: utf-8 -*-

import api.business_instance.business_instance_client

import api.cmdb_object.cmdb_object_client

import api.initialization.initialization_client

import api.instance.instance_client

import api.instance_graph.instance_graph_client

import api.instance_relation.instance_relation_client

import api.instance_tree.instance_tree_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.business_instance = api.business_instance.business_instance_client.BusinessInstanceClient(server_ip, server_port, service_name)
        
        self.cmdb_object = api.cmdb_object.cmdb_object_client.CmdbObjectClient(server_ip, server_port, service_name)
        
        self.initialization = api.initialization.initialization_client.InitializationClient(server_ip, server_port, service_name)
        
        self.instance = api.instance.instance_client.InstanceClient(server_ip, server_port, service_name)
        
        self.instance_graph = api.instance_graph.instance_graph_client.InstanceGraphClient(server_ip, server_port, service_name)
        
        self.instance_relation = api.instance_relation.instance_relation_client.InstanceRelationClient(server_ip, server_port, service_name)
        
        self.instance_tree = api.instance_tree.instance_tree_client.InstanceTreeClient(server_ip, server_port, service_name)
        
