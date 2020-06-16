# -*- coding: utf-8 -*-
import os
import sys


import resource_monitor_sdk.api.resource_monitor_config.create_resource_monitor_config_pb2

import resource_monitor_sdk.api.resource_monitor_config.list_resource_monitor_config_pb2

import resource_monitor_sdk.utils.http_util
import google.protobuf.json_format


class ResourceMonitorConfigClient(object):
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

    
    def create_resource_monitor_config(self, request, org, user, timeout=10):
        # type: (resource_monitor_sdk.api.resource_monitor_config.create_resource_monitor_config_pb2.CreateResourceMonitorConfigRequest, int, str, int) -> resource_monitor_sdk.api.resource_monitor_config.create_resource_monitor_config_pb2.CreateResourceMonitorConfigResponse
        """
        创建资源监控配置
        :param request: create_resource_monitor_config请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: resource_monitor_sdk.api.resource_monitor_config.create_resource_monitor_config_pb2.CreateResourceMonitorConfigResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.resource_monitor.resource_monitor_config.CreateResourceMonitorConfig"
        uri = "/api/v1/resource-monitor-config"
        
        requestParam = request
        
        rsp_obj = resource_monitor_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.resource_monitor_sdk",
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
        rsp = resource_monitor_sdk.api.resource_monitor_config.create_resource_monitor_config_pb2.CreateResourceMonitorConfigResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_resource_monitor_config(self, request, org, user, timeout=10):
        # type: (resource_monitor_sdk.api.resource_monitor_config.list_resource_monitor_config_pb2.ListResourceMonitorConfigRequest, int, str, int) -> resource_monitor_sdk.api.resource_monitor_config.list_resource_monitor_config_pb2.ListResourceMonitorConfigResponse
        """
        获取资源监控配置列表
        :param request: list_resource_monitor_config请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: resource_monitor_sdk.api.resource_monitor_config.list_resource_monitor_config_pb2.ListResourceMonitorConfigResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.resource_monitor.resource_monitor_config.ListResourceMonitorConfig"
        uri = "/api/v1/resource-monitor-config"
        
        requestParam = request
        
        rsp_obj = resource_monitor_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.resource_monitor_sdk",
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
        rsp = resource_monitor_sdk.api.resource_monitor_config.list_resource_monitor_config_pb2.ListResourceMonitorConfigResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
