# -*- coding: utf-8 -*-

import data_ops_analysis_sdk.api.model_analysis.model_analysis_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.model_analysis = data_ops_analysis_sdk.api.model_analysis.model_analysis_client.ModelAnalysisClient(server_ip, server_port, service_name)
        
