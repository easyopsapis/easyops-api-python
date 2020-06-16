# -*- coding: utf-8 -*-

import ucpro_sdk.api.desktop.desktop_client

import ucpro_sdk.api.org.org_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.desktop = ucpro_sdk.api.desktop.desktop_client.DesktopClient(server_ip, server_port, service_name)
        
        self.org = ucpro_sdk.api.org.org_client.OrgClient(server_ip, server_port, service_name)
        
