# -*- coding: utf-8 -*-

import cmdb_sdk.api.business_instance.business_instance_client

import cmdb_sdk.api.cmdb_object.cmdb_object_client

import cmdb_sdk.api.history.history_client

import cmdb_sdk.api.index.index_client

import cmdb_sdk.api.initialization.initialization_client

import cmdb_sdk.api.instance.instance_client

import cmdb_sdk.api.instance_archive.instance_archive_client

import cmdb_sdk.api.instance_graph.instance_graph_client

import cmdb_sdk.api.instance_path_search.instance_path_search_client

import cmdb_sdk.api.instance_relation.instance_relation_client

import cmdb_sdk.api.instance_tree.instance_tree_client

import cmdb_sdk.api.object_attribute.object_attribute_client

import cmdb_sdk.api.object_relation.object_relation_client

import cmdb_sdk.api.terraform.terraform_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.business_instance = cmdb_sdk.api.business_instance.business_instance_client.BusinessInstanceClient(server_ip, server_port, service_name)
        
        self.cmdb_object = cmdb_sdk.api.cmdb_object.cmdb_object_client.CmdbObjectClient(server_ip, server_port, service_name)
        
        self.history = cmdb_sdk.api.history.history_client.HistoryClient(server_ip, server_port, service_name)
        
        self.index = cmdb_sdk.api.index.index_client.IndexClient(server_ip, server_port, service_name)
        
        self.initialization = cmdb_sdk.api.initialization.initialization_client.InitializationClient(server_ip, server_port, service_name)
        
        self.instance = cmdb_sdk.api.instance.instance_client.InstanceClient(server_ip, server_port, service_name)
        
        self.instance_archive = cmdb_sdk.api.instance_archive.instance_archive_client.InstanceArchiveClient(server_ip, server_port, service_name)
        
        self.instance_graph = cmdb_sdk.api.instance_graph.instance_graph_client.InstanceGraphClient(server_ip, server_port, service_name)
        
        self.instance_path_search = cmdb_sdk.api.instance_path_search.instance_path_search_client.InstancePathSearchClient(server_ip, server_port, service_name)
        
        self.instance_relation = cmdb_sdk.api.instance_relation.instance_relation_client.InstanceRelationClient(server_ip, server_port, service_name)
        
        self.instance_tree = cmdb_sdk.api.instance_tree.instance_tree_client.InstanceTreeClient(server_ip, server_port, service_name)
        
        self.object_attribute = cmdb_sdk.api.object_attribute.object_attribute_client.ObjectAttributeClient(server_ip, server_port, service_name)
        
        self.object_relation = cmdb_sdk.api.object_relation.object_relation_client.ObjectRelationClient(server_ip, server_port, service_name)
        
        self.terraform = cmdb_sdk.api.terraform.terraform_client.TerraformClient(server_ip, server_port, service_name)
        
