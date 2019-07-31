# -*- coding: utf-8 -*-
import os
import sys

current_path = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = os.path.dirname(os.path.dirname(current_path))
if PROJECT_PATH not in sys.path:
    sys.path.append(PROJECT_PATH)


import create_org_pb2

import disable_org_pb2

import google.protobuf.empty_pb2

import enable_org_pb2

import list_org_pb2

import set_org_expires_pb2

import utils.http_util
import google.protobuf.json_format


class OrganizationClient(object):
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

    
    def create_org(self, request, org, user, timeout=10):
        # type: (create_org_pb2.CreateOrgRequest, int, str, int) -> create_org_pb2.CreateOrgResponse
        """
        创建Org[内部]
        :param request: create_org请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: create_org_pb2.CreateOrgResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.user_service.organization.CreateOrg"
        uri = "/api/v1/org"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.user_service_sdk",
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
        rsp = create_org_pb2.CreateOrgResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def disable_org(self, request, org, user, timeout=10):
        # type: (disable_org_pb2.DisableOrgRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        禁用Org[内部]
        :param request: disable_org请求
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
            route_name = "easyops.api.user_service.organization.DisableOrg"
        uri = "/api/v1/org/{id}/disable".format(
            id=request.id,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.user_service_sdk",
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
    
    def enable_org(self, request, org, user, timeout=10):
        # type: (enable_org_pb2.EnableOrgRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        启用Org[内部]
        :param request: enable_org请求
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
            route_name = "easyops.api.user_service.organization.EnableOrg"
        uri = "/api/v1/org/{id}/enable".format(
            id=request.id,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.user_service_sdk",
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
    
    def list_org(self, request, org, user, timeout=10):
        # type: (google.protobuf.empty_pb2.Empty, int, str, int) -> list_org_pb2.ListOrgResponse
        """
        获取所有Org[内部]
        :param request: list_org请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: list_org_pb2.ListOrgResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.user_service.organization.ListOrg"
        uri = "/api/v1/org/list"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="GET",
            src_name="logic.user_service_sdk",
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
        rsp = list_org_pb2.ListOrgResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def set_org_expired_date(self, request, org, user, timeout=10):
        # type: (set_org_expires_pb2.SetOrgExpiredDateRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        设置Org过期日期[内部]
        :param request: set_org_expired_date请求
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
            route_name = "easyops.api.user_service.organization.SetOrgExpiredDate"
        uri = "/api/v1/org/{id}/_expired_date".format(
            id=request.id,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.user_service_sdk",
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
    
