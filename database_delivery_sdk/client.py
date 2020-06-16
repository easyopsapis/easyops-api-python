# -*- coding: utf-8 -*-

import database_delivery_sdk.api.dbclient.dbclient_client

import database_delivery_sdk.api.dbinstance.dbinstance_client

import database_delivery_sdk.api.dbservice.dbservice_client

import database_delivery_sdk.api.dbtask.dbtask_client

import database_delivery_sdk.api.sqlpkg_versions.sqlpkg_versions_client

import database_delivery_sdk.api.sqlpkgs.sqlpkgs_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.dbclient = database_delivery_sdk.api.dbclient.dbclient_client.DbclientClient(server_ip, server_port, service_name)
        
        self.dbinstance = database_delivery_sdk.api.dbinstance.dbinstance_client.DbinstanceClient(server_ip, server_port, service_name)
        
        self.dbservice = database_delivery_sdk.api.dbservice.dbservice_client.DbserviceClient(server_ip, server_port, service_name)
        
        self.dbtask = database_delivery_sdk.api.dbtask.dbtask_client.DbtaskClient(server_ip, server_port, service_name)
        
        self.sqlpkg_versions = database_delivery_sdk.api.sqlpkg_versions.sqlpkg_versions_client.SqlpkgVersionsClient(server_ip, server_port, service_name)
        
        self.sqlpkgs = database_delivery_sdk.api.sqlpkgs.sqlpkgs_client.SqlpkgsClient(server_ip, server_port, service_name)
        
