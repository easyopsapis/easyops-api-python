# -*- coding: utf-8 -*-
import os
import sys


import container_sdk.api.resourcegroup.delete_resourcegroup_pb2

import google.protobuf.empty_pb2

import container_sdk.api.resourcegroup.list_pb2

import container_sdk.utils.http_util
import google.protobuf.json_format


class ResourcegroupClient(object):
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

    
    def delete_resource_group(self, request, org, user, timeout=10):
        # type: (container_sdk.api.resourcegroup.delete_resourcegroup_pb2.DeleteResourceGroupRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        删除 resourcegroup
        :param request: delete_resource_group请求
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
            route_name = "easyops.api.container.resourcegroup.DeleteResourceGroup"
        uri = "/api/container/v1/resourcegroups/{instanceId}".format(
            instanceId=request.instanceId,
        )
        requestParam = request
        
        rsp_obj = container_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.container_sdk",
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
    
    def list(self, request, org, user, timeout=10):
        # type: (container_sdk.api.resourcegroup.list_pb2.ListRequest, int, str, int) -> container_sdk.api.resourcegroup.list_pb2.ListResponse
        """
        获取 resourcegroup 列表
        :param request: list请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: container_sdk.api.resourcegroup.list_pb2.ListResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.container.resourcegroup.List"
        uri = "/api/container/v1/resourcegroups"
        
        requestParam = request
        
        rsp_obj = container_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.container_sdk",
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
        rsp = container_sdk.api.resourcegroup.list_pb2.ListResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
