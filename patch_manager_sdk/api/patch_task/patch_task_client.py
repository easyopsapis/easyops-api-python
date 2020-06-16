# -*- coding: utf-8 -*-
import os
import sys


import patch_manager_sdk.api.patch_task.create_task_pb2

import patch_manager_sdk.api.patch_task.get_task_detail_pb2

import patch_manager_sdk.api.patch_task.list_task_pb2

import patch_manager_sdk.model.easy_command.task_detail_pb2

import patch_manager_sdk.api.patch_task.update_task_pb2

import patch_manager_sdk.utils.http_util
import google.protobuf.json_format


class PatchTaskClient(object):
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

    
    def create_patch_task(self, request, org, user, timeout=10):
        # type: (patch_manager_sdk.api.patch_task.create_task_pb2.CreatePatchTaskRequest, int, str, int) -> patch_manager_sdk.api.patch_task.create_task_pb2.CreatePatchTaskResponse
        """
        发起补丁安装任务
        :param request: create_patch_task请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: patch_manager_sdk.api.patch_task.create_task_pb2.CreatePatchTaskResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.patch_manager.patch_task.CreatePatchTask"
        uri = "/api/patch_manager/v1/patch_task"
        
        requestParam = request
        
        rsp_obj = patch_manager_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.patch_manager_sdk",
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
        rsp = patch_manager_sdk.api.patch_task.create_task_pb2.CreatePatchTaskResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_patch_task_detail(self, request, org, user, timeout=10):
        # type: (patch_manager_sdk.api.patch_task.get_task_detail_pb2.GetPatchTaskDetailRequest, int, str, int) -> patch_manager_sdk.api.patch_task.get_task_detail_pb2.GetPatchTaskDetailResponse
        """
        获取补丁安装任务详情
        :param request: get_patch_task_detail请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: patch_manager_sdk.api.patch_task.get_task_detail_pb2.GetPatchTaskDetailResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.patch_manager.patch_task.GetPatchTaskDetail"
        uri = "/api/patch_manager/v1/patch_task/{taskId}".format(
            taskId=request.taskId,
        )
        requestParam = request
        
        rsp_obj = patch_manager_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.patch_manager_sdk",
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
        rsp = patch_manager_sdk.api.patch_task.get_task_detail_pb2.GetPatchTaskDetailResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_patch_task(self, request, org, user, timeout=10):
        # type: (patch_manager_sdk.api.patch_task.list_task_pb2.ListPatchTaskRequest, int, str, int) -> patch_manager_sdk.api.patch_task.list_task_pb2.ListPatchTaskResponse
        """
        获取安装补丁的任务列表
        :param request: list_patch_task请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: patch_manager_sdk.api.patch_task.list_task_pb2.ListPatchTaskResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.patch_manager.patch_task.ListPatchTask"
        uri = "/api/patch_manager/v1/patch_task"
        
        requestParam = request
        
        rsp_obj = patch_manager_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.patch_manager_sdk",
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
        rsp = patch_manager_sdk.api.patch_task.list_task_pb2.ListPatchTaskResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def host_patch_task_callback(self, request, org, user, timeout=10):
        # type: (patch_manager_sdk.model.easy_command.task_detail_pb2.TaskDetail, int, str, int) -> patch_manager_sdk.api.patch_task.update_task_pb2.HostPatchTaskCallbackResponse
        """
        主机备份任务结果回调
        :param request: host_patch_task_callback请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: patch_manager_sdk.api.patch_task.update_task_pb2.HostPatchTaskCallbackResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.patch_manager.patch_task.HostPatchTaskCallback"
        uri = "/api/patch_manager/v1/host_patch_task"
        
        requestParam = request
        
        rsp_obj = patch_manager_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.patch_manager_sdk",
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
        rsp = patch_manager_sdk.api.patch_task.update_task_pb2.HostPatchTaskCallbackResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
