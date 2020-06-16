# -*- coding: utf-8 -*-

import dc_console_sdk.api.org.org_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.org = dc_console_sdk.api.org.org_client.OrgClient(server_ip, server_port, service_name)
        
