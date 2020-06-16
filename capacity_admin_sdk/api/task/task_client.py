# -*- coding: utf-8 -*-
import os
import sys


import capacity_admin_sdk.api.task.create_task_pb2

import google.protobuf.empty_pb2

import capacity_admin_sdk.api.task.get_idle_hosts_pb2

import capacity_admin_sdk.api.task.get_task_detail_pb2

import capacity_admin_sdk.api.task.list_tasks_pb2

import capacity_admin_sdk.api.task.task_tool_callback_pb2

import capacity_admin_sdk.api.task.update_task_pb2

import capacity_admin_sdk.utils.http_util
import google.protobuf.json_format


class TaskClient(object):
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

    
    def create_task(self, request, org, user, timeout=10):
        # type: (capacity_admin_sdk.api.task.create_task_pb2.CreateTaskRequest, int, str, int) -> capacity_admin_sdk.api.task.create_task_pb2.CreateTaskResponse
        """
        创建容量管理-闲置资源任务
        :param request: create_task请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: capacity_admin_sdk.api.task.create_task_pb2.CreateTaskResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.capacity_admin.task.CreateTask"
        uri = "/api/capacity_admin/v1/task"
        
        requestParam = request
        
        rsp_obj = capacity_admin_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.capacity_admin_sdk",
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
        rsp = capacity_admin_sdk.api.task.create_task_pb2.CreateTaskResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_idle_hosts(self, request, org, user, timeout=10):
        # type: (google.protobuf.empty_pb2.Empty, int, str, int) -> capacity_admin_sdk.api.task.get_idle_hosts_pb2.GetIdleHostsResponse
        """
        获取容量管理-闲置主机列表
        :param request: get_idle_hosts请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: capacity_admin_sdk.api.task.get_idle_hosts_pb2.GetIdleHostsResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.capacity_admin.task.GetIdleHosts"
        uri = "/api/capacity_admin/v1/idle_hosts"
        
        requestParam = request
        
        rsp_obj = capacity_admin_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.capacity_admin_sdk",
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
        rsp = capacity_admin_sdk.api.task.get_idle_hosts_pb2.GetIdleHostsResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_task_detail(self, request, org, user, timeout=10):
        # type: (capacity_admin_sdk.api.task.get_task_detail_pb2.GetTaskDetailRequest, int, str, int) -> capacity_admin_sdk.api.task.get_task_detail_pb2.GetTaskDetailResponse
        """
        获取容量管理-闲置资源任务详情
        :param request: get_task_detail请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: capacity_admin_sdk.api.task.get_task_detail_pb2.GetTaskDetailResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.capacity_admin.task.GetTaskDetail"
        uri = "/api/capacity_admin/v1/task/{taskId}".format(
            taskId=request.taskId,
        )
        requestParam = request
        
        rsp_obj = capacity_admin_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.capacity_admin_sdk",
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
        rsp = capacity_admin_sdk.api.task.get_task_detail_pb2.GetTaskDetailResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_tasks(self, request, org, user, timeout=10):
        # type: (capacity_admin_sdk.api.task.list_tasks_pb2.ListTasksRequest, int, str, int) -> capacity_admin_sdk.api.task.list_tasks_pb2.ListTasksResponse
        """
        获取容量管理-闲置资源任务列表
        :param request: list_tasks请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: capacity_admin_sdk.api.task.list_tasks_pb2.ListTasksResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.capacity_admin.task.ListTasks"
        uri = "/api/capacity_admin/v1/task"
        
        requestParam = request
        
        rsp_obj = capacity_admin_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.capacity_admin_sdk",
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
        rsp = capacity_admin_sdk.api.task.list_tasks_pb2.ListTasksResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def task_tool_callback(self, request, org, user, timeout=10):
        # type: (capacity_admin_sdk.api.task.task_tool_callback_pb2.TaskToolCallbackRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        任务工具回调
        :param request: task_tool_callback请求
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
            route_name = "easyops.api.capacity_admin.task.TaskToolCallback"
        uri = "/api/capacity_admin/v1/task/tool/callback"
        
        requestParam = request
        
        rsp_obj = capacity_admin_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.capacity_admin_sdk",
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
    
    def update_task(self, request, org, user, timeout=10):
        # type: (capacity_admin_sdk.api.task.update_task_pb2.UpdateTaskRequest, int, str, int) -> capacity_admin_sdk.api.task.update_task_pb2.UpdateTaskResponse
        """
        更新容量管理-闲置资源任务
        :param request: update_task请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: capacity_admin_sdk.api.task.update_task_pb2.UpdateTaskResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.capacity_admin.task.UpdateTask"
        uri = "/api/capacity_admin/v1/task/{taskId}".format(
            taskId=request.taskId,
        )
        requestParam = request
        
        rsp_obj = capacity_admin_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.capacity_admin_sdk",
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
        rsp = capacity_admin_sdk.api.task.update_task_pb2.UpdateTaskResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
