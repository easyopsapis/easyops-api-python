# -*- coding: utf-8 -*-
import os
import sys


import scheduler_sdk.model.scheduler.task_pb2

import scheduler_sdk.api.task.create_task_pb2

import scheduler_sdk.api.task.delete_task_detail_pb2

import google.protobuf.empty_pb2

import scheduler_sdk.api.task.get_task_detail_pb2

import scheduler_sdk.api.task.list_task_pb2

import scheduler_sdk.api.task.update_task_detail_pb2

import scheduler_sdk.utils.http_util
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
        # type: (scheduler_sdk.model.scheduler.task_pb2.SchedulerTask, int, str, int) -> scheduler_sdk.api.task.create_task_pb2.CreateTaskResponse
        """
        创建定时调试任务
        :param request: create_task请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: scheduler_sdk.api.task.create_task_pb2.CreateTaskResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.scheduler.task.CreateTask"
        uri = "/api/v1/scheduler/task"
        
        requestParam = request
        
        rsp_obj = scheduler_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.scheduler_sdk",
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
        rsp = scheduler_sdk.api.task.create_task_pb2.CreateTaskResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def del_task(self, request, org, user, timeout=10):
        # type: (scheduler_sdk.api.task.delete_task_detail_pb2.DelTaskRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        删除任定时务
        :param request: del_task请求
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
            route_name = "easyops.api.scheduler.task.DelTask"
        uri = "/api/v1/scheduler/task/{taskId}".format(
            taskId=request.taskId,
        )
        requestParam = request
        
        rsp_obj = scheduler_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.scheduler_sdk",
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
    
    def get_task(self, request, org, user, timeout=10):
        # type: (scheduler_sdk.api.task.get_task_detail_pb2.GetTaskRequest, int, str, int) -> scheduler_sdk.model.scheduler.task_pb2.SchedulerTask
        """
        获取任务详情
        :param request: get_task请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: scheduler_sdk.model.scheduler.task_pb2.SchedulerTask
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.scheduler.task.GetTask"
        uri = "/api/v1/scheduler/task/{taskId}".format(
            taskId=request.taskId,
        )
        requestParam = request
        
        rsp_obj = scheduler_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.scheduler_sdk",
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
        rsp = scheduler_sdk.model.scheduler.task_pb2.SchedulerTask()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_task(self, request, org, user, timeout=10):
        # type: (scheduler_sdk.api.task.list_task_pb2.ListTaskRequest, int, str, int) -> scheduler_sdk.api.task.list_task_pb2.ListTaskResponse
        """
        获取任务列表
        :param request: list_task请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: scheduler_sdk.api.task.list_task_pb2.ListTaskResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.scheduler.task.ListTask"
        uri = "/api/v1/scheduler/task"
        
        requestParam = request
        
        rsp_obj = scheduler_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.scheduler_sdk",
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
        rsp = scheduler_sdk.api.task.list_task_pb2.ListTaskResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_task_detail(self, request, org, user, timeout=10):
        # type: (scheduler_sdk.api.task.update_task_detail_pb2.UpdateTaskDetailRequest, int, str, int) -> scheduler_sdk.api.task.update_task_detail_pb2.UpdateTaskDetailResponse
        """
        更新定时任务
        :param request: update_task_detail请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: scheduler_sdk.api.task.update_task_detail_pb2.UpdateTaskDetailResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.scheduler.task.UpdateTaskDetail"
        uri = "/api/v1/scheduler/task/{taskId}".format(
            taskId=request.taskId,
        )
        requestParam = request
        
        rsp_obj = scheduler_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.scheduler_sdk",
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
        rsp = scheduler_sdk.api.task.update_task_detail_pb2.UpdateTaskDetailResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
