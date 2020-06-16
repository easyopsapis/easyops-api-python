# -*- coding: utf-8 -*-

import idcmanager_sdk.api.excel.excel_client

import idcmanager_sdk.api.idc.idc_client

import idcmanager_sdk.api.idcrack.idcrack_client

import idcmanager_sdk.api.org.org_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.excel = idcmanager_sdk.api.excel.excel_client.ExcelClient(server_ip, server_port, service_name)
        
        self.idc = idcmanager_sdk.api.idc.idc_client.IdcClient(server_ip, server_port, service_name)
        
        self.idcrack = idcmanager_sdk.api.idcrack.idcrack_client.IdcrackClient(server_ip, server_port, service_name)
        
        self.org = idcmanager_sdk.api.org.org_client.OrgClient(server_ip, server_port, service_name)
        
