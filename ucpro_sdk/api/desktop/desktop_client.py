# -*- coding: utf-8 -*-
import os
import sys


import ucpro_sdk.api.desktop.clone_pb2

import ucpro_sdk.model.micro_app.installed_micro_app_pb2

import ucpro_sdk.api.desktop.get_app_dependencies_pb2

import ucpro_sdk.api.desktop.get_task_status_pb2

import ucpro_sdk.api.desktop.install_app_pb2

import google.protobuf.empty_pb2

import ucpro_sdk.api.desktop.running_tasks_pb2

import ucpro_sdk.api.desktop.uninstall_app_pb2

import ucpro_sdk.utils.http_util
import google.protobuf.json_format


class DesktopClient(object):
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

    
    def clone(self, request, org, user, timeout=10):
        # type: (ucpro_sdk.api.desktop.clone_pb2.CloneRequest, int, str, int) -> ucpro_sdk.model.micro_app.installed_micro_app_pb2.InstalledMicroApp
        """
        克隆小产品
        :param request: clone请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: ucpro_sdk.model.micro_app.installed_micro_app_pb2.InstalledMicroApp
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.ucpro.desktop.Clone"
        uri = "/api/micro_app/v1/installed_micro_app/clone"
        
        requestParam = request
        
        rsp_obj = ucpro_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.ucpro_sdk",
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
        rsp = ucpro_sdk.model.micro_app.installed_micro_app_pb2.InstalledMicroApp()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_app_dependencies(self, request, org, user, timeout=10):
        # type: (ucpro_sdk.api.desktop.get_app_dependencies_pb2.GetAppDependenciesRequest, int, str, int) -> ucpro_sdk.api.desktop.get_app_dependencies_pb2.GetAppDependenciesResponse
        """
        获取在线商店应用当前版本的依赖信息
        :param request: get_app_dependencies请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: ucpro_sdk.api.desktop.get_app_dependencies_pb2.GetAppDependenciesResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.ucpro.desktop.GetAppDependencies"
        uri = "/api/v1/desktop/app-dependencies"
        
        requestParam = request
        
        rsp_obj = ucpro_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.ucpro_sdk",
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
        rsp = ucpro_sdk.api.desktop.get_app_dependencies_pb2.GetAppDependenciesResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_task_status(self, request, org, user, timeout=10):
        # type: (ucpro_sdk.api.desktop.get_task_status_pb2.GetTaskStatusRequest, int, str, int) -> ucpro_sdk.api.desktop.get_task_status_pb2.GetTaskStatusResponse
        """
        查询部署任务状态
        :param request: get_task_status请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: ucpro_sdk.api.desktop.get_task_status_pb2.GetTaskStatusResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.ucpro.desktop.GetTaskStatus"
        uri = "/api/v1/desktop/task/{taskId}".format(
            taskId=request.taskId,
        )
        requestParam = request
        
        rsp_obj = ucpro_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.ucpro_sdk",
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
        rsp = ucpro_sdk.api.desktop.get_task_status_pb2.GetTaskStatusResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def install_app(self, request, org, user, timeout=10):
        # type: (ucpro_sdk.api.desktop.install_app_pb2.InstallAppRequest, int, str, int) -> ucpro_sdk.api.desktop.install_app_pb2.InstallAppResponse
        """
        安装小产品
        :param request: install_app请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: ucpro_sdk.api.desktop.install_app_pb2.InstallAppResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.ucpro.desktop.InstallApp"
        uri = "/api/v1/desktop/install-app"
        
        requestParam = request
        
        rsp_obj = ucpro_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.ucpro_sdk",
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
        rsp = ucpro_sdk.api.desktop.install_app_pb2.InstallAppResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def running_tasks(self, request, org, user, timeout=10):
        # type: (google.protobuf.empty_pb2.Empty, int, str, int) -> ucpro_sdk.api.desktop.running_tasks_pb2.RunningTasksResponse
        """
        正在安装或卸载的小产品任务
        :param request: running_tasks请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: ucpro_sdk.api.desktop.running_tasks_pb2.RunningTasksResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.ucpro.desktop.RunningTasks"
        uri = "/api/v1/desktop/task"
        
        requestParam = request
        
        rsp_obj = ucpro_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.ucpro_sdk",
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
        rsp = ucpro_sdk.api.desktop.running_tasks_pb2.RunningTasksResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def uninstall_app(self, request, org, user, timeout=10):
        # type: (ucpro_sdk.api.desktop.uninstall_app_pb2.UninstallAppRequest, int, str, int) -> ucpro_sdk.api.desktop.uninstall_app_pb2.UninstallAppResponse
        """
        卸载小产品
        :param request: uninstall_app请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: ucpro_sdk.api.desktop.uninstall_app_pb2.UninstallAppResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.ucpro.desktop.UninstallApp"
        uri = "/api/v1/desktop/uninstall-app"
        
        requestParam = request
        
        rsp_obj = ucpro_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.ucpro_sdk",
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
        rsp = ucpro_sdk.api.desktop.uninstall_app_pb2.UninstallAppResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
