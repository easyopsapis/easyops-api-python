# -*- coding: utf-8 -*-

import influxdb_service_sdk.api.influxdb_proxy.influxdb_proxy_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.influxdb_proxy = influxdb_service_sdk.api.influxdb_proxy.influxdb_proxy_client.InfluxdbProxyClient(server_ip, server_port, service_name)
        
