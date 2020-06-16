# -*- coding: utf-8 -*-
import os
import sys


import cmdb_extend_sdk.api.host_resolved.create_one_pb2

import google.protobuf.struct_pb2

import cmdb_extend_sdk.api.host_resolved.search_pb2

import cmdb_extend_sdk.api.host_resolved.update_by_query_pb2

import google.protobuf.empty_pb2

import cmdb_extend_sdk.api.host_resolved.update_host_unresolved_pb2

import cmdb_extend_sdk.api.host_resolved.update_one_pb2

import cmdb_extend_sdk.utils.http_util
import google.protobuf.json_format


class HostResolvedClient(object):
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

    
    def create_one(self, request, org, user, timeout=10):
        # type: (cmdb_extend_sdk.api.host_resolved.create_one_pb2.CreateOneRequest, int, str, int) -> google.protobuf.struct_pb2.Struct
        """
        创建主机冲突
        :param request: create_one请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: google.protobuf.struct_pb2.Struct
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb_extend.host_resolved.CreateOne"
        uri = "/system/storage/collection/t_alert_hostresolved/document"
        
        requestParam = request.data
        
        rsp_obj = cmdb_extend_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.cmdb_extend_sdk",
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
        rsp = google.protobuf.struct_pb2.Struct()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def search(self, request, org, user, timeout=10):
        # type: (cmdb_extend_sdk.api.host_resolved.search_pb2.SearchRequest, int, str, int) -> cmdb_extend_sdk.api.host_resolved.search_pb2.SearchResponse
        """
        搜索主机冲突实例
        :param request: search请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_extend_sdk.api.host_resolved.search_pb2.SearchResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb_extend.host_resolved.Search"
        uri = "/system/storage/collection/t_alert_hostresolved/document/search"
        
        requestParam = request
        
        rsp_obj = cmdb_extend_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.cmdb_extend_sdk",
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
        rsp = cmdb_extend_sdk.api.host_resolved.search_pb2.SearchResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_by_query(self, request, org, user, timeout=10):
        # type: (cmdb_extend_sdk.api.host_resolved.update_by_query_pb2.UpdateByQueryRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        根据条件更新主机冲突实例
        :param request: update_by_query请求
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
            route_name = "easyops.api.cmdb_extend.host_resolved.UpdateByQuery"
        uri = "/system/storage/collection/t_alert_hostresolved/document_by_query"
        
        requestParam = request
        
        rsp_obj = cmdb_extend_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.cmdb_extend_sdk",
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
    
    def update_host_unresolved(self, request, org, user, timeout=10):
        # type: (cmdb_extend_sdk.api.host_resolved.update_host_unresolved_pb2.UpdateHostUnresolvedRequest, int, str, int) -> google.protobuf.struct_pb2.Struct
        """
        主机冲突解决接口
        :param request: update_host_unresolved请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: google.protobuf.struct_pb2.Struct
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb_extend.host_resolved.UpdateHostUnresolved"
        uri = "/system/storage/hostResolved/document"
        
        requestParam = request
        
        rsp_obj = cmdb_extend_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.cmdb_extend_sdk",
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
        rsp = google.protobuf.struct_pb2.Struct()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_one(self, request, org, user, timeout=10):
        # type: (cmdb_extend_sdk.api.host_resolved.update_one_pb2.UpdateOneRequest, int, str, int) -> google.protobuf.struct_pb2.Struct
        """
        更新主机冲突实例
        :param request: update_one请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: google.protobuf.struct_pb2.Struct
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb_extend.host_resolved.UpdateOne"
        uri = "/system/storage/collection/t_alert_hostresolved/document/{id}".format(
            id=request.id,
        )
        requestParam = request.data
        
        rsp_obj = cmdb_extend_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.cmdb_extend_sdk",
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
        rsp = google.protobuf.struct_pb2.Struct()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
