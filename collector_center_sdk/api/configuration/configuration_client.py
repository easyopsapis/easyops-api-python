# -*- coding: utf-8 -*-
import os
import sys


import collector_center_sdk.api.configuration.create_configuration_pb2

import collector_center_sdk.api.configuration.delete_configuration_pb2

import collector_center_sdk.api.configuration.detail_configuration_pb2

import collector_center_sdk.model.collector_center.configuration_pb2

import collector_center_sdk.api.configuration.list_configuration_pb2

import collector_center_sdk.api.configuration.update_configuration_pb2

import collector_center_sdk.utils.http_util
import google.protobuf.json_format


class ConfigurationClient(object):
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

    
    def create_configuration(self, request, org, user, timeout=10):
        # type: (collector_center_sdk.api.configuration.create_configuration_pb2.CreateConfigurationRequest, int, str, int) -> collector_center_sdk.api.configuration.create_configuration_pb2.CreateConfigurationResponse
        """
        创建采集配置
        :param request: create_configuration请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: collector_center_sdk.api.configuration.create_configuration_pb2.CreateConfigurationResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.collector_center.configuration.CreateConfiguration"
        uri = "/api/v1/configuration"
        
        requestParam = request
        
        rsp_obj = collector_center_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.collector_center_sdk",
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
        rsp = collector_center_sdk.api.configuration.create_configuration_pb2.CreateConfigurationResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_configuration(self, request, org, user, timeout=10):
        # type: (collector_center_sdk.api.configuration.delete_configuration_pb2.DeleteConfigurationRequest, int, str, int) -> collector_center_sdk.api.configuration.delete_configuration_pb2.DeleteConfigurationResponse
        """
        删除采集配置
        :param request: delete_configuration请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: collector_center_sdk.api.configuration.delete_configuration_pb2.DeleteConfigurationResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.collector_center.configuration.DeleteConfiguration"
        uri = "/api/v1/configuration/{id}".format(
            id=request.id,
        )
        requestParam = request
        
        rsp_obj = collector_center_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.collector_center_sdk",
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
        rsp = collector_center_sdk.api.configuration.delete_configuration_pb2.DeleteConfigurationResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def detail_configuration(self, request, org, user, timeout=10):
        # type: (collector_center_sdk.api.configuration.detail_configuration_pb2.DetailConfigurationRequest, int, str, int) -> collector_center_sdk.model.collector_center.configuration_pb2.Configuration
        """
        查看采集配置
        :param request: detail_configuration请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: collector_center_sdk.model.collector_center.configuration_pb2.Configuration
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.collector_center.configuration.DetailConfiguration"
        uri = "/api/v1/configuration/{id}".format(
            id=request.id,
        )
        requestParam = request
        
        rsp_obj = collector_center_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.collector_center_sdk",
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
        rsp = collector_center_sdk.model.collector_center.configuration_pb2.Configuration()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_configuration(self, request, org, user, timeout=10):
        # type: (collector_center_sdk.api.configuration.list_configuration_pb2.ListConfigurationRequest, int, str, int) -> collector_center_sdk.api.configuration.list_configuration_pb2.ListConfigurationResponse
        """
        查看采集配置列表
        :param request: list_configuration请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: collector_center_sdk.api.configuration.list_configuration_pb2.ListConfigurationResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.collector_center.configuration.ListConfiguration"
        uri = "/api/v1/configuration"
        
        requestParam = request
        
        rsp_obj = collector_center_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.collector_center_sdk",
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
        rsp = collector_center_sdk.api.configuration.list_configuration_pb2.ListConfigurationResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_configuration(self, request, org, user, timeout=10):
        # type: (collector_center_sdk.api.configuration.update_configuration_pb2.UpdateConfigurationRequest, int, str, int) -> collector_center_sdk.api.configuration.update_configuration_pb2.UpdateConfigurationResponse
        """
        更新采集配置
        :param request: update_configuration请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: collector_center_sdk.api.configuration.update_configuration_pb2.UpdateConfigurationResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.collector_center.configuration.UpdateConfiguration"
        uri = "/api/v1/configuration/{id}".format(
            id=request.id,
        )
        requestParam = request
        
        rsp_obj = collector_center_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.collector_center_sdk",
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
        rsp = collector_center_sdk.api.configuration.update_configuration_pb2.UpdateConfigurationResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
