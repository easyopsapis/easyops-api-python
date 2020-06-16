# -*- coding: utf-8 -*-

import resource_monitor_sdk.api.health_assessment_result.health_assessment_result_client

import resource_monitor_sdk.api.health_assessment_rule.health_assessment_rule_client

import resource_monitor_sdk.api.related_resource.related_resource_client

import resource_monitor_sdk.api.resource_monitor_config.resource_monitor_config_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.health_assessment_result = resource_monitor_sdk.api.health_assessment_result.health_assessment_result_client.HealthAssessmentResultClient(server_ip, server_port, service_name)
        
        self.health_assessment_rule = resource_monitor_sdk.api.health_assessment_rule.health_assessment_rule_client.HealthAssessmentRuleClient(server_ip, server_port, service_name)
        
        self.related_resource = resource_monitor_sdk.api.related_resource.related_resource_client.RelatedResourceClient(server_ip, server_port, service_name)
        
        self.resource_monitor_config = resource_monitor_sdk.api.resource_monitor_config.resource_monitor_config_client.ResourceMonitorConfigClient(server_ip, server_port, service_name)
        
