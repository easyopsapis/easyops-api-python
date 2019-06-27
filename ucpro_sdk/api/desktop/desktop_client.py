# -*- coding: utf-8 -*-

import get_task_status_pb2

import install_app_pb2

import google.protobuf.empty_pb2

import running_install_app_pb2

import uninstall_app_pb2

import utils.http_util
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

    
    def get_task_status(self, request, org, user, timeout=10):
        # type: (get_task_status_pb2.GetTaskStatusRequest, int, str, int) -> get_task_status_pb2.GetTaskStatusResponse
        """
        查询安装任务状态
        :param request: get_task_status请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: get_task_status_pb2.GetTaskStatusResponse
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
        
        rsp_obj = utils.http_util.do_api_request(
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
        rsp = get_task_status_pb2.GetTaskStatusResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def install_app(self, request, org, user, timeout=10):
        # type: (install_app_pb2.InstallAppRequest, int, str, int) -> install_app_pb2.InstallAppResponse
        """
        安装小产品
        :param request: install_app请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: install_app_pb2.InstallAppResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.ucpro.desktop.InstallApp"
        uri = "/api/v1/desktop/install/{appId}/{version}".format(
            appId=request.appId,
            version=request.version,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
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
        rsp = install_app_pb2.InstallAppResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def running_install_app(self, request, org, user, timeout=10):
        # type: (google.protobuf.empty_pb2.Empty, int, str, int) -> running_install_app_pb2.RunningInstallAppResponse
        """
        正在安装的小产品
        :param request: running_install_app请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: running_install_app_pb2.RunningInstallAppResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.ucpro.desktop.RunningInstallApp"
        uri = "/api/v1/desktop/running"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
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
        rsp = running_install_app_pb2.RunningInstallAppResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def uninstall_app(self, request, org, user, timeout=10):
        # type: (uninstall_app_pb2.UninstallAppRequest, int, str, int) -> uninstall_app_pb2.UninstallAppResponse
        """
        卸载小产品
        :param request: uninstall_app请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: uninstall_app_pb2.UninstallAppResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.ucpro.desktop.UninstallApp"
        uri = "/api/v1/desktop/uninstall/{appId}/{version}".format(
            appId=request.appId,
            version=request.version,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
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
        rsp = uninstall_app_pb2.UninstallAppResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
