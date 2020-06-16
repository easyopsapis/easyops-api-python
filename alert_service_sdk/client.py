# -*- coding: utf-8 -*-

import alert_service_sdk.api.alert_event.alert_event_client

import alert_service_sdk.api.alert_rule.alert_rule_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.alert_event = alert_service_sdk.api.alert_event.alert_event_client.AlertEventClient(server_ip, server_port, service_name)
        
        self.alert_rule = alert_service_sdk.api.alert_rule.alert_rule_client.AlertRuleClient(server_ip, server_port, service_name)
        
