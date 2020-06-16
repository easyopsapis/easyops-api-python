# -*- coding: utf-8 -*-
import os
import sys


import topology_sdk.api.topo_view.create_topo_view_pb2

import topology_sdk.model.topology.topo_view_pb2

import topology_sdk.api.topo_view.delete_topo_view_pb2

import google.protobuf.empty_pb2

import topology_sdk.api.topo_view.get_topo_view_pb2

import topology_sdk.api.topo_view.list_topo_view_pb2

import topology_sdk.api.topo_view.update_topo_view_pb2

import topology_sdk.utils.http_util
import google.protobuf.json_format


class TopoViewClient(object):
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

    
    def create_topo_view(self, request, org, user, timeout=10):
        # type: (topology_sdk.api.topo_view.create_topo_view_pb2.CreateTopoViewRequest, int, str, int) -> topology_sdk.model.topology.topo_view_pb2.TopoView
        """
        创建拓扑视图
        :param request: create_topo_view请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: topology_sdk.model.topology.topo_view_pb2.TopoView
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.topology.topo_view.CreateTopoView"
        uri = "/api/topology/v1/view"
        
        requestParam = request
        
        rsp_obj = topology_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.topology_sdk",
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
        rsp = topology_sdk.model.topology.topo_view_pb2.TopoView()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_topo_view(self, request, org, user, timeout=10):
        # type: (topology_sdk.api.topo_view.delete_topo_view_pb2.DeleteTopoViewRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        删除拓扑视图
        :param request: delete_topo_view请求
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
            route_name = "easyops.api.topology.topo_view.DeleteTopoView"
        uri = "/api/topology/v1/view/{id}".format(
            id=request.id,
        )
        requestParam = request
        
        rsp_obj = topology_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.topology_sdk",
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
    
    def get_topo_view(self, request, org, user, timeout=10):
        # type: (topology_sdk.api.topo_view.get_topo_view_pb2.GetTopoViewRequest, int, str, int) -> topology_sdk.model.topology.topo_view_pb2.TopoView
        """
        获取拓扑视图详细数据
        :param request: get_topo_view请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: topology_sdk.model.topology.topo_view_pb2.TopoView
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.topology.topo_view.GetTopoView"
        uri = "/api/topology/v1/view/{id}".format(
            id=request.id,
        )
        requestParam = request
        
        rsp_obj = topology_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.topology_sdk",
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
        rsp = topology_sdk.model.topology.topo_view_pb2.TopoView()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_topo_view(self, request, org, user, timeout=10):
        # type: (topology_sdk.api.topo_view.list_topo_view_pb2.ListTopoViewRequest, int, str, int) -> topology_sdk.api.topo_view.list_topo_view_pb2.ListTopoViewResponse
        """
        获取拓扑视图列表
        :param request: list_topo_view请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: topology_sdk.api.topo_view.list_topo_view_pb2.ListTopoViewResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.topology.topo_view.ListTopoView"
        uri = "/api/topology/v1/views"
        
        requestParam = request
        
        rsp_obj = topology_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.topology_sdk",
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
        rsp = topology_sdk.api.topo_view.list_topo_view_pb2.ListTopoViewResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_topo_view(self, request, org, user, timeout=10):
        # type: (topology_sdk.api.topo_view.update_topo_view_pb2.UpdateTopoViewRequest, int, str, int) -> topology_sdk.model.topology.topo_view_pb2.TopoView
        """
        更新拓扑视图
        :param request: update_topo_view请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: topology_sdk.model.topology.topo_view_pb2.TopoView
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.topology.topo_view.UpdateTopoView"
        uri = "/api/topology/v1/view/{id}".format(
            id=request.id,
        )
        requestParam = request
        
        rsp_obj = topology_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.topology_sdk",
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
        rsp = topology_sdk.model.topology.topo_view_pb2.TopoView()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
