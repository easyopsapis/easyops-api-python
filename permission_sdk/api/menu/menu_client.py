# -*- coding: utf-8 -*-
import os
import sys


import permission_sdk.api.menu.get_user_forbidden_menu_pb2

import permission_sdk.utils.http_util
import google.protobuf.json_format


class MenuClient(object):
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

    
    def get_user_forbidden_menu(self, request, org, user, timeout=10):
        # type: (permission_sdk.api.menu.get_user_forbidden_menu_pb2.GetUserForbiddenMenuRequest, int, str, int) -> permission_sdk.api.menu.get_user_forbidden_menu_pb2.GetUserForbiddenMenuResponse
        """
        获取用户的不可访问菜单列表
        :param request: get_user_forbidden_menu请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: permission_sdk.api.menu.get_user_forbidden_menu_pb2.GetUserForbiddenMenuResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.permission.menu.GetUserForbiddenMenu"
        uri = "/api/v1/permission/menu/forbidden/{username}".format(
            username=request.username,
        )
        requestParam = request
        
        rsp_obj = permission_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.permission_sdk",
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
        rsp = permission_sdk.api.menu.get_user_forbidden_menu_pb2.GetUserForbiddenMenuResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
