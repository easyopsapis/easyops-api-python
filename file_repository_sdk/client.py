# -*- coding: utf-8 -*-

import api.archive.archive_client

import api.workspace.workspace_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.archive = api.archive.archive_client.ArchiveClient(server_ip, server_port, service_name)
        
        self.workspace = api.workspace.workspace_client.WorkspaceClient(server_ip, server_port, service_name)
        
