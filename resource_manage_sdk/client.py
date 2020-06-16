# -*- coding: utf-8 -*-

import resource_manage_sdk.api.cmdb_approve.cmdb_approve_client

import resource_manage_sdk.api.collector_history.collector_history_client

import resource_manage_sdk.api.datafilter.datafilter_client

import resource_manage_sdk.api.service_manage.service_manage_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.cmdb_approve = resource_manage_sdk.api.cmdb_approve.cmdb_approve_client.CmdbApproveClient(server_ip, server_port, service_name)
        
        self.collector_history = resource_manage_sdk.api.collector_history.collector_history_client.CollectorHistoryClient(server_ip, server_port, service_name)
        
        self.datafilter = resource_manage_sdk.api.datafilter.datafilter_client.DatafilterClient(server_ip, server_port, service_name)
        
        self.service_manage = resource_manage_sdk.api.service_manage.service_manage_client.ServiceManageClient(server_ip, server_port, service_name)
        
