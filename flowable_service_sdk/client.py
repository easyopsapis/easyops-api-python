# -*- coding: utf-8 -*-

import flowable_service_sdk.api.auth.auth_client

import flowable_service_sdk.api.form_schema.form_schema_client

import flowable_service_sdk.api.form_schema_version.form_schema_version_client

import flowable_service_sdk.api.process_definition.process_definition_client

import flowable_service_sdk.api.process_definition_version.process_definition_version_client

import flowable_service_sdk.api.process_instance.process_instance_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.auth = flowable_service_sdk.api.auth.auth_client.AuthClient(server_ip, server_port, service_name)
        
        self.form_schema = flowable_service_sdk.api.form_schema.form_schema_client.FormSchemaClient(server_ip, server_port, service_name)
        
        self.form_schema_version = flowable_service_sdk.api.form_schema_version.form_schema_version_client.FormSchemaVersionClient(server_ip, server_port, service_name)
        
        self.process_definition = flowable_service_sdk.api.process_definition.process_definition_client.ProcessDefinitionClient(server_ip, server_port, service_name)
        
        self.process_definition_version = flowable_service_sdk.api.process_definition_version.process_definition_version_client.ProcessDefinitionVersionClient(server_ip, server_port, service_name)
        
        self.process_instance = flowable_service_sdk.api.process_instance.process_instance_client.ProcessInstanceClient(server_ip, server_port, service_name)
        
