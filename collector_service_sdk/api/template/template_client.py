# -*- coding: utf-8 -*-
import os
import sys


import collector_service_sdk.api.template.create_template_with_yaml_pb2

import collector_service_sdk.model.collector_service.collector_template_pb2

import collector_service_sdk.api.template.delete_template_pb2

import collector_service_sdk.api.template.detail_template_pb2

import collector_service_sdk.api.template.update_template_with_yaml_pb2

import collector_service_sdk.api.template.valid_template_yaml_pb2

import collector_service_sdk.utils.http_util
import google.protobuf.json_format


class TemplateClient(object):
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

    
    def create_collector_template_with_yaml(self, request, org, user, timeout=10):
        # type: (collector_service_sdk.api.template.create_template_with_yaml_pb2.CreateCollectorTemplateWithYamlRequest, int, str, int) -> collector_service_sdk.model.collector_service.collector_template_pb2.CollectorTemplate
        """
        创建采集模版
        :param request: create_collector_template_with_yaml请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: collector_service_sdk.model.collector_service.collector_template_pb2.CollectorTemplate
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.collector_service.template.CreateCollectorTemplateWithYaml"
        uri = "/api/v1/collector-template"
        
        requestParam = request
        
        rsp_obj = collector_service_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.collector_service_sdk",
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
        rsp = collector_service_sdk.model.collector_service.collector_template_pb2.CollectorTemplate()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_collector_template(self, request, org, user, timeout=10):
        # type: (collector_service_sdk.api.template.delete_template_pb2.DeleteCollectorTemplateRequest, int, str, int) -> collector_service_sdk.api.template.delete_template_pb2.DeleteCollectorTemplateResponse
        """
        删除采集模版
        :param request: delete_collector_template请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: collector_service_sdk.api.template.delete_template_pb2.DeleteCollectorTemplateResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.collector_service.template.DeleteCollectorTemplate"
        uri = "/api/v1/collector-template/{instanceId}".format(
            instanceId=request.instanceId,
        )
        requestParam = request
        
        rsp_obj = collector_service_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.collector_service_sdk",
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
        rsp = collector_service_sdk.api.template.delete_template_pb2.DeleteCollectorTemplateResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def detail_collector_template(self, request, org, user, timeout=10):
        # type: (collector_service_sdk.api.template.detail_template_pb2.DetailCollectorTemplateRequest, int, str, int) -> collector_service_sdk.api.template.detail_template_pb2.DetailCollectorTemplateResponse
        """
        获取采集模版详情
        :param request: detail_collector_template请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: collector_service_sdk.api.template.detail_template_pb2.DetailCollectorTemplateResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.collector_service.template.DetailCollectorTemplate"
        uri = "/api/v1/collector-template/{instanceId}".format(
            instanceId=request.instanceId,
        )
        requestParam = request
        
        rsp_obj = collector_service_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.collector_service_sdk",
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
        rsp = collector_service_sdk.api.template.detail_template_pb2.DetailCollectorTemplateResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_collector_template_with_yaml(self, request, org, user, timeout=10):
        # type: (collector_service_sdk.api.template.update_template_with_yaml_pb2.UpdateCollectorTemplateWithYamlRequest, int, str, int) -> collector_service_sdk.model.collector_service.collector_template_pb2.CollectorTemplate
        """
        更新采集模版
        :param request: update_collector_template_with_yaml请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: collector_service_sdk.model.collector_service.collector_template_pb2.CollectorTemplate
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.collector_service.template.UpdateCollectorTemplateWithYaml"
        uri = "/api/v1/collector-template/{instanceId}".format(
            instanceId=request.instanceId,
        )
        requestParam = request
        
        rsp_obj = collector_service_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.collector_service_sdk",
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
        rsp = collector_service_sdk.model.collector_service.collector_template_pb2.CollectorTemplate()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def valid_template_yaml(self, request, org, user, timeout=10):
        # type: (collector_service_sdk.api.template.valid_template_yaml_pb2.ValidTemplateYamlRequest, int, str, int) -> collector_service_sdk.api.template.valid_template_yaml_pb2.ValidTemplateYamlResponse
        """
        校验采集模版yaml
        :param request: valid_template_yaml请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: collector_service_sdk.api.template.valid_template_yaml_pb2.ValidTemplateYamlResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.collector_service.template.ValidTemplateYaml"
        uri = "/api/v1/collector-template/valid"
        
        requestParam = request
        
        rsp_obj = collector_service_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.collector_service_sdk",
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
        rsp = collector_service_sdk.api.template.valid_template_yaml_pb2.ValidTemplateYamlResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
