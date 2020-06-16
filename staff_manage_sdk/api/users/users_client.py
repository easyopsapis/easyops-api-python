# -*- coding: utf-8 -*-
import os
import sys


import staff_manage_sdk.api.users.add_user_from_dingtalk_pb2

import google.protobuf.empty_pb2

import staff_manage_sdk.api.users.alert_user_password_to_ldap_pb2

import staff_manage_sdk.api.users.list_dimission_user_form_ldap_pb2

import staff_manage_sdk.api.users.sync_dimission_user_dingtalk_to_ldap_pb2

import staff_manage_sdk.api.users.sync_ldap_dimission_user_state_to_cmdb_pb2

import staff_manage_sdk.api.users.sync_user_dingtalk_to_ldap_pb2

import staff_manage_sdk.utils.http_util
import google.protobuf.json_format


class UsersClient(object):
    def __init__(self, server_ip="", server_port=0, service_name="", host=""):
        """
        初始化client
        :param server_ip: 指定sdk请求的server_ip，为空时走名字服务路由
        :param server_port: 指定sdk请求的server_port，与server_ip一起使用, 为空时走名字服务路由
        :param service_name: 指定sdk请求的service_name, 为空时按契约名称路由。如果server_ip和service_name同时设置，server_ip优先级更高
        :param host: 指定sdk请求服务的host名称, 如cmdb.easyops-only.com
        """
        if server_ip == "" and server_port != 0 or server_ip != "" and server_port == 0:
            raise Exception("server_ip和server_port必须同时指定")
        self._server_ip = server_ip
        self._server_port = server_port
        self._service_name = service_name
        self._host = host

    
    def add_user_from_ding_talk(self, request, org, user, timeout=10):
        # type: (staff_manage_sdk.api.users.add_user_from_dingtalk_pb2.AddUserFromDingTalkRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        从钉钉中添加用户
        :param request: add_user_from_ding_talk请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: google.protobuf.empty_pb2.Empty
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.staff_manage.users.AddUserFromDingTalk"
        uri = "/api/v1/users-add/dingtalk"
        
        requestParam = request
        
        rsp_obj = staff_manage_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.staff_manage_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=self._host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = google.protobuf.empty_pb2.Empty()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def alert_user_password_to_ldap(self, request, org, user, timeout=10):
        # type: (staff_manage_sdk.api.users.alert_user_password_to_ldap_pb2.AlertUserPasswordToLdapRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        修改Ldap用户密码
        :param request: alert_user_password_to_ldap请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: google.protobuf.empty_pb2.Empty
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.staff_manage.users.AlertUserPasswordToLdap"
        uri = "/api/v1/users-password/ldap"
        
        requestParam = request
        
        rsp_obj = staff_manage_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.staff_manage_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=self._host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = google.protobuf.empty_pb2.Empty()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_dimission_user_from_ldap(self, request, org, user, timeout=10):
        # type: (google.protobuf.empty_pb2.Empty, int, str, int) -> staff_manage_sdk.api.users.list_dimission_user_form_ldap_pb2.ListDimissionUserFromLdapResponse
        """
        从ldap获取禁用用户
        :param request: list_dimission_user_from_ldap请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: staff_manage_sdk.api.users.list_dimission_user_form_ldap_pb2.ListDimissionUserFromLdapResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.staff_manage.users.ListDimissionUserFromLdap"
        uri = "/api/v1/users-list/dimission-from-ldap"
        
        requestParam = request
        
        rsp_obj = staff_manage_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.staff_manage_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=self._host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = staff_manage_sdk.api.users.list_dimission_user_form_ldap_pb2.ListDimissionUserFromLdapResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def sync_dimission_user_ding_talk_to_ldap(self, request, org, user, timeout=10):
        # type: (google.protobuf.empty_pb2.Empty, int, str, int) -> staff_manage_sdk.api.users.sync_dimission_user_dingtalk_to_ldap_pb2.SyncDimissionUserDingTalkToLdapResponse
        """
        同步钉钉离职用户状态至ldap
        :param request: sync_dimission_user_ding_talk_to_ldap请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: staff_manage_sdk.api.users.sync_dimission_user_dingtalk_to_ldap_pb2.SyncDimissionUserDingTalkToLdapResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.staff_manage.users.SyncDimissionUserDingTalkToLdap"
        uri = "/api/v1/users-sync-dimission/dingtalk-to-ldap"
        
        requestParam = request
        
        rsp_obj = staff_manage_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.staff_manage_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=self._host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = staff_manage_sdk.api.users.sync_dimission_user_dingtalk_to_ldap_pb2.SyncDimissionUserDingTalkToLdapResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def sync_ldap_dimission_user_state_to_cmdb(self, request, org, user, timeout=10):
        # type: (staff_manage_sdk.api.users.sync_ldap_dimission_user_state_to_cmdb_pb2.SyncLdapDimissionUserStateToCmdbRequest, int, str, int) -> staff_manage_sdk.api.users.sync_ldap_dimission_user_state_to_cmdb_pb2.SyncLdapDimissionUserStateToCmdbResponse
        """
        同步ldap用户状态到cmdb
        :param request: sync_ldap_dimission_user_state_to_cmdb请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: staff_manage_sdk.api.users.sync_ldap_dimission_user_state_to_cmdb_pb2.SyncLdapDimissionUserStateToCmdbResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.staff_manage.users.SyncLdapDimissionUserStateToCmdb"
        uri = "/api/v1/users-sync-dimission/ldap-to-cmdb"
        
        requestParam = request
        
        rsp_obj = staff_manage_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.staff_manage_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=self._host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = staff_manage_sdk.api.users.sync_ldap_dimission_user_state_to_cmdb_pb2.SyncLdapDimissionUserStateToCmdbResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def sync_user_ding_talk_to_ldap(self, request, org, user, timeout=10):
        # type: (google.protobuf.empty_pb2.Empty, int, str, int) -> staff_manage_sdk.api.users.sync_user_dingtalk_to_ldap_pb2.SyncUserDingTalkToLdapResponse
        """
        同步钉钉用户至ldap
        :param request: sync_user_ding_talk_to_ldap请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: staff_manage_sdk.api.users.sync_user_dingtalk_to_ldap_pb2.SyncUserDingTalkToLdapResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.staff_manage.users.SyncUserDingTalkToLdap"
        uri = "/api/v1/users-sync/dingtalk-to-ldap"
        
        requestParam = request
        
        rsp_obj = staff_manage_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.staff_manage_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=self._host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = staff_manage_sdk.api.users.sync_user_dingtalk_to_ldap_pb2.SyncUserDingTalkToLdapResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
