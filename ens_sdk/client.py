# -*- coding: utf-8 -*-

import ens_sdk.api.legacy.legacy_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.legacy = ens_sdk.api.legacy.legacy_client.LegacyClient(server_ip, server_port, service_name)
        
