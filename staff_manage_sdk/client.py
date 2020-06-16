# -*- coding: utf-8 -*-

import staff_manage_sdk.api.users.users_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.users = staff_manage_sdk.api.users.users_client.UsersClient(server_ip, server_port, service_name)
        
