# -*- coding: utf-8 -*-

import tuna_service_sdk.api.test_plan.test_plan_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.test_plan = tuna_service_sdk.api.test_plan.test_plan_client.TestPlanClient(server_ip, server_port, service_name)
        
