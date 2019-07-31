# -*- coding: utf-8 -*-
import os
import sys

current_path = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = os.path.dirname(os.path.dirname(current_path))
if PROJECT_PATH not in sys.path:
    sys.path.append(PROJECT_PATH)


import model.tool.tool_pb2

import create_tool_pb2

import delete_tool_pb2

import google.protobuf.empty_pb2

import get_tool_pb2

import get_tool_categories_pb2

import list_tool_pb2

import utils.http_util
import google.protobuf.json_format


class BasicClient(object):
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

    
    def create_tool(self, request, org, user, timeout=10):
        # type: (model.tool.tool_pb2.Tool, int, str, int) -> create_tool_pb2.CreateToolResponse
        """
        创建工具
        :param request: create_tool请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: create_tool_pb2.CreateToolResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.tool.basic.CreateTool"
        uri = "/tools"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.tool_sdk",
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
        rsp = create_tool_pb2.CreateToolResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_tool(self, request, org, user, timeout=10):
        # type: (delete_tool_pb2.DeleteToolRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        删除工具
        :param request: delete_tool请求
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
            route_name = "easyops.api.tool.basic.DeleteTool"
        uri = "/tools/{toolId}".format(
            toolId=request.toolId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.tool_sdk",
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
    
    def get_tool(self, request, org, user, timeout=10):
        # type: (get_tool_pb2.GetToolRequest, int, str, int) -> model.tool.tool_pb2.Tool
        """
        获取工具信息
        :param request: get_tool请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: model.tool.tool_pb2.Tool
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.tool.basic.GetTool"
        uri = "/tools/{toolId}".format(
            toolId=request.toolId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="GET",
            src_name="logic.tool_sdk",
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
        rsp = model.tool.tool_pb2.Tool()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_tool_categories(self, request, org, user, timeout=10):
        # type: (google.protobuf.empty_pb2.Empty, int, str, int) -> get_tool_categories_pb2.GetToolCategoriesResponse
        """
        批量获取工具分类
        :param request: get_tool_categories请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: get_tool_categories_pb2.GetToolCategoriesResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.tool.basic.GetToolCategories"
        uri = "/tool_categories"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="GET",
            src_name="logic.tool_sdk",
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
        rsp = get_tool_categories_pb2.GetToolCategoriesResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_tool(self, request, org, user, timeout=10):
        # type: (list_tool_pb2.ListToolRequest, int, str, int) -> list_tool_pb2.ListToolResponse
        """
        批量获取工具信息
        :param request: list_tool请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: list_tool_pb2.ListToolResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.tool.basic.ListTool"
        uri = "/tools"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="GET",
            src_name="logic.tool_sdk",
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
        rsp = list_tool_pb2.ListToolResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_tool(self, request, org, user, timeout=10):
        # type: (model.tool.tool_pb2.Tool, int, str, int) -> model.tool.tool_pb2.Tool
        """
        修改工具
        :param request: update_tool请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: model.tool.tool_pb2.Tool
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.tool.basic.UpdateTool"
        uri = "/tools/{toolId}".format(
            toolId=request.toolId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.tool_sdk",
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
        rsp = model.tool.tool_pb2.Tool()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
