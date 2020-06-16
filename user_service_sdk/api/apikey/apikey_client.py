# -*- coding: utf-8 -*-
import os
import sys


import user_service_sdk.api.apikey.create_apikey_pb2

import user_service_sdk.api.apikey.delete_apikey_pb2

import google.protobuf.empty_pb2

import user_service_sdk.api.apikey.disable_apikey_pb2

import user_service_sdk.api.apikey.enable_apikey_pb2

import user_service_sdk.api.apikey.get_apikey_pb2

import user_service_sdk.api.apikey.list_apikey_pb2

import user_service_sdk.api.apikey.reset_apikey_pb2

import user_service_sdk.utils.http_util
import google.protobuf.json_format


class ApikeyClient(object):
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

    
    def create_api_key(self, request, org, user, timeout=10):
        # type: (user_service_sdk.api.apikey.create_apikey_pb2.CreateApiKeyRequest, int, str, int) -> user_service_sdk.api.apikey.create_apikey_pb2.CreateApiKeyResponse
        """
        创建用户ApiKey[内部]
        :param request: create_api_key请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: user_service_sdk.api.apikey.create_apikey_pb2.CreateApiKeyResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.user_service.apikey.CreateApiKey"
        uri = "/api/v1/apikey/{user}".format(
            user=request.user,
        )
        requestParam = request
        
        rsp_obj = user_service_sdk.utils.http_util.do_api_request(
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
        rsp = user_service_sdk.api.apikey.create_apikey_pb2.CreateApiKeyResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_api_key(self, request, org, user, timeout=10):
        # type: (user_service_sdk.api.apikey.delete_apikey_pb2.DeleteApiKeyRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        删除用户ApiKey[内部]
        :param request: delete_api_key请求
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
            route_name = "easyops.api.user_service.apikey.DeleteApiKey"
        uri = "/api/v1/apikey/delete/{access_key}".format(
            access_key=request.access_key,
        )
        requestParam = request
        
        rsp_obj = user_service_sdk.utils.http_util.do_api_request(
            method="DELETE",
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
    
    def disable_api_key(self, request, org, user, timeout=10):
        # type: (user_service_sdk.api.apikey.disable_apikey_pb2.DisableApiKeyRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        禁用用户ApiKey[内部]
        :param request: disable_api_key请求
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
            route_name = "easyops.api.user_service.apikey.DisableApiKey"
        uri = "/api/v1/apikey/disable/{access_key}".format(
            access_key=request.access_key,
        )
        requestParam = request
        
        rsp_obj = user_service_sdk.utils.http_util.do_api_request(
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
    
    def enable_api_key(self, request, org, user, timeout=10):
        # type: (user_service_sdk.api.apikey.enable_apikey_pb2.EnableApiKeyRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        启用用户ApiKey[内部]
        :param request: enable_api_key请求
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
            route_name = "easyops.api.user_service.apikey.EnableApiKey"
        uri = "/api/v1/apikey/enable/{access_key}".format(
            access_key=request.access_key,
        )
        requestParam = request
        
        rsp_obj = user_service_sdk.utils.http_util.do_api_request(
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
    
    def get_api_key(self, request, org, user, timeout=10):
        # type: (google.protobuf.empty_pb2.Empty, int, str, int) -> user_service_sdk.api.apikey.get_apikey_pb2.GetApiKeyResponse
        """
        查询个人apikey
        :param request: get_api_key请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: user_service_sdk.api.apikey.get_apikey_pb2.GetApiKeyResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.user_service.apikey.GetApiKey"
        uri = "/profile/apikey"
        
        requestParam = request
        
        rsp_obj = user_service_sdk.utils.http_util.do_api_request(
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
        rsp = user_service_sdk.api.apikey.get_apikey_pb2.GetApiKeyResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_api_key(self, request, org, user, timeout=10):
        # type: (user_service_sdk.api.apikey.list_apikey_pb2.ListApiKeyRequest, int, str, int) -> user_service_sdk.api.apikey.list_apikey_pb2.ListApiKeyResponse
        """
        获取用户ApiKey[内部]
        :param request: list_api_key请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: user_service_sdk.api.apikey.list_apikey_pb2.ListApiKeyResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.user_service.apikey.ListApiKey"
        uri = "/api/v1/apikey"
        
        requestParam = request
        
        rsp_obj = user_service_sdk.utils.http_util.do_api_request(
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
        rsp = user_service_sdk.api.apikey.list_apikey_pb2.ListApiKeyResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def reset_api_key(self, request, org, user, timeout=10):
        # type: (user_service_sdk.api.apikey.reset_apikey_pb2.ResetApiKeyRequest, int, str, int) -> user_service_sdk.api.apikey.reset_apikey_pb2.ResetApiKeyResponse
        """
        重置用户ApiKey[内部]
        :param request: reset_api_key请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: user_service_sdk.api.apikey.reset_apikey_pb2.ResetApiKeyResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.user_service.apikey.ResetApiKey"
        uri = "/api/v1/apikey/_reset/{user}".format(
            user=request.user,
        )
        requestParam = request
        
        rsp_obj = user_service_sdk.utils.http_util.do_api_request(
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
        rsp = user_service_sdk.api.apikey.reset_apikey_pb2.ResetApiKeyResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
