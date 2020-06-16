# -*- coding: utf-8 -*-
import os
import sys


import pipeline_sdk.model.pipeline.template_pb2

import pipeline_sdk.api.template.delete_pb2

import google.protobuf.empty_pb2

import pipeline_sdk.api.template.get_pb2

import pipeline_sdk.api.template.list_pb2

import pipeline_sdk.api.template.update_pb2

import pipeline_sdk.utils.http_util
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

    
    def create(self, request, org, user, timeout=10):
        # type: (pipeline_sdk.model.pipeline.template_pb2.Template, int, str, int) -> pipeline_sdk.model.pipeline.template_pb2.Template
        """
        创建模版
        :param request: create请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: pipeline_sdk.model.pipeline.template_pb2.Template
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.pipeline.template.Create"
        uri = "/api/pipeline/v1/templates"
        
        requestParam = request
        
        rsp_obj = pipeline_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.pipeline_sdk",
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
        rsp = pipeline_sdk.model.pipeline.template_pb2.Template()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_template(self, request, org, user, timeout=10):
        # type: (pipeline_sdk.api.template.delete_pb2.DeleteTemplateRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        删除模版
        :param request: delete_template请求
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
            route_name = "easyops.api.pipeline.template.DeleteTemplate"
        uri = "/api/pipeline/v1/templates/{id}".format(
            id=request.id,
        )
        requestParam = request
        
        rsp_obj = pipeline_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.pipeline_sdk",
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
    
    def get(self, request, org, user, timeout=10):
        # type: (pipeline_sdk.api.template.get_pb2.GetRequest, int, str, int) -> pipeline_sdk.api.template.get_pb2.GetResponse
        """
        获取模版详情
        :param request: get请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: pipeline_sdk.api.template.get_pb2.GetResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.pipeline.template.Get"
        uri = "/api/pipeline/v1/templates/{id}".format(
            id=request.id,
        )
        requestParam = request
        
        rsp_obj = pipeline_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.pipeline_sdk",
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
        rsp = pipeline_sdk.api.template.get_pb2.GetResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list(self, request, org, user, timeout=10):
        # type: (pipeline_sdk.api.template.list_pb2.ListRequest, int, str, int) -> pipeline_sdk.api.template.list_pb2.ListResponse
        """
        获取模版列表
        :param request: list请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: pipeline_sdk.api.template.list_pb2.ListResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.pipeline.template.List"
        uri = "/api/pipeline/v1/templates"
        
        requestParam = request
        
        rsp_obj = pipeline_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.pipeline_sdk",
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
        rsp = pipeline_sdk.api.template.list_pb2.ListResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update(self, request, org, user, timeout=10):
        # type: (pipeline_sdk.api.template.update_pb2.UpdateRequest, int, str, int) -> pipeline_sdk.model.pipeline.template_pb2.Template
        """
        更新模版信息
        :param request: update请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: pipeline_sdk.model.pipeline.template_pb2.Template
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.pipeline.template.Update"
        uri = "/api/pipeline/v1/templates/{id}".format(
            id=request.id,
        )
        requestParam = request
        
        rsp_obj = pipeline_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.pipeline_sdk",
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
        rsp = pipeline_sdk.model.pipeline.template_pb2.Template()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
