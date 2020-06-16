# -*- coding: utf-8 -*-

import msgsender_sdk.api.custom_sender.custom_sender_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.custom_sender = msgsender_sdk.api.custom_sender.custom_sender_client.CustomSenderClient(server_ip, server_port, service_name)
        
