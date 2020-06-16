# -*- coding: utf-8 -*-
import os
import sys


import database_delivery_sdk.api.dbclient.create_pb2

import database_delivery_sdk.model.database_delivery.dbclient_pb2

import database_delivery_sdk.model.easy_command.task_detail_pb2

import database_delivery_sdk.api.dbclient.create_callback_pb2

import database_delivery_sdk.api.dbclient.delete_pb2

import google.protobuf.empty_pb2

import database_delivery_sdk.api.dbclient.list_pb2

import database_delivery_sdk.utils.http_util
import google.protobuf.json_format


class DbclientClient(object):
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

    
    def create_client(self, request, org, user, timeout=10):
        # type: (database_delivery_sdk.api.dbclient.create_pb2.CreateClientRequest, int, str, int) -> database_delivery_sdk.model.database_delivery.dbclient_pb2.DBClient
        """
        创建客户端
        :param request: create_client请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: database_delivery_sdk.model.database_delivery.dbclient_pb2.DBClient
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.database_delivery.dbclient.CreateClient"
        uri = "/api/v1/client"
        
        requestParam = request
        
        rsp_obj = database_delivery_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.database_delivery_sdk",
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
        rsp = database_delivery_sdk.model.database_delivery.dbclient_pb2.DBClient()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def create_client_callback(self, request, org, user, timeout=10):
        # type: (database_delivery_sdk.model.easy_command.task_detail_pb2.TaskDetail, int, str, int) -> database_delivery_sdk.api.dbclient.create_callback_pb2.CreateClientCallbackResponse
        """
        创建客户端回调
        :param request: create_client_callback请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: database_delivery_sdk.api.dbclient.create_callback_pb2.CreateClientCallbackResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.database_delivery.dbclient.CreateClientCallback"
        uri = "/api/v1/client/callback"
        
        requestParam = request
        
        rsp_obj = database_delivery_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.database_delivery_sdk",
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
        rsp = database_delivery_sdk.api.dbclient.create_callback_pb2.CreateClientCallbackResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_client(self, request, org, user, timeout=10):
        # type: (database_delivery_sdk.api.dbclient.delete_pb2.DeleteClientRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        删除客户端
        :param request: delete_client请求
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
            route_name = "easyops.api.database_delivery.dbclient.DeleteClient"
        uri = "/api/v1/client/{clientIp}".format(
            clientIp=request.clientIp,
        )
        requestParam = request
        
        rsp_obj = database_delivery_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.database_delivery_sdk",
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
    
    def list_client(self, request, org, user, timeout=10):
        # type: (database_delivery_sdk.api.dbclient.list_pb2.ListClientRequest, int, str, int) -> database_delivery_sdk.api.dbclient.list_pb2.ListClientResponse
        """
        获取客户端列表
        :param request: list_client请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: database_delivery_sdk.api.dbclient.list_pb2.ListClientResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.database_delivery.dbclient.ListClient"
        uri = "/api/v1/client"
        
        requestParam = request
        
        rsp_obj = database_delivery_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.database_delivery_sdk",
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
        rsp = database_delivery_sdk.api.dbclient.list_pb2.ListClientResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
