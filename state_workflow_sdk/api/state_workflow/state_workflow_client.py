# -*- coding: utf-8 -*-
import os
import sys


import state_workflow_sdk.api.state_workflow.callback_pb2

import state_workflow_sdk.api.state_workflow.createStateWorkflow_pb2

import state_workflow_sdk.model.state_workflow.stateWorkflow_pb2

import state_workflow_sdk.api.state_workflow.deleteStateWorkflow_pb2

import google.protobuf.empty_pb2

import state_workflow_sdk.api.state_workflow.filterInstanceOfStateWorkflow_pb2

import state_workflow_sdk.api.state_workflow.searchStateWorkflow_pb2

import state_workflow_sdk.api.state_workflow.transitWorkflowStatus_pb2

import state_workflow_sdk.utils.http_util
import google.protobuf.json_format


class StateWorkflowClient(object):
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

    
    def callback_state_workflow(self, request, org, user, timeout=10):
        # type: (state_workflow_sdk.api.state_workflow.callback_pb2.CallbackStateWorkflowRequest, int, str, int) -> state_workflow_sdk.api.state_workflow.callback_pb2.CallbackStateWorkflowResponse
        """
        状态工作流执行回调
        :param request: callback_state_workflow请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: state_workflow_sdk.api.state_workflow.callback_pb2.CallbackStateWorkflowResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.state_workflow.state_workflow.CallbackStateWorkflow"
        uri = "/api/v1/stateWorkflow/callback"
        
        requestParam = request
        
        rsp_obj = state_workflow_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.state_workflow_sdk",
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
        rsp = state_workflow_sdk.api.state_workflow.callback_pb2.CallbackStateWorkflowResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def create_state_workflow(self, request, org, user, timeout=10):
        # type: (state_workflow_sdk.api.state_workflow.createStateWorkflow_pb2.CreateStateWorkflowRequest, int, str, int) -> state_workflow_sdk.model.state_workflow.stateWorkflow_pb2.StateWorkflow
        """
        创建状态工作流
        :param request: create_state_workflow请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: state_workflow_sdk.model.state_workflow.stateWorkflow_pb2.StateWorkflow
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.state_workflow.state_workflow.CreateStateWorkflow"
        uri = "/api/v1/stateWorkflow"
        
        requestParam = request
        
        rsp_obj = state_workflow_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.state_workflow_sdk",
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
        rsp = state_workflow_sdk.model.state_workflow.stateWorkflow_pb2.StateWorkflow()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_state_workflow(self, request, org, user, timeout=10):
        # type: (state_workflow_sdk.api.state_workflow.deleteStateWorkflow_pb2.DeleteStateWorkflowRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        删除状态工作流
        :param request: delete_state_workflow请求
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
            route_name = "easyops.api.state_workflow.state_workflow.DeleteStateWorkflow"
        uri = "/api/v1/stateWorkflow/{instanceId}".format(
            instanceId=request.instanceId,
        )
        requestParam = request
        
        rsp_obj = state_workflow_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.state_workflow_sdk",
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
    
    def filter_instance_of_state_workflow(self, request, org, user, timeout=10):
        # type: (state_workflow_sdk.api.state_workflow.filterInstanceOfStateWorkflow_pb2.FilterInstanceOfStateWorkflowRequest, int, str, int) -> state_workflow_sdk.api.state_workflow.filterInstanceOfStateWorkflow_pb2.FilterInstanceOfStateWorkflowResponse
        """
        按工作流filter过滤实例
        :param request: filter_instance_of_state_workflow请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: state_workflow_sdk.api.state_workflow.filterInstanceOfStateWorkflow_pb2.FilterInstanceOfStateWorkflowResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.state_workflow.state_workflow.FilterInstanceOfStateWorkflow"
        uri = "/api/v1/stateWorkflow/instance/filter"
        
        requestParam = request
        
        rsp_obj = state_workflow_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.state_workflow_sdk",
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
        rsp = state_workflow_sdk.api.state_workflow.filterInstanceOfStateWorkflow_pb2.FilterInstanceOfStateWorkflowResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def search_state_workflow(self, request, org, user, timeout=10):
        # type: (state_workflow_sdk.api.state_workflow.searchStateWorkflow_pb2.SearchStateWorkflowRequest, int, str, int) -> state_workflow_sdk.model.state_workflow.stateWorkflow_pb2.StateWorkflow
        """
        搜索状态工作流
        :param request: search_state_workflow请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: state_workflow_sdk.model.state_workflow.stateWorkflow_pb2.StateWorkflow
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.state_workflow.state_workflow.SearchStateWorkflow"
        uri = "/api/v1/stateWorkflow/_search"
        
        requestParam = request
        
        rsp_obj = state_workflow_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.state_workflow_sdk",
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
        rsp = state_workflow_sdk.model.state_workflow.stateWorkflow_pb2.StateWorkflow()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def transit_state_workflow_status(self, request, org, user, timeout=10):
        # type: (state_workflow_sdk.api.state_workflow.transitWorkflowStatus_pb2.TransitStateWorkflowStatusRequest, int, str, int) -> state_workflow_sdk.api.state_workflow.transitWorkflowStatus_pb2.TransitStateWorkflowStatusResponse
        """
        实例属性状态切换
        :param request: transit_state_workflow_status请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: state_workflow_sdk.api.state_workflow.transitWorkflowStatus_pb2.TransitStateWorkflowStatusResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.state_workflow.state_workflow.TransitStateWorkflowStatus"
        uri = "/api/v1/stateWorkflow/transit"
        
        requestParam = request
        
        rsp_obj = state_workflow_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.state_workflow_sdk",
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
        rsp = state_workflow_sdk.api.state_workflow.transitWorkflowStatus_pb2.TransitStateWorkflowStatusResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
