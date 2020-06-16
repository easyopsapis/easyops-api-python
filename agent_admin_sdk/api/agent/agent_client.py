# -*- coding: utf-8 -*-
import os
import sys


import agent_admin_sdk.api.agent.get_agent_pb2

import agent_admin_sdk.model.agent_admin.agent_pb2

import agent_admin_sdk.api.agent.list_agent_pb2

import agent_admin_sdk.api.agent.list_agent_plugins_pb2

import agent_admin_sdk.api.agent.list_agent_plugins_v1_pb2

import agent_admin_sdk.api.agent.list_agent_status_old_pb2

import agent_admin_sdk.api.agent.upsert_agent_plugins_pb2

import agent_admin_sdk.api.agent.upsert_agent_plugins_v1_pb2

import agent_admin_sdk.utils.http_util
import google.protobuf.json_format


class AgentClient(object):
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

    
    def get_agent(self, request, org, user, timeout=10):
        # type: (agent_admin_sdk.api.agent.get_agent_pb2.GetAgentRequest, int, str, int) -> agent_admin_sdk.model.agent_admin.agent_pb2.Agent
        """
        获取Agent详细数据
        :param request: get_agent请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: agent_admin_sdk.model.agent_admin.agent_pb2.Agent
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.agent_admin.agent.GetAgent"
        uri = "/api/v1/agent/{id}".format(
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
        rsp = agent_admin_sdk.model.agent_admin.agent_pb2.Agent()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_agent(self, request, org, user, timeout=10):
        # type: (agent_admin_sdk.api.agent.list_agent_pb2.ListAgentRequest, int, str, int) -> agent_admin_sdk.api.agent.list_agent_pb2.ListAgentResponse
        """
        Agent列表
        :param request: list_agent请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: agent_admin_sdk.api.agent.list_agent_pb2.ListAgentResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.agent_admin.agent.ListAgent"
        uri = "/api/v1/agent"
        
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
        rsp = agent_admin_sdk.api.agent.list_agent_pb2.ListAgentResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_agent_plugins(self, request, org, user, timeout=10):
        # type: (agent_admin_sdk.api.agent.list_agent_plugins_pb2.ListAgentPluginsRequest, int, str, int) -> agent_admin_sdk.api.agent.list_agent_plugins_pb2.ListAgentPluginsResponse
        """
        获取Agent插件列表
        :param request: list_agent_plugins请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: agent_admin_sdk.api.agent.list_agent_plugins_pb2.ListAgentPluginsResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.agent_admin.agent.ListAgentPlugins"
        uri = "/api/v1/agent/{id}/plugins".format(
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
        rsp = agent_admin_sdk.api.agent.list_agent_plugins_pb2.ListAgentPluginsResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_agent_plugins_v_1(self, request, org, user, timeout=10):
        # type: (agent_admin_sdk.api.agent.list_agent_plugins_v1_pb2.ListAgentPluginsV1Request, int, str, int) -> agent_admin_sdk.api.agent.list_agent_plugins_v1_pb2.ListAgentPluginsV1Response
        """
        获取Agent插件列表
        :param request: list_agent_plugins_v_1请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: agent_admin_sdk.api.agent.list_agent_plugins_v1_pb2.ListAgentPluginsV1Response
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.agent_admin.agent.ListAgentPluginsV1"
        uri = "/api/v1/agents/{id}/plugins".format(
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
        rsp = agent_admin_sdk.api.agent.list_agent_plugins_v1_pb2.ListAgentPluginsV1Response()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_agent_status_old(self, request, org, user, timeout=10):
        # type: (agent_admin_sdk.api.agent.list_agent_status_old_pb2.ListAgentStatusOldRequest, int, str, int) -> agent_admin_sdk.api.agent.list_agent_status_old_pb2.ListAgentStatusOldResponse
        """
        Agent列表
        :param request: list_agent_status_old请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: agent_admin_sdk.api.agent.list_agent_status_old_pb2.ListAgentStatusOldResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.agent_admin.agent.ListAgentStatusOld"
        uri = "/api/v1/agent_status/status"
        
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
        rsp = agent_admin_sdk.api.agent.list_agent_status_old_pb2.ListAgentStatusOldResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def upsert_agent_plugins(self, request, org, user, timeout=10):
        # type: (agent_admin_sdk.api.agent.upsert_agent_plugins_pb2.UpsertAgentPluginsRequest, int, str, int) -> agent_admin_sdk.api.agent.upsert_agent_plugins_pb2.UpsertAgentPluginsResponse
        """
        刷新Agent插件列表
        :param request: upsert_agent_plugins请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: agent_admin_sdk.api.agent.upsert_agent_plugins_pb2.UpsertAgentPluginsResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.agent_admin.agent.UpsertAgentPlugins"
        uri = "/api/v1/agent/plugins"
        
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
        rsp = agent_admin_sdk.api.agent.upsert_agent_plugins_pb2.UpsertAgentPluginsResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def upsert_agent_plugins_v_1(self, request, org, user, timeout=10):
        # type: (agent_admin_sdk.api.agent.upsert_agent_plugins_v1_pb2.UpsertAgentPluginsV1Request, int, str, int) -> agent_admin_sdk.api.agent.upsert_agent_plugins_v1_pb2.UpsertAgentPluginsV1Response
        """
        刷新Agent插件列表
        :param request: upsert_agent_plugins_v_1请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: agent_admin_sdk.api.agent.upsert_agent_plugins_v1_pb2.UpsertAgentPluginsV1Response
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.agent_admin.agent.UpsertAgentPluginsV1"
        uri = "/api/v1/deploy-info"
        
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
        rsp = agent_admin_sdk.api.agent.upsert_agent_plugins_v1_pb2.UpsertAgentPluginsV1Response()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
