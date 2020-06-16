# -*- coding: utf-8 -*-
import os
import sys


import next_builder_sdk.api.storyboard.delete_storyboard_pb2

import google.protobuf.empty_pb2

import next_builder_sdk.api.storyboard.import_single_storyboard_pb2

import next_builder_sdk.api.storyboard.import_storyboard_pb2

import next_builder_sdk.api.storyboard.search_children_storyboard_pb2

import next_builder_sdk.api.storyboard.sort_single_storyboard_pb2

import next_builder_sdk.model.next_builder.storyboard_node_pb2

import next_builder_sdk.api.storyboard.sort_storyboard_pb2

import next_builder_sdk.utils.http_util
import google.protobuf.json_format


class StoryboardClient(object):
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

    
    def delete_storyboard_node(self, request, org, user, timeout=10):
        # type: (next_builder_sdk.api.storyboard.delete_storyboard_pb2.DeleteStoryboardNodeRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        storyboard节点删除
        :param request: delete_storyboard_node请求
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
            route_name = "easyops.api.next_builder.storyboard.DeleteStoryboardNode"
        uri = "/api/v1/nextBuilder/delete"
        
        requestParam = request
        
        rsp_obj = next_builder_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.next_builder_sdk",
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
    
    def import_storyboard_node(self, request, org, user, timeout=10):
        # type: (next_builder_sdk.api.storyboard.import_single_storyboard_pb2.ImportStoryboardNodeRequest, int, str, int) -> next_builder_sdk.api.storyboard.import_single_storyboard_pb2.ImportStoryboardNodeResponse
        """
        导入storyboard节点
        :param request: import_storyboard_node请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: next_builder_sdk.api.storyboard.import_single_storyboard_pb2.ImportStoryboardNodeResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.next_builder.storyboard.ImportStoryboardNode"
        uri = "/api/v1/nextBuilder/importNode"
        
        requestParam = request
        
        rsp_obj = next_builder_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.next_builder_sdk",
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
        rsp = next_builder_sdk.api.storyboard.import_single_storyboard_pb2.ImportStoryboardNodeResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def import_storyboard_nodes(self, request, org, user, timeout=10):
        # type: (next_builder_sdk.api.storyboard.import_storyboard_pb2.ImportStoryboardNodesRequest, int, str, int) -> next_builder_sdk.api.storyboard.import_storyboard_pb2.ImportStoryboardNodesResponse
        """
        批量导入storyboard节点
        :param request: import_storyboard_nodes请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: next_builder_sdk.api.storyboard.import_storyboard_pb2.ImportStoryboardNodesResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.next_builder.storyboard.ImportStoryboardNodes"
        uri = "/api/v1/nextBuilder/importNodes"
        
        requestParam = request
        
        rsp_obj = next_builder_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.next_builder_sdk",
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
        rsp = next_builder_sdk.api.storyboard.import_storyboard_pb2.ImportStoryboardNodesResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def search_storyboard_child_nodes(self, request, org, user, timeout=10):
        # type: (next_builder_sdk.api.storyboard.search_children_storyboard_pb2.SearchStoryboardChildNodesRequest, int, str, int) -> next_builder_sdk.api.storyboard.search_children_storyboard_pb2.SearchStoryboardChildNodesResponse
        """
        获取storyboard节点的子节点
        :param request: search_storyboard_child_nodes请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: next_builder_sdk.api.storyboard.search_children_storyboard_pb2.SearchStoryboardChildNodesResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.next_builder.storyboard.SearchStoryboardChildNodes"
        uri = "/api/v1/nextBuilder/childNodes/{nodeId}".format(
            nodeId=request.nodeId,
        )
        requestParam = request
        
        rsp_obj = next_builder_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.next_builder_sdk",
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
        rsp = next_builder_sdk.api.storyboard.search_children_storyboard_pb2.SearchStoryboardChildNodesResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def sort_storyboard_node(self, request, org, user, timeout=10):
        # type: (next_builder_sdk.api.storyboard.sort_single_storyboard_pb2.SortStoryboardNodeRequest, int, str, int) -> next_builder_sdk.model.next_builder.storyboard_node_pb2.StoryboardNode
        """
        更新单个storyboard节点排序
        :param request: sort_storyboard_node请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: next_builder_sdk.model.next_builder.storyboard_node_pb2.StoryboardNode
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.next_builder.storyboard.SortStoryboardNode"
        uri = "/api/v1/nextBuilder/sortNode"
        
        requestParam = request
        
        rsp_obj = next_builder_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.next_builder_sdk",
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
        rsp = next_builder_sdk.model.next_builder.storyboard_node_pb2.StoryboardNode()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def sort_storyboard_nodes(self, request, org, user, timeout=10):
        # type: (next_builder_sdk.api.storyboard.sort_storyboard_pb2.SortStoryboardNodesRequest, int, str, int) -> next_builder_sdk.api.storyboard.sort_storyboard_pb2.SortStoryboardNodesResponse
        """
        storyboard节点排序
        :param request: sort_storyboard_nodes请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: next_builder_sdk.api.storyboard.sort_storyboard_pb2.SortStoryboardNodesResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.next_builder.storyboard.SortStoryboardNodes"
        uri = "/api/v1/nextBuilder/sortNodes"
        
        requestParam = request
        
        rsp_obj = next_builder_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.next_builder_sdk",
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
        rsp = next_builder_sdk.api.storyboard.sort_storyboard_pb2.SortStoryboardNodesResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
