# -*- coding: utf-8 -*-
import os
import sys


import cmdb_sdk.api.business_instance.business_tree_list_pb2

import cmdb_sdk.api.business_instance.search_app_in_system_pb2

import cmdb_sdk.api.business_instance.search_subsystem_pb2

import cmdb_sdk.utils.http_util
import google.protobuf.json_format


class BusinessInstanceClient(object):
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

    
    def get_business_tree_list(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.business_instance.business_tree_list_pb2.GetBusinessTreeListRequest, int, str, int) -> cmdb_sdk.api.business_instance.business_tree_list_pb2.GetBusinessTreeListResponse
        """
        批量获取业务业务树全路径
        :param request: get_business_tree_list请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.business_instance.business_tree_list_pb2.GetBusinessTreeListResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.business_instance.GetBusinessTreeList"
        uri = "/system/business_tree/list"
        
        requestParam = request
        
        rsp_obj = cmdb_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.cmdb_sdk",
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
        rsp = cmdb_sdk.api.business_instance.business_tree_list_pb2.GetBusinessTreeListResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def search_app_in_system(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.business_instance.search_app_in_system_pb2.SearchAppInSystemRequest, int, str, int) -> cmdb_sdk.api.business_instance.search_app_in_system_pb2.SearchAppInSystemResponse
        """
        查询应用系统的所有子系统以及所有子系统的子系统所包含的应用
        :param request: search_app_in_system请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.business_instance.search_app_in_system_pb2.SearchAppInSystemResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.business_instance.SearchAppInSystem"
        uri = "/system/{systemInstanceId}/_search_apps".format(
            systemInstanceId=request.systemInstanceId,
        )
        requestParam = request
        
        rsp_obj = cmdb_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.cmdb_sdk",
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
        rsp = cmdb_sdk.api.business_instance.search_app_in_system_pb2.SearchAppInSystemResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def search_sub_system(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.business_instance.search_subsystem_pb2.SearchSubSystemRequest, int, str, int) -> cmdb_sdk.api.business_instance.search_subsystem_pb2.SearchSubSystemResponse
        """
        搜索系统的子系统以及，以及递归的获取子系统的子系统
        :param request: search_sub_system请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.business_instance.search_subsystem_pb2.SearchSubSystemResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.business_instance.SearchSubSystem"
        uri = "/system/{systemInstanceId}/_search_subsystem".format(
            systemInstanceId=request.systemInstanceId,
        )
        requestParam = request
        
        rsp_obj = cmdb_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.cmdb_sdk",
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
        rsp = cmdb_sdk.api.business_instance.search_subsystem_pb2.SearchSubSystemResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
