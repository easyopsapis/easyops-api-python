# -*- coding: utf-8 -*-

import api.cmdb_approve.cmdb_approve_client

import api.service_manage.service_manage_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.cmdb_approve = api.cmdb_approve.cmdb_approve_client.CmdbApproveClient(server_ip, server_port, service_name)
        
        self.service_manage = api.service_manage.service_manage_client.ServiceManageClient(server_ip, server_port, service_name)
        
