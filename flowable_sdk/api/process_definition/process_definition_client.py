# -*- coding: utf-8 -*-
import os
import sys


import flowable_sdk.api.process_definition.get_process_definition_pb2

import flowable_sdk.model.flowable.process_definition_pb2

import flowable_sdk.api.process_definition.get_process_definition_model_pb2

import flowable_sdk.api.process_definition.list_process_definition_pb2

import flowable_sdk.api.process_definition.update_process_definition_pb2

import flowable_sdk.utils.http_util
import google.protobuf.json_format


class ProcessDefinitionClient(object):
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

    
    def get_process_definition(self, request, org, user, timeout=10):
        # type: (flowable_sdk.api.process_definition.get_process_definition_pb2.GetProcessDefinitionRequest, int, str, int) -> flowable_sdk.model.flowable.process_definition_pb2.FlowableProcessDefinition
        """
        获取流程定义详情
        :param request: get_process_definition请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: flowable_sdk.model.flowable.process_definition_pb2.FlowableProcessDefinition
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.flowable.process_definition.GetProcessDefinition"
        uri = "/flowable-rest/service/repository/process-definitions/{definitionId}".format(
            definitionId=request.definitionId,
        )
        requestParam = request
        
        rsp_obj = flowable_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.flowable_sdk",
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
        rsp = flowable_sdk.model.flowable.process_definition_pb2.FlowableProcessDefinition()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_process_definition_model(self, request, org, user, timeout=10):
        # type: (flowable_sdk.api.process_definition.get_process_definition_model_pb2.GetProcessDefinitionModelRequest, int, str, int) -> flowable_sdk.api.process_definition.get_process_definition_model_pb2.GetProcessDefinitionModelResponse
        """
        获取流程定义的模型
        :param request: get_process_definition_model请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: flowable_sdk.api.process_definition.get_process_definition_model_pb2.GetProcessDefinitionModelResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.flowable.process_definition.GetProcessDefinitionModel"
        uri = "/flowable-rest/service/repository/process-definitions/{definitionId}/model".format(
            definitionId=request.definitionId,
        )
        requestParam = request
        
        rsp_obj = flowable_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.flowable_sdk",
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
        rsp = flowable_sdk.api.process_definition.get_process_definition_model_pb2.GetProcessDefinitionModelResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_process_definition(self, request, org, user, timeout=10):
        # type: (flowable_sdk.api.process_definition.list_process_definition_pb2.ListProcessDefinitionRequest, int, str, int) -> flowable_sdk.api.process_definition.list_process_definition_pb2.ListProcessDefinitionResponse
        """
        搜索流程定义列表
        :param request: list_process_definition请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: flowable_sdk.api.process_definition.list_process_definition_pb2.ListProcessDefinitionResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.flowable.process_definition.ListProcessDefinition"
        uri = "/flowable-rest/service/repository/process-definitions"
        
        requestParam = request
        
        rsp_obj = flowable_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.flowable_sdk",
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
        rsp = flowable_sdk.api.process_definition.list_process_definition_pb2.ListProcessDefinitionResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_process_definition(self, request, org, user, timeout=10):
        # type: (flowable_sdk.api.process_definition.update_process_definition_pb2.UpdateProcessDefinitionRequest, int, str, int) -> flowable_sdk.model.flowable.process_definition_pb2.FlowableProcessDefinition
        """
        更新流程定义详情
        :param request: update_process_definition请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: flowable_sdk.model.flowable.process_definition_pb2.FlowableProcessDefinition
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.flowable.process_definition.UpdateProcessDefinition"
        uri = "/flowable-rest/service/repository/process-definitions/{definitionId}".format(
            definitionId=request.definitionId,
        )
        requestParam = request
        
        rsp_obj = flowable_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.flowable_sdk",
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
        rsp = flowable_sdk.model.flowable.process_definition_pb2.FlowableProcessDefinition()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
