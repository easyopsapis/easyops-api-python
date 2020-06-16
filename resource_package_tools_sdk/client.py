# -*- coding: utf-8 -*-

import resource_package_tools_sdk.api.org.org_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.org = resource_package_tools_sdk.api.org.org_client.OrgClient(server_ip, server_port, service_name)
        
