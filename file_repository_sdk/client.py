# -*- coding: utf-8 -*-

import file_repository_sdk.api.archive.archive_client

import file_repository_sdk.api.workspace.workspace_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.archive = file_repository_sdk.api.archive.archive_client.ArchiveClient(server_ip, server_port, service_name)
        
        self.workspace = file_repository_sdk.api.workspace.workspace_client.WorkspaceClient(server_ip, server_port, service_name)
        
