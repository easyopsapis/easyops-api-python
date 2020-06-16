# -*- coding: utf-8 -*-
import os
import sys


import cmdb_extend_sdk.api.toolkit.create_toolkit_pb2

import cmdb_extend_sdk.model.cmdb_extend.toolkit_pb2

import cmdb_extend_sdk.api.toolkit.delete_toolkit_pb2

import google.protobuf.empty_pb2

import cmdb_extend_sdk.api.toolkit.get_toolkit_pb2

import cmdb_extend_sdk.api.toolkit.get_toolkit_status_pb2

import cmdb_extend_sdk.api.toolkit.list_toolkit_pb2

import cmdb_extend_sdk.api.toolkit.update_toolkit_pb2

import cmdb_extend_sdk.api.toolkit.update_toolkit_status_pb2

import cmdb_extend_sdk.utils.http_util
import google.protobuf.json_format


class ToolkitClient(object):
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

    
    def create_toolkit(self, request, org, user, timeout=10):
        # type: (cmdb_extend_sdk.api.toolkit.create_toolkit_pb2.CreateToolkitRequest, int, str, int) -> cmdb_extend_sdk.model.cmdb_extend.toolkit_pb2.Toolkit
        """
        创建任意门
        :param request: create_toolkit请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_extend_sdk.model.cmdb_extend.toolkit_pb2.Toolkit
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb_extend.toolkit.CreateToolkit"
        uri = "/toolkit/{objectId}".format(
            objectId=request.objectId,
        )
        requestParam = request.toolkit
        
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
        rsp = cmdb_extend_sdk.model.cmdb_extend.toolkit_pb2.Toolkit()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_toolkit(self, request, org, user, timeout=10):
        # type: (cmdb_extend_sdk.api.toolkit.delete_toolkit_pb2.DeleteToolkitRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        删除指定任意门
        :param request: delete_toolkit请求
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
            route_name = "easyops.api.cmdb_extend.toolkit.DeleteToolkit"
        uri = "/toolkit/entity/{objectId}/{toolkitId}".format(
            objectId=request.objectId,
            toolkitId=request.toolkitId,
        )
        requestParam = request
        
        rsp_obj = cmdb_extend_sdk.utils.http_util.do_api_request(
            method="DELETE",
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
    
    def get_toolkit(self, request, org, user, timeout=10):
        # type: (cmdb_extend_sdk.api.toolkit.get_toolkit_pb2.GetToolkitRequest, int, str, int) -> cmdb_extend_sdk.model.cmdb_extend.toolkit_pb2.Toolkit
        """
        获取指定任意门详情
        :param request: get_toolkit请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_extend_sdk.model.cmdb_extend.toolkit_pb2.Toolkit
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb_extend.toolkit.GetToolkit"
        uri = "/toolkit/entity/{objectId}/{toolkitId}".format(
            objectId=request.objectId,
            toolkitId=request.toolkitId,
        )
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
        rsp = cmdb_extend_sdk.model.cmdb_extend.toolkit_pb2.Toolkit()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_toolkit_status(self, request, org, user, timeout=10):
        # type: (cmdb_extend_sdk.api.toolkit.get_toolkit_status_pb2.GetToolkitStatusRequest, int, str, int) -> cmdb_extend_sdk.api.toolkit.get_toolkit_status_pb2.GetToolkitStatusResponse
        """
        获取指定模型任意门状态
        :param request: get_toolkit_status请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_extend_sdk.api.toolkit.get_toolkit_status_pb2.GetToolkitStatusResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb_extend.toolkit.GetToolkitStatus"
        uri = "/toolkit/setting/{objectId}".format(
            objectId=request.objectId,
        )
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
        rsp = cmdb_extend_sdk.api.toolkit.get_toolkit_status_pb2.GetToolkitStatusResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_toolkit(self, request, org, user, timeout=10):
        # type: (cmdb_extend_sdk.api.toolkit.list_toolkit_pb2.ListToolkitRequest, int, str, int) -> cmdb_extend_sdk.api.toolkit.list_toolkit_pb2.ListToolkitResponse
        """
        获取某个模型下的所有任意门
        :param request: list_toolkit请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_extend_sdk.api.toolkit.list_toolkit_pb2.ListToolkitResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb_extend.toolkit.ListToolkit"
        uri = "/toolkit/tools/{objectId}".format(
            objectId=request.objectId,
        )
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
        rsp = cmdb_extend_sdk.api.toolkit.list_toolkit_pb2.ListToolkitResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_toolkit(self, request, org, user, timeout=10):
        # type: (cmdb_extend_sdk.api.toolkit.update_toolkit_pb2.UpdateToolkitRequest, int, str, int) -> cmdb_extend_sdk.model.cmdb_extend.toolkit_pb2.Toolkit
        """
        更新指定任意门
        :param request: update_toolkit请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_extend_sdk.model.cmdb_extend.toolkit_pb2.Toolkit
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb_extend.toolkit.UpdateToolkit"
        uri = "/toolkit/entity/{objectId}/{toolkitId}".format(
            objectId=request.objectId,
            toolkitId=request.toolkitId,
        )
        requestParam = request.toolkit
        
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
        rsp = cmdb_extend_sdk.model.cmdb_extend.toolkit_pb2.Toolkit()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_toolkit_status(self, request, org, user, timeout=10):
        # type: (cmdb_extend_sdk.api.toolkit.update_toolkit_status_pb2.UpdateToolkitStatusRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        更新指定模型任意门状态
        :param request: update_toolkit_status请求
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
            route_name = "easyops.api.cmdb_extend.toolkit.UpdateToolkitStatus"
        uri = "/toolkit/setting/{objectId}".format(
            objectId=request.objectId,
        )
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
    
