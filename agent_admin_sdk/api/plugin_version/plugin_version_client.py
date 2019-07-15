# -*- coding: utf-8 -*-

import create_plugin_version_pb2

import create_plugin_version_v1_pb2

import delete_plugin_version_pb2

import get_plugin_version_pb2

import model.agent_admin.plugin_version_pb2

import get_plugin_version_v1_pb2

import list_plugin_version_pb2

import list_plugin_version_v1_pb2

import update_plugin_version_pb2

import update_plugin_version_v1_pb2

import utils.http_util
import google.protobuf.json_format


class PluginVersionClient(object):
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

    
    def create_plugin_version(self, request, org, user, timeout=10):
        # type: (create_plugin_version_pb2.CreatePluginVersionRequest, int, str, int) -> create_plugin_version_pb2.CreatePluginVersionResponse
        """
        创建插件
        :param request: create_plugin_version请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: create_plugin_version_pb2.CreatePluginVersionResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.agent_admin.plugin_version.CreatePluginVersion"
        uri = "/api/v1/plugin/{id}/version".format(
            id=request.id,
        )
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
        rsp = create_plugin_version_pb2.CreatePluginVersionResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def create_plugin_version_v_1(self, request, org, user, timeout=10):
        # type: (create_plugin_version_v1_pb2.CreatePluginVersionV1Request, int, str, int) -> create_plugin_version_v1_pb2.CreatePluginVersionV1Response
        """
        创建插件
        :param request: create_plugin_version_v_1请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: create_plugin_version_v1_pb2.CreatePluginVersionV1Response
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.agent_admin.plugin_version.CreatePluginVersionV1"
        uri = "/api/v1/agent-plugins/{id}/versions".format(
            id=request.id,
        )
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
        rsp = create_plugin_version_v1_pb2.CreatePluginVersionV1Response()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_plugin_version(self, request, org, user, timeout=10):
        # type: (delete_plugin_version_pb2.DeletePluginVersionRequest, int, str, int) -> delete_plugin_version_pb2.DeletePluginVersionResponse
        """
        删除插件
        :param request: delete_plugin_version请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: delete_plugin_version_pb2.DeletePluginVersionResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.agent_admin.plugin_version.DeletePluginVersion"
        uri = "/api/v1/plugin/{id}/version/{verId}".format(
            id=request.id,
            verId=request.verId,
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
        rsp = delete_plugin_version_pb2.DeletePluginVersionResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_plugin_version(self, request, org, user, timeout=10):
        # type: (get_plugin_version_pb2.GetPluginVersionRequest, int, str, int) -> model.agent_admin.plugin_version_pb2.PluginVersion
        """
        获取插件
        :param request: get_plugin_version请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: model.agent_admin.plugin_version_pb2.PluginVersion
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.agent_admin.plugin_version.GetPluginVersion"
        uri = "/api/v1/plugin/{id}/version/{verId}".format(
            id=request.id,
            verId=request.verId,
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
        rsp = model.agent_admin.plugin_version_pb2.PluginVersion()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_plugin_version_v_1(self, request, org, user, timeout=10):
        # type: (get_plugin_version_v1_pb2.GetPluginVersionV1Request, int, str, int) -> get_plugin_version_v1_pb2.GetPluginVersionV1Response
        """
        获取插件
        :param request: get_plugin_version_v_1请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: get_plugin_version_v1_pb2.GetPluginVersionV1Response
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.agent_admin.plugin_version.GetPluginVersionV1"
        uri = "/api/v1/agent-plugins/{id}/versions/{verId}".format(
            id=request.id,
            verId=request.verId,
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
        rsp = get_plugin_version_v1_pb2.GetPluginVersionV1Response()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_plugin_version(self, request, org, user, timeout=10):
        # type: (list_plugin_version_pb2.ListPluginVersionRequest, int, str, int) -> list_plugin_version_pb2.ListPluginVersionResponse
        """
        插件列表
        :param request: list_plugin_version请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: list_plugin_version_pb2.ListPluginVersionResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.agent_admin.plugin_version.ListPluginVersion"
        uri = "/api/v1/plugin/{id}/version".format(
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
        rsp = list_plugin_version_pb2.ListPluginVersionResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_plugin_version_v_1(self, request, org, user, timeout=10):
        # type: (list_plugin_version_v1_pb2.ListPluginVersionV1Request, int, str, int) -> list_plugin_version_v1_pb2.ListPluginVersionV1Response
        """
        插件列表
        :param request: list_plugin_version_v_1请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: list_plugin_version_v1_pb2.ListPluginVersionV1Response
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.agent_admin.plugin_version.ListPluginVersionV1"
        uri = "/api/v1/agent-plugins/{id}/versions".format(
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
        rsp = list_plugin_version_v1_pb2.ListPluginVersionV1Response()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_plugin_version(self, request, org, user, timeout=10):
        # type: (update_plugin_version_pb2.UpdatePluginVersionRequest, int, str, int) -> update_plugin_version_pb2.UpdatePluginVersionResponse
        """
        更新插件
        :param request: update_plugin_version请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: update_plugin_version_pb2.UpdatePluginVersionResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.agent_admin.plugin_version.UpdatePluginVersion"
        uri = "/api/v1/plugin/{id}/version/{verId}".format(
            id=request.id,
            verId=request.verId,
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
        rsp = update_plugin_version_pb2.UpdatePluginVersionResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_plugin_version_v_1(self, request, org, user, timeout=10):
        # type: (update_plugin_version_v1_pb2.UpdatePluginVersionV1Request, int, str, int) -> update_plugin_version_v1_pb2.UpdatePluginVersionV1Response
        """
        更新插件
        :param request: update_plugin_version_v_1请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: update_plugin_version_v1_pb2.UpdatePluginVersionV1Response
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.agent_admin.plugin_version.UpdatePluginVersionV1"
        uri = "/api/v1/agent-plugins/{id}/versions/{verId}".format(
            id=request.id,
            verId=request.verId,
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
        rsp = update_plugin_version_v1_pb2.UpdatePluginVersionV1Response()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
