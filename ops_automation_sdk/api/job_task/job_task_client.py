# -*- coding: utf-8 -*-
import os
import sys


import ops_automation_sdk.api.job_task.get_job_tasks_details_pb2

import ops_automation_sdk.model.ops_automation.job_tasks_pb2

import ops_automation_sdk.api.job_task.job_tasks_flow_callback_pb2

import ops_automation_sdk.api.job_task.job_tasks_flow_end_callback_pb2

import ops_automation_sdk.api.job_task.job_tasks_tool_callback_pb2

import ops_automation_sdk.api.job_task.list_job_tasks_pb2

import ops_automation_sdk.utils.http_util
import google.protobuf.json_format


class JobTaskClient(object):
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

    
    def get_job_tasks_detail(self, request, org, user, timeout=10):
        # type: (ops_automation_sdk.api.job_task.get_job_tasks_details_pb2.GetJobTasksDetailRequest, int, str, int) -> ops_automation_sdk.model.ops_automation.job_tasks_pb2.JobTasks
        """
        获取作业任务详情
        :param request: get_job_tasks_detail请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: ops_automation_sdk.model.ops_automation.job_tasks_pb2.JobTasks
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.ops_automation.job_task.GetJobTasksDetail"
        uri = "/api/ops_automation/v1/jobTasks/{jobTaskId}".format(
            jobTaskId=request.jobTaskId,
        )
        requestParam = request
        
        rsp_obj = ops_automation_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.ops_automation_sdk",
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
        rsp = ops_automation_sdk.model.ops_automation.job_tasks_pb2.JobTasks()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def job_tasks_flow_callback(self, request, org, user, timeout=10):
        # type: (ops_automation_sdk.api.job_task.job_tasks_flow_callback_pb2.JobTasksFlowCallbackRequest, int, str, int) -> ops_automation_sdk.api.job_task.job_tasks_flow_callback_pb2.JobTasksFlowCallbackResponse
        """
        流程作业任务回调
        :param request: job_tasks_flow_callback请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: ops_automation_sdk.api.job_task.job_tasks_flow_callback_pb2.JobTasksFlowCallbackResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.ops_automation.job_task.JobTasksFlowCallback"
        uri = "/api/ops_automation/v1/jobTasks/flow/callback"
        
        requestParam = request
        
        rsp_obj = ops_automation_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.ops_automation_sdk",
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
        rsp = ops_automation_sdk.api.job_task.job_tasks_flow_callback_pb2.JobTasksFlowCallbackResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def job_tasks_flow_end_callback(self, request, org, user, timeout=10):
        # type: (ops_automation_sdk.api.job_task.job_tasks_flow_end_callback_pb2.JobTasksFlowEndCallbackRequest, int, str, int) -> ops_automation_sdk.api.job_task.job_tasks_flow_end_callback_pb2.JobTasksFlowEndCallbackResponse
        """
        流程作业任务执行完后回调
        :param request: job_tasks_flow_end_callback请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: ops_automation_sdk.api.job_task.job_tasks_flow_end_callback_pb2.JobTasksFlowEndCallbackResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.ops_automation.job_task.JobTasksFlowEndCallback"
        uri = "/api/ops_automation/v1/jobTasks/flow/endCallback"
        
        requestParam = request
        
        rsp_obj = ops_automation_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.ops_automation_sdk",
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
        rsp = ops_automation_sdk.api.job_task.job_tasks_flow_end_callback_pb2.JobTasksFlowEndCallbackResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def job_tasks_tool_callback(self, request, org, user, timeout=10):
        # type: (ops_automation_sdk.api.job_task.job_tasks_tool_callback_pb2.JobTasksToolCallbackRequest, int, str, int) -> ops_automation_sdk.api.job_task.job_tasks_tool_callback_pb2.JobTasksToolCallbackResponse
        """
        工具作业任务回调
        :param request: job_tasks_tool_callback请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: ops_automation_sdk.api.job_task.job_tasks_tool_callback_pb2.JobTasksToolCallbackResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.ops_automation.job_task.JobTasksToolCallback"
        uri = "/api/ops_automation/v1/jobTasks/tool/callback"
        
        requestParam = request
        
        rsp_obj = ops_automation_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.ops_automation_sdk",
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
        rsp = ops_automation_sdk.api.job_task.job_tasks_tool_callback_pb2.JobTasksToolCallbackResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_job_tasks(self, request, org, user, timeout=10):
        # type: (ops_automation_sdk.api.job_task.list_job_tasks_pb2.ListJobTasksRequest, int, str, int) -> ops_automation_sdk.api.job_task.list_job_tasks_pb2.ListJobTasksResponse
        """
        获取作业任务
        :param request: list_job_tasks请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: ops_automation_sdk.api.job_task.list_job_tasks_pb2.ListJobTasksResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.ops_automation.job_task.ListJobTasks"
        uri = "/api/ops_automation/v1/jobTasks"
        
        requestParam = request
        
        rsp_obj = ops_automation_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.ops_automation_sdk",
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
        rsp = ops_automation_sdk.api.job_task.list_job_tasks_pb2.ListJobTasksResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
