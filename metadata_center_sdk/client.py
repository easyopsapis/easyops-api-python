# -*- coding: utf-8 -*-

import metadata_center_sdk.api.stream.stream_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.stream = metadata_center_sdk.api.stream.stream_client.StreamClient(server_ip, server_port, service_name)
        
