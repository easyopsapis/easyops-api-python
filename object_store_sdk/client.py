# -*- coding: utf-8 -*-

import object_store_sdk.api.object_store.object_store_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.object_store = object_store_sdk.api.object_store.object_store_client.ObjectStoreClient(server_ip, server_port, service_name)
        
