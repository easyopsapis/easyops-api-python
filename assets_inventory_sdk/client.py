# -*- coding: utf-8 -*-

import assets_inventory_sdk.api.excel.excel_client

import assets_inventory_sdk.api.idc.idc_client

import assets_inventory_sdk.api.idcrack.idcrack_client

import assets_inventory_sdk.api.inventory.inventory_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.excel = assets_inventory_sdk.api.excel.excel_client.ExcelClient(server_ip, server_port, service_name)
        
        self.idc = assets_inventory_sdk.api.idc.idc_client.IdcClient(server_ip, server_port, service_name)
        
        self.idcrack = assets_inventory_sdk.api.idcrack.idcrack_client.IdcrackClient(server_ip, server_port, service_name)
        
        self.inventory = assets_inventory_sdk.api.inventory.inventory_client.InventoryClient(server_ip, server_port, service_name)
        
