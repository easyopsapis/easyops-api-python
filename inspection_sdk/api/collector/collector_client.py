# -*- coding: utf-8 -*-
import os
import sys


import inspection_sdk.api.collector.create_pb2

import inspection_sdk.api.collector.debug_pb2

import inspection_sdk.api.collector.delete_pb2

import google.protobuf.empty_pb2

import inspection_sdk.api.collector.get_pb2

import inspection_sdk.model.inspection.collector_pb2

import inspection_sdk.api.collector.list_pb2

import inspection_sdk.api.collector.update_pb2

import inspection_sdk.utils.http_util
import google.protobuf.json_format


class CollectorClient(object):
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

    
    def create_collector(self, request, org, user, timeout=10):
        # type: (inspection_sdk.api.collector.create_pb2.CreateCollectorRequest, int, str, int) -> inspection_sdk.api.collector.create_pb2.CreateCollectorResponse
        """
        创建采集脚本
        :param request: create_collector请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: inspection_sdk.api.collector.create_pb2.CreateCollectorResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.inspection.collector.CreateCollector"
        uri = "/api/v1/inspection/{pluginId}/collector".format(
            pluginId=request.pluginId,
        )
        requestParam = request
        
        rsp_obj = inspection_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.inspection_sdk",
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
        rsp = inspection_sdk.api.collector.create_pb2.CreateCollectorResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def debug_collector(self, request, org, user, timeout=10):
        # type: (inspection_sdk.api.collector.debug_pb2.DebugCollectorRequest, int, str, int) -> inspection_sdk.api.collector.debug_pb2.DebugCollectorResponse
        """
        调试采集脚本
        :param request: debug_collector请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: inspection_sdk.api.collector.debug_pb2.DebugCollectorResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.inspection.collector.DebugCollector"
        uri = "/api/v1/inspection/{pluginId}/collector-debug".format(
            pluginId=request.pluginId,
        )
        requestParam = request
        
        rsp_obj = inspection_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.inspection_sdk",
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
        rsp = inspection_sdk.api.collector.debug_pb2.DebugCollectorResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_collector(self, request, org, user, timeout=10):
        # type: (inspection_sdk.api.collector.delete_pb2.DeleteCollectorRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        删除采集脚本
        :param request: delete_collector请求
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
            route_name = "easyops.api.inspection.collector.DeleteCollector"
        uri = "/api/v1/inspection/{pluginId}/collector/{collectorId}".format(
            pluginId=request.pluginId,
            collectorId=request.collectorId,
        )
        requestParam = request
        
        rsp_obj = inspection_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.inspection_sdk",
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
    
    def get_collector(self, request, org, user, timeout=10):
        # type: (inspection_sdk.api.collector.get_pb2.GetCollectorRequest, int, str, int) -> inspection_sdk.model.inspection.collector_pb2.InspectionCollector
        """
        获取采集脚本
        :param request: get_collector请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: inspection_sdk.model.inspection.collector_pb2.InspectionCollector
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.inspection.collector.GetCollector"
        uri = "/api/v1/inspection/{pluginId}/collector/{collectorId}".format(
            pluginId=request.pluginId,
            collectorId=request.collectorId,
        )
        requestParam = request
        
        rsp_obj = inspection_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.inspection_sdk",
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
        rsp = inspection_sdk.model.inspection.collector_pb2.InspectionCollector()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_collector(self, request, org, user, timeout=10):
        # type: (inspection_sdk.api.collector.list_pb2.ListCollectorRequest, int, str, int) -> inspection_sdk.api.collector.list_pb2.ListCollectorResponse
        """
        获取采集脚本列表
        :param request: list_collector请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: inspection_sdk.api.collector.list_pb2.ListCollectorResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.inspection.collector.ListCollector"
        uri = "/api/v1/inspection/{pluginId}/collector".format(
            pluginId=request.pluginId,
        )
        requestParam = request
        
        rsp_obj = inspection_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.inspection_sdk",
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
        rsp = inspection_sdk.api.collector.list_pb2.ListCollectorResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_collector(self, request, org, user, timeout=10):
        # type: (inspection_sdk.api.collector.update_pb2.UpdateCollectorRequest, int, str, int) -> inspection_sdk.model.inspection.collector_pb2.InspectionCollector
        """
        更新采集脚本
        :param request: update_collector请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: inspection_sdk.model.inspection.collector_pb2.InspectionCollector
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.inspection.collector.UpdateCollector"
        uri = "/api/v1/inspection/{pluginId}/collector/{collectorId}".format(
            pluginId=request.pluginId,
            collectorId=request.collectorId,
        )
        requestParam = request
        
        rsp_obj = inspection_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.inspection_sdk",
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
        rsp = inspection_sdk.model.inspection.collector_pb2.InspectionCollector()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
