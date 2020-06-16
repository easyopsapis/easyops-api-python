# -*- coding: utf-8 -*-

import topboard_sdk.api.topboard.topboard_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.topboard = topboard_sdk.api.topboard.topboard_client.TopboardClient(server_ip, server_port, service_name)
        
