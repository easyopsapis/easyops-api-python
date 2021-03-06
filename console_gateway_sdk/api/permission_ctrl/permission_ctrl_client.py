# -*- coding: utf-8 -*-
import os
import sys


import console_gateway_sdk.api.permission_ctrl.create_role_pb2

import console_gateway_sdk.api.permission_ctrl.get_permission_list_pb2

import console_gateway_sdk.api.permission_ctrl.get_role_detail_pb2

import console_gateway_sdk.utils.http_util
import google.protobuf.json_format


class PermissionCtrlClient(object):
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

    
    def create_role(self, request, org, user, timeout=10):
        # type: (console_gateway_sdk.api.permission_ctrl.create_role_pb2.CreateRoleRequest, int, str, int) -> console_gateway_sdk.api.permission_ctrl.create_role_pb2.CreateRoleResponse
        """
        新增角色权限配置
        :param request: create_role请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: console_gateway_sdk.api.permission_ctrl.create_role_pb2.CreateRoleResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.console_gateway.permission_ctrl.CreateRole"
        uri = "/api/role-add"
        
        requestParam = request
        
        rsp_obj = console_gateway_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.console_gateway_sdk",
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
        rsp = console_gateway_sdk.api.permission_ctrl.create_role_pb2.CreateRoleResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_permission_list(self, request, org, user, timeout=10):
        # type: (console_gateway_sdk.api.permission_ctrl.get_permission_list_pb2.GetPermissionListRequest, int, str, int) -> console_gateway_sdk.api.permission_ctrl.get_permission_list_pb2.GetPermissionListResponse
        """
        获取权限点列表
        :param request: get_permission_list请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: console_gateway_sdk.api.permission_ctrl.get_permission_list_pb2.GetPermissionListResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.console_gateway.permission_ctrl.GetPermissionList"
        uri = "/api/permission-list"
        
        requestParam = request
        
        rsp_obj = console_gateway_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.console_gateway_sdk",
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
        rsp = console_gateway_sdk.api.permission_ctrl.get_permission_list_pb2.GetPermissionListResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_role_detail(self, request, org, user, timeout=10):
        # type: (console_gateway_sdk.api.permission_ctrl.get_role_detail_pb2.GetRoleDetailRequest, int, str, int) -> console_gateway_sdk.api.permission_ctrl.get_role_detail_pb2.GetRoleDetailResponse
        """
        获取角色权限配置详情
        :param request: get_role_detail请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: console_gateway_sdk.api.permission_ctrl.get_role_detail_pb2.GetRoleDetailResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.console_gateway.permission_ctrl.GetRoleDetail"
        uri = "/api/role-detail/{id}".format(
            id=request.id,
        )
        requestParam = request
        
        rsp_obj = console_gateway_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.console_gateway_sdk",
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
        rsp = console_gateway_sdk.api.permission_ctrl.get_role_detail_pb2.GetRoleDetailResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
