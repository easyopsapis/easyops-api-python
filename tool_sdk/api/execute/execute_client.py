# -*- coding: utf-8 -*-
import os
import sys


import tool_sdk.api.execute.execute_debug_tool_pb2

import tool_sdk.api.execute.execute_tool_pb2

import tool_sdk.api.execute.get_execute_result_pb2

import tool_sdk.model.tool.tool_task_pb2

import tool_sdk.api.execute.get_tool_execution_logs_pb2

import tool_sdk.api.execute.get_tool_execution_table_result_pb2

import tool_sdk.api.execute.list_tool_execution_result_pb2

import tool_sdk.api.execute.terminate_task_pb2

import tool_sdk.api.execute.tool_debug_snapshot_pb2

import tool_sdk.model.tool.execution_snapshot_pb2

import tool_sdk.api.execute.tool_execution_snapshot_pb2

import tool_sdk.api.execute.tool_executon_callback_pb2

import tool_sdk.utils.http_util
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

    
    def execute_debug_tool(self, request, org, user, timeout=10):
        # type: (tool_sdk.api.execute.execute_debug_tool_pb2.ExecuteDebugToolRequest, int, str, int) -> tool_sdk.api.execute.execute_debug_tool_pb2.ExecuteDebugToolResponse
        """
        调试工具的执行
        :param request: execute_debug_tool请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: tool_sdk.api.execute.execute_debug_tool_pb2.ExecuteDebugToolResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.tool.execute.ExecuteDebugTool"
        uri = "/tools/debug"
        
        requestParam = request
        
        rsp_obj = tool_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.tool_sdk",
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
        rsp = tool_sdk.api.execute.execute_debug_tool_pb2.ExecuteDebugToolResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def execute_tool(self, request, org, user, timeout=10):
        # type: (tool_sdk.api.execute.execute_tool_pb2.ExecuteToolRequest, int, str, int) -> tool_sdk.api.execute.execute_tool_pb2.ExecuteToolResponse
        """
        执行工具
        :param request: execute_tool请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: tool_sdk.api.execute.execute_tool_pb2.ExecuteToolResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.tool.execute.ExecuteTool"
        uri = "/tools/execution"
        
        requestParam = request
        
        rsp_obj = tool_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.tool_sdk",
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
        rsp = tool_sdk.api.execute.execute_tool_pb2.ExecuteToolResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_execute_result(self, request, org, user, timeout=10):
        # type: (tool_sdk.api.execute.get_execute_result_pb2.GetExecuteResultRequest, int, str, int) -> tool_sdk.model.tool.tool_task_pb2.ToolTask
        """
        获取工具执行结果
        :param request: get_execute_result请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: tool_sdk.model.tool.tool_task_pb2.ToolTask
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.tool.execute.GetExecuteResult"
        uri = "/tools/execution/{execId}".format(
            execId=request.execId,
        )
        requestParam = request
        
        rsp_obj = tool_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.tool_sdk",
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
        rsp = tool_sdk.model.tool.tool_task_pb2.ToolTask()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_tool_execution_logs(self, request, org, user, timeout=10):
        # type: (tool_sdk.api.execute.get_tool_execution_logs_pb2.ListToolExecutionLogsRequest, int, str, int) -> tool_sdk.api.execute.get_tool_execution_logs_pb2.ListToolExecutionLogsResponse
        """
        根据execId批量获取工具执行日志
        :param request: list_tool_execution_logs请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: tool_sdk.api.execute.get_tool_execution_logs_pb2.ListToolExecutionLogsResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.tool.execute.ListToolExecutionLogs"
        uri = "/tools/execution/logs/{execIds}".format(
            execIds=request.execIds,
        )
        requestParam = request
        
        rsp_obj = tool_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.tool_sdk",
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
        rsp = tool_sdk.api.execute.get_tool_execution_logs_pb2.ListToolExecutionLogsResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_tool_execution_table_result(self, request, org, user, timeout=10):
        # type: (tool_sdk.api.execute.get_tool_execution_table_result_pb2.GetToolExecutionTableResultRequest, int, str, int) -> tool_sdk.api.execute.get_tool_execution_table_result_pb2.GetToolExecutionTableResultResponse
        """
        获取工具执行表格结果
        :param request: get_tool_execution_table_result请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: tool_sdk.api.execute.get_tool_execution_table_result_pb2.GetToolExecutionTableResultResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.tool.execute.GetToolExecutionTableResult"
        uri = "/tools/execution/{execId}/table".format(
            execId=request.execId,
        )
        requestParam = request
        
        rsp_obj = tool_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.tool_sdk",
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
        rsp = tool_sdk.api.execute.get_tool_execution_table_result_pb2.GetToolExecutionTableResultResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_tool_execution_result(self, request, org, user, timeout=10):
        # type: (tool_sdk.api.execute.list_tool_execution_result_pb2.ListToolExecutionResultRequest, int, str, int) -> tool_sdk.api.execute.list_tool_execution_result_pb2.ListToolExecutionResultResponse
        """
        批量获取工具执行结果
        :param request: list_tool_execution_result请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: tool_sdk.api.execute.list_tool_execution_result_pb2.ListToolExecutionResultResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.tool.execute.ListToolExecutionResult"
        uri = "/tools/result/list"
        
        requestParam = request
        
        rsp_obj = tool_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.tool_sdk",
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
        rsp = tool_sdk.api.execute.list_tool_execution_result_pb2.ListToolExecutionResultResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def terminate_task(self, request, org, user, timeout=10):
        # type: (tool_sdk.api.execute.terminate_task_pb2.TerminateTaskRequest, int, str, int) -> tool_sdk.model.tool.tool_task_pb2.ToolTask
        """
        终止进行中任务
        :param request: terminate_task请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: tool_sdk.model.tool.tool_task_pb2.ToolTask
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.tool.execute.TerminateTask"
        uri = "/tools/terminate/{taskId}".format(
            taskId=request.taskId,
        )
        requestParam = request
        
        rsp_obj = tool_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.tool_sdk",
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
        rsp = tool_sdk.model.tool.tool_task_pb2.ToolTask()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def tool_debug_snapshot(self, request, org, user, timeout=10):
        # type: (tool_sdk.api.execute.tool_debug_snapshot_pb2.ToolDebugSnapshotRequest, int, str, int) -> tool_sdk.model.tool.execution_snapshot_pb2.ExecutionSnapshot
        """
        调试工具的执行快照
        :param request: tool_debug_snapshot请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: tool_sdk.model.tool.execution_snapshot_pb2.ExecutionSnapshot
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.tool.execute.ToolDebugSnapshot"
        uri = "/tools/debug/snapshot"
        
        requestParam = request
        
        rsp_obj = tool_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.tool_sdk",
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
        rsp = tool_sdk.model.tool.execution_snapshot_pb2.ExecutionSnapshot()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def tool_execution_snapshot(self, request, org, user, timeout=10):
        # type: (tool_sdk.api.execute.tool_execution_snapshot_pb2.ToolExecutionSnapshotRequest, int, str, int) -> tool_sdk.model.tool.execution_snapshot_pb2.ExecutionSnapshot
        """
        工具执行前快照
        :param request: tool_execution_snapshot请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: tool_sdk.model.tool.execution_snapshot_pb2.ExecutionSnapshot
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.tool.execute.ToolExecutionSnapshot"
        uri = "/tools/execution/snapshot"
        
        requestParam = request
        
        rsp_obj = tool_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.tool_sdk",
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
        rsp = tool_sdk.model.tool.execution_snapshot_pb2.ExecutionSnapshot()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def tool_execution_callback(self, request, org, user, timeout=10):
        # type: (tool_sdk.api.execute.tool_executon_callback_pb2.ToolExecutionCallbackRequest, int, str, int) -> tool_sdk.api.execute.tool_executon_callback_pb2.ToolExecutionCallbackResponse
        """
        执行工具回调
        :param request: tool_execution_callback请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: tool_sdk.api.execute.tool_executon_callback_pb2.ToolExecutionCallbackResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.tool.execute.ToolExecutionCallback"
        uri = "/tools/execution/callback"
        
        requestParam = request
        
        rsp_obj = tool_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.tool_sdk",
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
        rsp = tool_sdk.api.execute.tool_executon_callback_pb2.ToolExecutionCallbackResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
