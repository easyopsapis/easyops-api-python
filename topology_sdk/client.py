# -*- coding: utf-8 -*-

import topology_sdk.api.container.container_client

import topology_sdk.api.org.org_client

import topology_sdk.api.topo_view.topo_view_client

import topology_sdk.api.view.view_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.container = topology_sdk.api.container.container_client.ContainerClient(server_ip, server_port, service_name)
        
        self.org = topology_sdk.api.org.org_client.OrgClient(server_ip, server_port, service_name)
        
        self.topo_view = topology_sdk.api.topo_view.topo_view_client.TopoViewClient(server_ip, server_port, service_name)
        
        self.view = topology_sdk.api.view.view_client.ViewClient(server_ip, server_port, service_name)
        
