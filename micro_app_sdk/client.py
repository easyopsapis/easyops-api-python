# -*- coding: utf-8 -*-

import api.installed_micro_app.installed_micro_app_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.installed_micro_app = api.installed_micro_app.installed_micro_app_client.InstalledMicroAppClient(server_ip, server_port, service_name)
        
