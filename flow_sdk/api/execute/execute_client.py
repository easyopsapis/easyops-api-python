# -*- coding: utf-8 -*-
import os
import sys

current_path = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = os.path.dirname(os.path.dirname(current_path))
if PROJECT_PATH not in sys.path:
    sys.path.append(PROJECT_PATH)


import execute_pb2

import get_flow_result_pb2

import model.flow.flow_instance_pb2

import retry_pb2

import utils.http_util
import google.protobuf.json_format


class ExecuteClient(object):
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

    
    def execute_flow(self, request, org, user, timeout=10):
        # type: (execute_pb2.ExecuteFlowRequest, int, str, int) -> execute_pb2.ExecuteFlowResponse
        """
        执行流程
        :param request: execute_flow请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: execute_pb2.ExecuteFlowResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.flow.execute.ExecuteFlow"
        uri = "/flows/execution"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.flow_sdk",
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
        rsp = execute_pb2.ExecuteFlowResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_flow_result(self, request, org, user, timeout=10):
        # type: (get_flow_result_pb2.GetFlowResultRequest, int, str, int) -> model.flow.flow_instance_pb2.FlowInstance
        """
        获取流程执行结果
        :param request: get_flow_result请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: model.flow.flow_instance_pb2.FlowInstance
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.flow.execute.GetFlowResult"
        uri = "/flows/execution/{taskId}".format(
            taskId=request.taskId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="GET",
            src_name="logic.flow_sdk",
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
        rsp = model.flow.flow_instance_pb2.FlowInstance()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def retry_step(self, request, org, user, timeout=10):
        # type: (retry_pb2.RetryStepRequest, int, str, int) -> retry_pb2.RetryStepResponse
        """
        重试步骤
        :param request: retry_step请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: retry_pb2.RetryStepResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.flow.execute.RetryStep"
        uri = "/flows/execution/retry/{taskId}/{stepId}".format(
            taskId=request.taskId,
            stepId=request.stepId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.flow_sdk",
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
        rsp = retry_pb2.RetryStepResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
