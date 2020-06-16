# -*- coding: utf-8 -*-

import translate_sdk.api.data_name.data_name_client

import translate_sdk.api.translate_rule.translate_rule_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.data_name = translate_sdk.api.data_name.data_name_client.DataNameClient(server_ip, server_port, service_name)
        
        self.translate_rule = translate_sdk.api.translate_rule.translate_rule_client.TranslateRuleClient(server_ip, server_port, service_name)
        
