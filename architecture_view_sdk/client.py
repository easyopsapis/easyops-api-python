# -*- coding: utf-8 -*-

import architecture_view_sdk.api.business.business_client

import architecture_view_sdk.api.org.org_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.business = architecture_view_sdk.api.business.business_client.BusinessClient(server_ip, server_port, service_name)
        
        self.org = architecture_view_sdk.api.org.org_client.OrgClient(server_ip, server_port, service_name)
        
