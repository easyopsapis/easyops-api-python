# -*- coding: utf-8 -*-

import api.user_admin.user_admin_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.user_admin = api.user_admin.user_admin_client.UserAdminClient(server_ip, server_port, service_name)
        
