# -*- coding: utf-8 -*-

import api.desktop.desktop_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.desktop = api.desktop.desktop_client.DesktopClient(server_ip, server_port, service_name)
        
