# -*- coding: utf-8 -*-
import os
import sys


import capacity_admin_sdk.api.portrait.create_portrait_pb2

import capacity_admin_sdk.api.portrait.delete_portrait_pb2

import google.protobuf.empty_pb2

import capacity_admin_sdk.api.portrait.get_portrait_detail_pb2

import capacity_admin_sdk.api.portrait.list_portraits_pb2

import capacity_admin_sdk.api.portrait.update_portrait_pb2

import capacity_admin_sdk.model.capacity_admin.portrait_pb2

import capacity_admin_sdk.utils.http_util
import google.protobuf.json_format


class PortraitClient(object):
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

    
    def create_portrait(self, request, org, user, timeout=10):
        # type: (capacity_admin_sdk.api.portrait.create_portrait_pb2.CreatePortraitRequest, int, str, int) -> capacity_admin_sdk.api.portrait.create_portrait_pb2.CreatePortraitResponse
        """
        创建容量管理-闲置资源画像
        :param request: create_portrait请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: capacity_admin_sdk.api.portrait.create_portrait_pb2.CreatePortraitResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.capacity_admin.portrait.CreatePortrait"
        uri = "/api/capacity_admin/v1/portrait"
        
        requestParam = request
        
        rsp_obj = capacity_admin_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.capacity_admin_sdk",
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
        rsp = capacity_admin_sdk.api.portrait.create_portrait_pb2.CreatePortraitResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_portrait(self, request, org, user, timeout=10):
        # type: (capacity_admin_sdk.api.portrait.delete_portrait_pb2.DeletePortraitRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        删除画像
        :param request: delete_portrait请求
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
            route_name = "easyops.api.capacity_admin.portrait.DeletePortrait"
        uri = "/api/capacity_admin/v1/portrait/{portraitId}".format(
            portraitId=request.portraitId,
        )
        requestParam = request
        
        rsp_obj = capacity_admin_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.capacity_admin_sdk",
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
    
    def get_portrait_detail(self, request, org, user, timeout=10):
        # type: (capacity_admin_sdk.api.portrait.get_portrait_detail_pb2.GetPortraitDetailRequest, int, str, int) -> capacity_admin_sdk.api.portrait.get_portrait_detail_pb2.GetPortraitDetailResponse
        """
        获取容量管理-闲置资源画像配置
        :param request: get_portrait_detail请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: capacity_admin_sdk.api.portrait.get_portrait_detail_pb2.GetPortraitDetailResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.capacity_admin.portrait.GetPortraitDetail"
        uri = "/api/capacity_admin/v1/portrait/{portraitId}".format(
            portraitId=request.portraitId,
        )
        requestParam = request
        
        rsp_obj = capacity_admin_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.capacity_admin_sdk",
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
        rsp = capacity_admin_sdk.api.portrait.get_portrait_detail_pb2.GetPortraitDetailResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_portraits(self, request, org, user, timeout=10):
        # type: (capacity_admin_sdk.api.portrait.list_portraits_pb2.ListPortraitsRequest, int, str, int) -> capacity_admin_sdk.api.portrait.list_portraits_pb2.ListPortraitsResponse
        """
        获取容量管理-闲置资源画像列表
        :param request: list_portraits请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: capacity_admin_sdk.api.portrait.list_portraits_pb2.ListPortraitsResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.capacity_admin.portrait.ListPortraits"
        uri = "/api/capacity_admin/v1/portrait"
        
        requestParam = request
        
        rsp_obj = capacity_admin_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.capacity_admin_sdk",
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
        rsp = capacity_admin_sdk.api.portrait.list_portraits_pb2.ListPortraitsResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_portrait(self, request, org, user, timeout=10):
        # type: (capacity_admin_sdk.api.portrait.update_portrait_pb2.UpdatePortraitRequest, int, str, int) -> capacity_admin_sdk.model.capacity_admin.portrait_pb2.Portrait
        """
        更新容量管理-闲置资源画像
        :param request: update_portrait请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: capacity_admin_sdk.model.capacity_admin.portrait_pb2.Portrait
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.capacity_admin.portrait.UpdatePortrait"
        uri = "/api/capacity_admin/v1/portrait/{portraitId}".format(
            portraitId=request.portraitId,
        )
        requestParam = request
        
        rsp_obj = capacity_admin_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.capacity_admin_sdk",
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
        rsp = capacity_admin_sdk.model.capacity_admin.portrait_pb2.Portrait()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
