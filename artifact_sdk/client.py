# -*- coding: utf-8 -*-

import artifact_sdk.api.pkg.pkg_client

import artifact_sdk.api.version.version_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.pkg = artifact_sdk.api.pkg.pkg_client.PkgClient(server_ip, server_port, service_name)
        
        self.version = artifact_sdk.api.version.version_client.VersionClient(server_ip, server_port, service_name)
        
