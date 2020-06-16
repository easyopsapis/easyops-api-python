# -*- coding: utf-8 -*-
import os
import sys


import resource_monitor_sdk.api.related_resource.create_related_resource_pb2

import resource_monitor_sdk.api.related_resource.delete_related_resource_pb2

import google.protobuf.empty_pb2

import resource_monitor_sdk.api.related_resource.list_related_resource_pb2

import resource_monitor_sdk.api.related_resource.update_related_resource_pb2

import resource_monitor_sdk.utils.http_util
import google.protobuf.json_format


class RelatedResourceClient(object):
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

    
    def create_related_resource(self, request, org, user, timeout=10):
        # type: (resource_monitor_sdk.api.related_resource.create_related_resource_pb2.CreateRelatedResourceRequest, int, str, int) -> resource_monitor_sdk.api.related_resource.create_related_resource_pb2.CreateRelatedResourceResponse
        """
        创建关联资源
        :param request: create_related_resource请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: resource_monitor_sdk.api.related_resource.create_related_resource_pb2.CreateRelatedResourceResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.resource_monitor.related_resource.CreateRelatedResource"
        uri = "/api/v1/related-resource"
        
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
        rsp = resource_monitor_sdk.api.related_resource.create_related_resource_pb2.CreateRelatedResourceResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_related_resource(self, request, org, user, timeout=10):
        # type: (resource_monitor_sdk.api.related_resource.delete_related_resource_pb2.DeleteRelatedResourceRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        删除关联资源
        :param request: delete_related_resource请求
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
            route_name = "easyops.api.resource_monitor.related_resource.DeleteRelatedResource"
        uri = "/api/v1/related-resource/{instanceId}".format(
            instanceId=request.instanceId,
        )
        requestParam = request
        
        rsp_obj = resource_monitor_sdk.utils.http_util.do_api_request(
            method="DELETE",
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
        rsp = google.protobuf.empty_pb2.Empty()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_related_resource(self, request, org, user, timeout=10):
        # type: (resource_monitor_sdk.api.related_resource.list_related_resource_pb2.ListRelatedResourceRequest, int, str, int) -> resource_monitor_sdk.api.related_resource.list_related_resource_pb2.ListRelatedResourceResponse
        """
        获取关联资源
        :param request: list_related_resource请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: resource_monitor_sdk.api.related_resource.list_related_resource_pb2.ListRelatedResourceResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.resource_monitor.related_resource.ListRelatedResource"
        uri = "/api/v1/related-resource"
        
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
        rsp = resource_monitor_sdk.api.related_resource.list_related_resource_pb2.ListRelatedResourceResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_related_resource(self, request, org, user, timeout=10):
        # type: (resource_monitor_sdk.api.related_resource.update_related_resource_pb2.UpdateRelatedResourceRequest, int, str, int) -> resource_monitor_sdk.api.related_resource.update_related_resource_pb2.UpdateRelatedResourceResponse
        """
        创建关联资源
        :param request: update_related_resource请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: resource_monitor_sdk.api.related_resource.update_related_resource_pb2.UpdateRelatedResourceResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.resource_monitor.related_resource.UpdateRelatedResource"
        uri = "/api/v1/related-resource/{instanceId}".format(
            instanceId=request.instanceId,
        )
        requestParam = request
        
        rsp_obj = resource_monitor_sdk.utils.http_util.do_api_request(
            method="PUT",
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
        rsp = resource_monitor_sdk.api.related_resource.update_related_resource_pb2.UpdateRelatedResourceResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
