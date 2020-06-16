# -*- coding: utf-8 -*-
import os
import sys


import resource_manage_sdk.api.service_manage.create_service_task_pb2

import resource_manage_sdk.api.service_manage.create_service_topology_task_pb2

import resource_manage_sdk.api.service_manage.list_service_info_pb2

import resource_manage_sdk.utils.http_util
import google.protobuf.json_format


class ServiceManageClient(object):
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

    
    def create_service_task(self, request, org, user, timeout=10):
        # type: (resource_manage_sdk.api.service_manage.create_service_task_pb2.CreateServiceTaskRequest, int, str, int) -> resource_manage_sdk.api.service_manage.create_service_task_pb2.CreateServiceTaskResponse
        """
        执行服务管理相关任务
        :param request: create_service_task请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: resource_manage_sdk.api.service_manage.create_service_task_pb2.CreateServiceTaskResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.resource_manage.service_manage.CreateServiceTask"
        uri = "/api/v1/service/task"
        
        requestParam = request
        
        rsp_obj = resource_manage_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.resource_manage_sdk",
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
        rsp = resource_manage_sdk.api.service_manage.create_service_task_pb2.CreateServiceTaskResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def create_service_topology_task(self, request, org, user, timeout=10):
        # type: (resource_manage_sdk.api.service_manage.create_service_topology_task_pb2.CreateServiceTopologyTaskRequest, int, str, int) -> resource_manage_sdk.api.service_manage.create_service_topology_task_pb2.CreateServiceTopologyTaskResponse
        """
        创建服务拓扑任务
        :param request: create_service_topology_task请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: resource_manage_sdk.api.service_manage.create_service_topology_task_pb2.CreateServiceTopologyTaskResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.resource_manage.service_manage.CreateServiceTopologyTask"
        uri = "/api/v2/service/task/topology"
        
        requestParam = request
        
        rsp_obj = resource_manage_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.resource_manage_sdk",
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
        rsp = resource_manage_sdk.api.service_manage.create_service_topology_task_pb2.CreateServiceTopologyTaskResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_service_info(self, request, org, user, timeout=10):
        # type: (resource_manage_sdk.api.service_manage.list_service_info_pb2.ListServiceInfoRequest, int, str, int) -> resource_manage_sdk.api.service_manage.list_service_info_pb2.ListServiceInfoResponse
        """
        查询所有服务信息
        :param request: list_service_info请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: resource_manage_sdk.api.service_manage.list_service_info_pb2.ListServiceInfoResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.resource_manage.service_manage.ListServiceInfo"
        uri = "/api/v1/service/info"
        
        requestParam = request
        
        rsp_obj = resource_manage_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.resource_manage_sdk",
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
        rsp = resource_manage_sdk.api.service_manage.list_service_info_pb2.ListServiceInfoResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
