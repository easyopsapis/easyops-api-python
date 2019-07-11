# -*- coding: utf-8 -*-

import api.pipeline.pipeline_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.pipeline = api.pipeline.pipeline_client.PipelineClient(server_ip, server_port, service_name)
        
