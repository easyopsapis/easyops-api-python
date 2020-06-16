# -*- coding: utf-8 -*-
import os
import sys


import terraform_sdk.api.backend.delete_state_pb2

import google.protobuf.empty_pb2

import terraform_sdk.api.backend.get_state_pb2

import google.protobuf.struct_pb2

import terraform_sdk.api.backend.lock_state_pb2

import terraform_sdk.api.backend.unlock_state_pb2

import terraform_sdk.api.backend.update_state_pb2

import terraform_sdk.utils.http_util
import google.protobuf.json_format


class BackendClient(object):
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

    
    def delete_state(self, request, org, user, timeout=10):
        # type: (terraform_sdk.api.backend.delete_state_pb2.DeleteStateRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        删除state
        :param request: delete_state请求
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
            route_name = "easyops.api.terraform.backend.DeleteState"
        uri = "/api/terraform/v1/state/org/{org}/tfId/{tfId}".format(
            org=request.org,
            tfId=request.tfId,
        )
        requestParam = request
        
        rsp_obj = terraform_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.terraform_sdk",
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
    
    def get_state(self, request, org, user, timeout=10):
        # type: (terraform_sdk.api.backend.get_state_pb2.GetStateRequest, int, str, int) -> google.protobuf.struct_pb2.Struct
        """
        获取state
        :param request: get_state请求
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
            route_name = "easyops.api.terraform.backend.GetState"
        uri = "/api/terraform/v1/state/org/{org}/tfId/{tfId}".format(
            org=request.org,
            tfId=request.tfId,
        )
        requestParam = request
        
        rsp_obj = terraform_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.terraform_sdk",
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
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def lock_state(self, request, org, user, timeout=10):
        # type: (terraform_sdk.api.backend.lock_state_pb2.LockStateRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        锁定工作区
        :param request: lock_state请求
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
            route_name = "easyops.api.terraform.backend.LockState"
        uri = "/api/terraform/v1/state/org/{org}/tfId/{tfId}/lock".format(
            org=request.org,
            tfId=request.tfId,
        )
        requestParam = request.body
        
        rsp_obj = terraform_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.terraform_sdk",
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
    
    def un_lock_state(self, request, org, user, timeout=10):
        # type: (terraform_sdk.api.backend.unlock_state_pb2.UnLockStateRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        解锁工作区
        :param request: un_lock_state请求
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
            route_name = "easyops.api.terraform.backend.UnLockState"
        uri = "/api/terraform/v1/state/org/{org}/tfId/{tfId}/unlock".format(
            org=request.org,
            tfId=request.tfId,
        )
        requestParam = request.body
        
        rsp_obj = terraform_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.terraform_sdk",
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
    
    def update_state(self, request, org, user, timeout=10):
        # type: (terraform_sdk.api.backend.update_state_pb2.UpdateStateRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        更新state
        :param request: update_state请求
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
            route_name = "easyops.api.terraform.backend.UpdateState"
        uri = "/api/terraform/v1/state/org/{org}/tfId/{tfId}".format(
            org=request.org,
            tfId=request.tfId,
        )
        requestParam = request.body
        
        rsp_obj = terraform_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.terraform_sdk",
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
    
