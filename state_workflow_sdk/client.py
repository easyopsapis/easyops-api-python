# -*- coding: utf-8 -*-

import state_workflow_sdk.api.state_workflow.state_workflow_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.state_workflow = state_workflow_sdk.api.state_workflow.state_workflow_client.StateWorkflowClient(server_ip, server_port, service_name)
        
