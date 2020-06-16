# -*- coding: utf-8 -*-

import user_service_sdk.api.apikey.apikey_client

import user_service_sdk.api.auth.auth_client

import user_service_sdk.api.gateway.gateway_client

import user_service_sdk.api.invitation_code.invitation_code_client

import user_service_sdk.api.ldap.ldap_client

import user_service_sdk.api.organization.organization_client

import user_service_sdk.api.user_admin.user_admin_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.apikey = user_service_sdk.api.apikey.apikey_client.ApikeyClient(server_ip, server_port, service_name)
        
        self.auth = user_service_sdk.api.auth.auth_client.AuthClient(server_ip, server_port, service_name)
        
        self.gateway = user_service_sdk.api.gateway.gateway_client.GatewayClient(server_ip, server_port, service_name)
        
        self.invitation_code = user_service_sdk.api.invitation_code.invitation_code_client.InvitationCodeClient(server_ip, server_port, service_name)
        
        self.ldap = user_service_sdk.api.ldap.ldap_client.LdapClient(server_ip, server_port, service_name)
        
        self.organization = user_service_sdk.api.organization.organization_client.OrganizationClient(server_ip, server_port, service_name)
        
        self.user_admin = user_service_sdk.api.user_admin.user_admin_client.UserAdminClient(server_ip, server_port, service_name)
        
