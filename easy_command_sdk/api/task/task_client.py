# -*- coding: utf-8 -*-
import os
import sys


import easy_command_sdk.model.easy_command.task_spec_pb2

import easy_command_sdk.api.task.create_async_pb2

import easy_command_sdk.model.easy_command.task_detail_pb2

import easy_command_sdk.api.task.get_detail_pb2

import easy_command_sdk.utils.http_util
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

    
    def create_async_task(self, request, org, user, timeout=10):
        # type: (easy_command_sdk.model.easy_command.task_spec_pb2.TaskSpec, int, str, int) -> easy_command_sdk.api.task.create_async_pb2.CreateAsyncTaskResponse
        """
        创建异步任务
        :param request: create_async_task请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: easy_command_sdk.api.task.create_async_pb2.CreateAsyncTaskResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.easy_command.task.CreateAsyncTask"
        uri = "/cmd"
        
        requestParam = request
        
        rsp_obj = easy_command_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.easy_command_sdk",
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
        rsp = easy_command_sdk.api.task.create_async_pb2.CreateAsyncTaskResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def create_sync_task(self, request, org, user, timeout=10):
        # type: (easy_command_sdk.model.easy_command.task_spec_pb2.TaskSpec, int, str, int) -> easy_command_sdk.model.easy_command.task_detail_pb2.TaskDetail
        """
        创建同步任务
        :param request: create_sync_task请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: easy_command_sdk.model.easy_command.task_detail_pb2.TaskDetail
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.easy_command.task.CreateSyncTask"
        uri = "/cmd/sync"
        
        requestParam = request
        
        rsp_obj = easy_command_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.easy_command_sdk",
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
        rsp = easy_command_sdk.model.easy_command.task_detail_pb2.TaskDetail()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def create_transient_task(self, request, org, user, timeout=10):
        # type: (easy_command_sdk.model.easy_command.task_spec_pb2.TaskSpec, int, str, int) -> easy_command_sdk.model.easy_command.task_detail_pb2.TaskDetail
        """
        创建短暂任务。无数据库日志，执行后也不可查。最大目标数默认为10。依赖 easy_command ^3.6.2
        :param request: create_transient_task请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: easy_command_sdk.model.easy_command.task_detail_pb2.TaskDetail
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.easy_command.task.CreateTransientTask"
        uri = "/cmd/transient"
        
        requestParam = request
        
        rsp_obj = easy_command_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.easy_command_sdk",
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
        rsp = easy_command_sdk.model.easy_command.task_detail_pb2.TaskDetail()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_task_detail(self, request, org, user, timeout=10):
        # type: (easy_command_sdk.api.task.get_detail_pb2.GetTaskDetailRequest, int, str, int) -> easy_command_sdk.model.easy_command.task_detail_pb2.TaskDetail
        """
        获取任务详情
        :param request: get_task_detail请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: easy_command_sdk.model.easy_command.task_detail_pb2.TaskDetail
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.easy_command.task.GetTaskDetail"
        uri = "/cmd/detail/{taskId}".format(
            taskId=request.taskId,
        )
        requestParam = request
        
        rsp_obj = easy_command_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.easy_command_sdk",
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
        rsp = easy_command_sdk.model.easy_command.task_detail_pb2.TaskDetail()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
