# -*- coding: utf-8 -*-
import os
import sys


import agent_admin_sdk.api.admin_task.callback_task_pb2

import agent_admin_sdk.api.admin_task.callback_task_v1_pb2

import agent_admin_sdk.api.admin_task.get_deploy_task_v1_pb2

import agent_admin_sdk.api.admin_task.get_task_pb2

import agent_admin_sdk.model.agent_admin.admin_task_pb2

import agent_admin_sdk.api.admin_task.install_plugin_pb2

import agent_admin_sdk.api.admin_task.install_plugin_v1_pb2

import agent_admin_sdk.api.admin_task.list_plugin_task_pb2

import agent_admin_sdk.api.admin_task.refresh_agent_plugin_pb2

import agent_admin_sdk.api.admin_task.refresh_agent_plugin_v1_pb2

import google.protobuf.empty_pb2

import agent_admin_sdk.utils.http_util
import google.protobuf.json_format


class AdminTaskClient(object):
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

    
    def callback_admin_task(self, request, org, user, timeout=10):
        # type: (agent_admin_sdk.api.admin_task.callback_task_pb2.CallbackAdminTaskRequest, int, str, int) -> agent_admin_sdk.api.admin_task.callback_task_pb2.CallbackAdminTaskResponse
        """
        创建插件
        :param request: callback_admin_task请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: agent_admin_sdk.api.admin_task.callback_task_pb2.CallbackAdminTaskResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.agent_admin.admin_task.CallbackAdminTask"
        uri = "/api/v1/task/callback"
        
        requestParam = request
        
        rsp_obj = agent_admin_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.agent_admin_sdk",
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
        rsp = agent_admin_sdk.api.admin_task.callback_task_pb2.CallbackAdminTaskResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def callback_admin_task_v_1(self, request, org, user, timeout=10):
        # type: (agent_admin_sdk.api.admin_task.callback_task_v1_pb2.CallbackAdminTaskV1Request, int, str, int) -> agent_admin_sdk.api.admin_task.callback_task_v1_pb2.CallbackAdminTaskV1Response
        """
        创建插件
        :param request: callback_admin_task_v_1请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: agent_admin_sdk.api.admin_task.callback_task_v1_pb2.CallbackAdminTaskV1Response
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.agent_admin.admin_task.CallbackAdminTaskV1"
        uri = "/api/v1/plugin-tasks/callback"
        
        requestParam = request
        
        rsp_obj = agent_admin_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.agent_admin_sdk",
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
        rsp = agent_admin_sdk.api.admin_task.callback_task_v1_pb2.CallbackAdminTaskV1Response()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_deploy_task_v_1(self, request, org, user, timeout=10):
        # type: (agent_admin_sdk.api.admin_task.get_deploy_task_v1_pb2.GetDeployTaskV1Request, int, str, int) -> agent_admin_sdk.api.admin_task.get_deploy_task_v1_pb2.GetDeployTaskV1Response
        """
        获取任务详细数据
        :param request: get_deploy_task_v_1请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: agent_admin_sdk.api.admin_task.get_deploy_task_v1_pb2.GetDeployTaskV1Response
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.agent_admin.admin_task.GetDeployTaskV1"
        uri = "/api/v1/plugin-tasks/{cmdTaskId}".format(
            cmdTaskId=request.cmdTaskId,
        )
        requestParam = request
        
        rsp_obj = agent_admin_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.agent_admin_sdk",
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
        rsp = agent_admin_sdk.api.admin_task.get_deploy_task_v1_pb2.GetDeployTaskV1Response()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_task(self, request, org, user, timeout=10):
        # type: (agent_admin_sdk.api.admin_task.get_task_pb2.GetTaskRequest, int, str, int) -> agent_admin_sdk.model.agent_admin.admin_task_pb2.AdminTask
        """
        获取任务详细数据
        :param request: get_task请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: agent_admin_sdk.model.agent_admin.admin_task_pb2.AdminTask
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.agent_admin.admin_task.GetTask"
        uri = "/api/v1/task/{id}".format(
            id=request.id,
        )
        requestParam = request
        
        rsp_obj = agent_admin_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.agent_admin_sdk",
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
        rsp = agent_admin_sdk.model.agent_admin.admin_task_pb2.AdminTask()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def install_plugin_task(self, request, org, user, timeout=10):
        # type: (agent_admin_sdk.api.admin_task.install_plugin_pb2.InstallPluginTaskRequest, int, str, int) -> agent_admin_sdk.api.admin_task.install_plugin_pb2.InstallPluginTaskResponse
        """
        安装插件
        :param request: install_plugin_task请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: agent_admin_sdk.api.admin_task.install_plugin_pb2.InstallPluginTaskResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.agent_admin.admin_task.InstallPluginTask"
        uri = "/api/v1/task/plugin/install"
        
        requestParam = request
        
        rsp_obj = agent_admin_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.agent_admin_sdk",
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
        rsp = agent_admin_sdk.api.admin_task.install_plugin_pb2.InstallPluginTaskResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def install_plugin_task_v_1(self, request, org, user, timeout=10):
        # type: (agent_admin_sdk.api.admin_task.install_plugin_v1_pb2.InstallPluginTaskV1Request, int, str, int) -> agent_admin_sdk.api.admin_task.install_plugin_v1_pb2.InstallPluginTaskV1Response
        """
        安装插件
        :param request: install_plugin_task_v_1请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: agent_admin_sdk.api.admin_task.install_plugin_v1_pb2.InstallPluginTaskV1Response
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.agent_admin.admin_task.InstallPluginTaskV1"
        uri = "/api/v1/plugin-tasks"
        
        requestParam = request
        
        rsp_obj = agent_admin_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.agent_admin_sdk",
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
        rsp = agent_admin_sdk.api.admin_task.install_plugin_v1_pb2.InstallPluginTaskV1Response()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_plugin_task(self, request, org, user, timeout=10):
        # type: (agent_admin_sdk.api.admin_task.list_plugin_task_pb2.ListPluginTaskRequest, int, str, int) -> agent_admin_sdk.api.admin_task.list_plugin_task_pb2.ListPluginTaskResponse
        """
        获取部署任务历史列表
        :param request: list_plugin_task请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: agent_admin_sdk.api.admin_task.list_plugin_task_pb2.ListPluginTaskResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.agent_admin.admin_task.ListPluginTask"
        uri = "/api/v1/plugin/{id}/task".format(
            id=request.id,
        )
        requestParam = request
        
        rsp_obj = agent_admin_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.agent_admin_sdk",
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
        rsp = agent_admin_sdk.api.admin_task.list_plugin_task_pb2.ListPluginTaskResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def refresh_agent_plugin_task(self, request, org, user, timeout=10):
        # type: (agent_admin_sdk.api.admin_task.refresh_agent_plugin_pb2.RefreshAgentPluginTaskRequest, int, str, int) -> agent_admin_sdk.api.admin_task.refresh_agent_plugin_pb2.RefreshAgentPluginTaskResponse
        """
        安装插件
        :param request: refresh_agent_plugin_task请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: agent_admin_sdk.api.admin_task.refresh_agent_plugin_pb2.RefreshAgentPluginTaskResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.agent_admin.admin_task.RefreshAgentPluginTask"
        uri = "/api/v1/task/agent/plugin/refresh"
        
        requestParam = request
        
        rsp_obj = agent_admin_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.agent_admin_sdk",
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
        rsp = agent_admin_sdk.api.admin_task.refresh_agent_plugin_pb2.RefreshAgentPluginTaskResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def refresh_agent_plugin_task_v_1(self, request, org, user, timeout=10):
        # type: (agent_admin_sdk.api.admin_task.refresh_agent_plugin_v1_pb2.RefreshAgentPluginTaskV1Request, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        安装插件
        :param request: refresh_agent_plugin_task_v_1请求
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
            route_name = "easyops.api.agent_admin.admin_task.RefreshAgentPluginTaskV1"
        uri = "/api/v1/agents/{agentId}/plugins/refresh".format(
            agentId=request.agentId,
        )
        requestParam = request
        
        rsp_obj = agent_admin_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.agent_admin_sdk",
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
    
