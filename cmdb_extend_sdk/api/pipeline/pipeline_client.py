# -*- coding: utf-8 -*-
import os
import sys


import cmdb_extend_sdk.api.pipeline.bind_pipeline_pb2

import cmdb_extend_sdk.model.cmdb_extend.app_pipeline_pb2

import cmdb_extend_sdk.api.pipeline.get_pipeline_pb2

import cmdb_extend_sdk.api.pipeline.get_pipelines_pb2

import cmdb_extend_sdk.api.pipeline.modify_pipeline_pb2

import cmdb_extend_sdk.api.pipeline.unbind_pipeline_pb2

import cmdb_extend_sdk.utils.http_util
import google.protobuf.json_format


class PipelineClient(object):
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

    
    def bind_pipeline(self, request, org, user, timeout=10):
        # type: (cmdb_extend_sdk.api.pipeline.bind_pipeline_pb2.BindPipelineRequest, int, str, int) -> cmdb_extend_sdk.model.cmdb_extend.app_pipeline_pb2.AppPipeline
        """
        绑定流水线
        :param request: bind_pipeline请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_extend_sdk.model.cmdb_extend.app_pipeline_pb2.AppPipeline
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb_extend.pipeline.BindPipeline"
        uri = "/application/{appId}/pipeline".format(
            appId=request.appId,
        )
        requestParam = request.pipeline
        
        rsp_obj = cmdb_extend_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.cmdb_extend_sdk",
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
        rsp = cmdb_extend_sdk.model.cmdb_extend.app_pipeline_pb2.AppPipeline()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_pipeline(self, request, org, user, timeout=10):
        # type: (cmdb_extend_sdk.api.pipeline.get_pipeline_pb2.GetPipelineRequest, int, str, int) -> cmdb_extend_sdk.model.cmdb_extend.app_pipeline_pb2.AppPipeline
        """
        获取指定流水线
        :param request: get_pipeline请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_extend_sdk.model.cmdb_extend.app_pipeline_pb2.AppPipeline
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb_extend.pipeline.GetPipeline"
        uri = "/application/{appId}/pipeline/{flowId}".format(
            appId=request.appId,
            flowId=request.flowId,
        )
        requestParam = request
        
        rsp_obj = cmdb_extend_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.cmdb_extend_sdk",
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
        rsp = cmdb_extend_sdk.model.cmdb_extend.app_pipeline_pb2.AppPipeline()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_pipelines(self, request, org, user, timeout=10):
        # type: (cmdb_extend_sdk.api.pipeline.get_pipelines_pb2.GetPipelinesRequest, int, str, int) -> cmdb_extend_sdk.api.pipeline.get_pipelines_pb2.GetPipelinesResponse
        """
        获取流水线列表
        :param request: get_pipelines请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_extend_sdk.api.pipeline.get_pipelines_pb2.GetPipelinesResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb_extend.pipeline.GetPipelines"
        uri = "/application/{appId}/pipeline".format(
            appId=request.appId,
        )
        requestParam = request
        
        rsp_obj = cmdb_extend_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.cmdb_extend_sdk",
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
        rsp = cmdb_extend_sdk.api.pipeline.get_pipelines_pb2.GetPipelinesResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def modify_pipeline(self, request, org, user, timeout=10):
        # type: (cmdb_extend_sdk.api.pipeline.modify_pipeline_pb2.ModifyPipelineRequest, int, str, int) -> cmdb_extend_sdk.model.cmdb_extend.app_pipeline_pb2.AppPipeline
        """
        修改流水线
        :param request: modify_pipeline请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_extend_sdk.model.cmdb_extend.app_pipeline_pb2.AppPipeline
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb_extend.pipeline.ModifyPipeline"
        uri = "/application/{appId}/pipeline/{flowId}".format(
            appId=request.appId,
            flowId=request.flowId,
        )
        requestParam = request.pipeline
        
        rsp_obj = cmdb_extend_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.cmdb_extend_sdk",
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
        rsp = cmdb_extend_sdk.model.cmdb_extend.app_pipeline_pb2.AppPipeline()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def un_bind_pipeline(self, request, org, user, timeout=10):
        # type: (cmdb_extend_sdk.api.pipeline.unbind_pipeline_pb2.UnBindPipelineRequest, int, str, int) -> cmdb_extend_sdk.model.cmdb_extend.app_pipeline_pb2.AppPipeline
        """
        解绑流水线
        :param request: un_bind_pipeline请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_extend_sdk.model.cmdb_extend.app_pipeline_pb2.AppPipeline
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb_extend.pipeline.UnBindPipeline"
        uri = "/application/{appId}/pipeline/{flowId}".format(
            appId=request.appId,
            flowId=request.flowId,
        )
        requestParam = request
        
        rsp_obj = cmdb_extend_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.cmdb_extend_sdk",
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
        rsp = cmdb_extend_sdk.model.cmdb_extend.app_pipeline_pb2.AppPipeline()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
