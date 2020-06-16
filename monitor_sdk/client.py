# -*- coding: utf-8 -*-

import monitor_sdk.api.alert.alert_client

import monitor_sdk.api.alert_downtime.alert_downtime_client

import monitor_sdk.api.alert_rule.alert_rule_client

import monitor_sdk.api.app_health.app_health_client

import monitor_sdk.api.auto_recovery.auto_recovery_client

import monitor_sdk.api.collector.collector_client

import monitor_sdk.api.data_name.data_name_client

import monitor_sdk.api.influxdb.influxdb_client

import monitor_sdk.api.log_search.log_search_client

import monitor_sdk.api.translate.translate_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.alert = monitor_sdk.api.alert.alert_client.AlertClient(server_ip, server_port, service_name)
        
        self.alert_downtime = monitor_sdk.api.alert_downtime.alert_downtime_client.AlertDowntimeClient(server_ip, server_port, service_name)
        
        self.alert_rule = monitor_sdk.api.alert_rule.alert_rule_client.AlertRuleClient(server_ip, server_port, service_name)
        
        self.app_health = monitor_sdk.api.app_health.app_health_client.AppHealthClient(server_ip, server_port, service_name)
        
        self.auto_recovery = monitor_sdk.api.auto_recovery.auto_recovery_client.AutoRecoveryClient(server_ip, server_port, service_name)
        
        self.collector = monitor_sdk.api.collector.collector_client.CollectorClient(server_ip, server_port, service_name)
        
        self.data_name = monitor_sdk.api.data_name.data_name_client.DataNameClient(server_ip, server_port, service_name)
        
        self.influxdb = monitor_sdk.api.influxdb.influxdb_client.InfluxdbClient(server_ip, server_port, service_name)
        
        self.log_search = monitor_sdk.api.log_search.log_search_client.LogSearchClient(server_ip, server_port, service_name)
        
        self.translate = monitor_sdk.api.translate.translate_client.TranslateClient(server_ip, server_port, service_name)
        
