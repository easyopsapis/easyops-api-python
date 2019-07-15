# -*- coding: utf-8 -*-

import create_plugin_pb2

import create_plugin_v1_pb2

import delete_plugin_pb2

import get_plugin_pb2

import model.agent_admin.plugin_pb2

import get_plugin_v1_pb2

import list_plugin_pb2

import list_plugin_agent_pb2

import list_plugin_agent_v1_pb2

import list_plugin_v1_pb2

import update_plugin_pb2

import update_plugin_v1_pb2

import utils.http_util
import google.protobuf.json_format


class PluginClient(object):
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

    
    def create_plugin(self, request, org, user, timeout=10):
        # type: (create_plugin_pb2.CreatePluginRequest, int, str, int) -> create_plugin_pb2.CreatePluginResponse
        """
        创建插件
        :param request: create_plugin请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: create_plugin_pb2.CreatePluginResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.agent_admin.plugin.CreatePlugin"
        uri = "/api/v1/plugin"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
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
        rsp = create_plugin_pb2.CreatePluginResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def create_plugin_v_1(self, request, org, user, timeout=10):
        # type: (create_plugin_v1_pb2.CreatePluginV1Request, int, str, int) -> create_plugin_v1_pb2.CreatePluginV1Response
        """
        创建插件
        :param request: create_plugin_v_1请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: create_plugin_v1_pb2.CreatePluginV1Response
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.agent_admin.plugin.CreatePluginV1"
        uri = "/api/v1/agent-plugins"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
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
        rsp = create_plugin_v1_pb2.CreatePluginV1Response()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_plugin(self, request, org, user, timeout=10):
        # type: (delete_plugin_pb2.DeletePluginRequest, int, str, int) -> delete_plugin_pb2.DeletePluginResponse
        """
        删除插件
        :param request: delete_plugin请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: delete_plugin_pb2.DeletePluginResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.agent_admin.plugin.DeletePlugin"
        uri = "/api/v1/plugin/{id}".format(
            id=request.id,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="DELETE",
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
        rsp = delete_plugin_pb2.DeletePluginResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_plugin(self, request, org, user, timeout=10):
        # type: (get_plugin_pb2.GetPluginRequest, int, str, int) -> model.agent_admin.plugin_pb2.Plugin
        """
        获取插件
        :param request: get_plugin请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: model.agent_admin.plugin_pb2.Plugin
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.agent_admin.plugin.GetPlugin"
        uri = "/api/v1/plugin/{id}".format(
            id=request.id,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
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
        rsp = model.agent_admin.plugin_pb2.Plugin()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_plugin_v_1(self, request, org, user, timeout=10):
        # type: (get_plugin_v1_pb2.GetPluginV1Request, int, str, int) -> get_plugin_v1_pb2.GetPluginV1Response
        """
        获取插件
        :param request: get_plugin_v_1请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: get_plugin_v1_pb2.GetPluginV1Response
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.agent_admin.plugin.GetPluginV1"
        uri = "/api/v1/agent-plugins/{id}".format(
            id=request.id,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
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
        rsp = get_plugin_v1_pb2.GetPluginV1Response()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_plugin(self, request, org, user, timeout=10):
        # type: (list_plugin_pb2.ListPluginRequest, int, str, int) -> list_plugin_pb2.ListPluginResponse
        """
        插件列表
        :param request: list_plugin请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: list_plugin_pb2.ListPluginResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.agent_admin.plugin.ListPlugin"
        uri = "/api/v1/plugin"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
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
        rsp = list_plugin_pb2.ListPluginResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_plugin_agents(self, request, org, user, timeout=10):
        # type: (list_plugin_agent_pb2.ListPluginAgentsRequest, int, str, int) -> list_plugin_agent_pb2.ListPluginAgentsResponse
        """
        插件Agent列表
        :param request: list_plugin_agents请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: list_plugin_agent_pb2.ListPluginAgentsResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.agent_admin.plugin.ListPluginAgents"
        uri = "/api/v1/plugin/{id}/agents".format(
            id=request.id,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
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
        rsp = list_plugin_agent_pb2.ListPluginAgentsResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_plugin_agents_v_1(self, request, org, user, timeout=10):
        # type: (list_plugin_agent_v1_pb2.ListPluginAgentsV1Request, int, str, int) -> list_plugin_agent_v1_pb2.ListPluginAgentsV1Response
        """
        插件Agent列表
        :param request: list_plugin_agents_v_1请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: list_plugin_agent_v1_pb2.ListPluginAgentsV1Response
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.agent_admin.plugin.ListPluginAgentsV1"
        uri = "/api/v1/agent-plugins/{id}/agents".format(
            id=request.id,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
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
        rsp = list_plugin_agent_v1_pb2.ListPluginAgentsV1Response()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_plugin_v_1(self, request, org, user, timeout=10):
        # type: (list_plugin_v1_pb2.ListPluginV1Request, int, str, int) -> list_plugin_v1_pb2.ListPluginV1Response
        """
        插件列表
        :param request: list_plugin_v_1请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: list_plugin_v1_pb2.ListPluginV1Response
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.agent_admin.plugin.ListPluginV1"
        uri = "/api/v1/agent-plugins"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
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
        rsp = list_plugin_v1_pb2.ListPluginV1Response()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_plugin(self, request, org, user, timeout=10):
        # type: (update_plugin_pb2.UpdatePluginRequest, int, str, int) -> update_plugin_pb2.UpdatePluginResponse
        """
        更新插件
        :param request: update_plugin请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: update_plugin_pb2.UpdatePluginResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.agent_admin.plugin.UpdatePlugin"
        uri = "/api/v1/plugin/{id}".format(
            id=request.id,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="PUT",
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
        rsp = update_plugin_pb2.UpdatePluginResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_plugin_v_1(self, request, org, user, timeout=10):
        # type: (update_plugin_v1_pb2.UpdatePluginV1Request, int, str, int) -> update_plugin_v1_pb2.UpdatePluginV1Response
        """
        更新插件
        :param request: update_plugin_v_1请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: update_plugin_v1_pb2.UpdatePluginV1Response
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.agent_admin.plugin.UpdatePluginV1"
        uri = "/api/v1/agent-plugins/{id}".format(
            id=request.id,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="PUT",
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
        rsp = update_plugin_v1_pb2.UpdatePluginV1Response()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
