# -*- coding: utf-8 -*-

import api.oplog.oplog_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.oplog = api.oplog.oplog_client.OplogClient(server_ip, server_port, service_name)
        
