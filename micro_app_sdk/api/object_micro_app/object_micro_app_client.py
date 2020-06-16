# -*- coding: utf-8 -*-
import os
import sys


import micro_app_sdk.api.object_micro_app.aggregate_micro_app_pb2

import micro_app_sdk.api.object_micro_app.bind_object_micro_app_pb2

import google.protobuf.empty_pb2

import micro_app_sdk.api.object_micro_app.get_micro_app_list_pb2

import micro_app_sdk.api.object_micro_app.get_micro_app_list_by_objectId_pb2

import micro_app_sdk.api.object_micro_app.get_object_by_micro_app_pb2

import micro_app_sdk.model.micro_app.object_micro_app_pb2

import micro_app_sdk.api.object_micro_app.search_micro_app_list_pb2

import micro_app_sdk.utils.http_util
import google.protobuf.json_format


class ObjectMicroAppClient(object):
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

    
    def aggregate_micro_app(self, request, org, user, timeout=10):
        # type: (micro_app_sdk.api.object_micro_app.aggregate_micro_app_pb2.AggregateMicroAppRequest, int, str, int) -> micro_app_sdk.api.object_micro_app.aggregate_micro_app_pb2.AggregateMicroAppResponse
        """
        根据模型ID聚合小产品
        :param request: aggregate_micro_app请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: micro_app_sdk.api.object_micro_app.aggregate_micro_app_pb2.AggregateMicroAppResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.micro_app.object_micro_app.AggregateMicroApp"
        uri = "/api/micro_app/v1/object_micro_app/aggregate"
        
        requestParam = request
        
        rsp_obj = micro_app_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.micro_app_sdk",
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
        rsp = micro_app_sdk.api.object_micro_app.aggregate_micro_app_pb2.AggregateMicroAppResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def bind_object_micro_app(self, request, org, user, timeout=10):
        # type: (micro_app_sdk.api.object_micro_app.bind_object_micro_app_pb2.BindObjectMicroAppRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        绑定Object与MicroApp关系
        :param request: bind_object_micro_app请求
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
            route_name = "easyops.api.micro_app.object_micro_app.BindObjectMicroApp"
        uri = "/api/micro_app/v1/object_micro_app/bind"
        
        requestParam = request
        
        rsp_obj = micro_app_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.micro_app_sdk",
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
    
    def get_object_micro_app_list(self, request, org, user, timeout=10):
        # type: (google.protobuf.empty_pb2.Empty, int, str, int) -> micro_app_sdk.api.object_micro_app.get_micro_app_list_pb2.GetObjectMicroAppListResponse
        """
        查询模型关联小产品列表
        :param request: get_object_micro_app_list请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: micro_app_sdk.api.object_micro_app.get_micro_app_list_pb2.GetObjectMicroAppListResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.micro_app.object_micro_app.GetObjectMicroAppList"
        uri = "/api/micro_app/v1/object_micro_app"
        
        requestParam = request
        
        rsp_obj = micro_app_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.micro_app_sdk",
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
        rsp = micro_app_sdk.api.object_micro_app.get_micro_app_list_pb2.GetObjectMicroAppListResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_micro_app_list(self, request, org, user, timeout=10):
        # type: (micro_app_sdk.api.object_micro_app.get_micro_app_list_by_objectId_pb2.GetMicroAppListRequest, int, str, int) -> micro_app_sdk.api.object_micro_app.get_micro_app_list_by_objectId_pb2.GetMicroAppListResponse
        """
        根据模型查询关联小产品列表
        :param request: get_micro_app_list请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: micro_app_sdk.api.object_micro_app.get_micro_app_list_by_objectId_pb2.GetMicroAppListResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.micro_app.object_micro_app.GetMicroAppList"
        uri = "/api/micro_app/v1/object_micro_app/object_id/{object_id}".format(
            object_id=request.object_id,
        )
        requestParam = request
        
        rsp_obj = micro_app_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.micro_app_sdk",
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
        rsp = micro_app_sdk.api.object_micro_app.get_micro_app_list_by_objectId_pb2.GetMicroAppListResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_object_by_micro_app(self, request, org, user, timeout=10):
        # type: (micro_app_sdk.api.object_micro_app.get_object_by_micro_app_pb2.GetObjectByMicroAppRequest, int, str, int) -> micro_app_sdk.model.micro_app.object_micro_app_pb2.ObjectMicroApp
        """
        根据小产品查询模型和小产品关联信息
        :param request: get_object_by_micro_app请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: micro_app_sdk.model.micro_app.object_micro_app_pb2.ObjectMicroApp
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.micro_app.object_micro_app.GetObjectByMicroApp"
        uri = "/api/micro_app/v1/object_micro_app/appId/{appId}".format(
            appId=request.appId,
        )
        requestParam = request
        
        rsp_obj = micro_app_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.micro_app_sdk",
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
        rsp = micro_app_sdk.model.micro_app.object_micro_app_pb2.ObjectMicroApp()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def search_micro_app_list(self, request, org, user, timeout=10):
        # type: (micro_app_sdk.api.object_micro_app.search_micro_app_list_pb2.SearchMicroAppListRequest, int, str, int) -> micro_app_sdk.api.object_micro_app.search_micro_app_list_pb2.SearchMicroAppListResponse
        """
        搜索模型查询关联小产品列表
        :param request: search_micro_app_list请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: micro_app_sdk.api.object_micro_app.search_micro_app_list_pb2.SearchMicroAppListResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.micro_app.object_micro_app.SearchMicroAppList"
        uri = "/api/micro_app/v1/object_micro_app/search"
        
        requestParam = request
        
        rsp_obj = micro_app_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.micro_app_sdk",
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
        rsp = micro_app_sdk.api.object_micro_app.search_micro_app_list_pb2.SearchMicroAppListResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
