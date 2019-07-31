# -*- coding: utf-8 -*-

import api.dbclient.dbclient_client

import api.dbinstance.dbinstance_client

import api.dbservice.dbservice_client

import api.dbtask.dbtask_client

import api.sqlpkg_versions.sqlpkg_versions_client

import api.sqlpkgs.sqlpkgs_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.dbclient = api.dbclient.dbclient_client.DbclientClient(server_ip, server_port, service_name)
        
        self.dbinstance = api.dbinstance.dbinstance_client.DbinstanceClient(server_ip, server_port, service_name)
        
        self.dbservice = api.dbservice.dbservice_client.DbserviceClient(server_ip, server_port, service_name)
        
        self.dbtask = api.dbtask.dbtask_client.DbtaskClient(server_ip, server_port, service_name)
        
        self.sqlpkg_versions = api.sqlpkg_versions.sqlpkg_versions_client.SqlpkgVersionsClient(server_ip, server_port, service_name)
        
        self.sqlpkgs = api.sqlpkgs.sqlpkgs_client.SqlpkgsClient(server_ip, server_port, service_name)
        
