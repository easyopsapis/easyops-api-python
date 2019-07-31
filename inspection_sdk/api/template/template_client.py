# -*- coding: utf-8 -*-
import os
import sys

current_path = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = os.path.dirname(os.path.dirname(current_path))
if PROJECT_PATH not in sys.path:
    sys.path.append(PROJECT_PATH)


import create_pb2

import model.inspection.template_pb2

import delete_pb2

import google.protobuf.empty_pb2

import get_pb2

import list_pb2

import update_pb2

import utils.http_util
import google.protobuf.json_format


class TemplateClient(object):
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

    
    def create_template(self, request, org, user, timeout=10):
        # type: (create_pb2.CreateTemplateRequest, int, str, int) -> model.inspection.template_pb2.InspectionTemplate
        """
        创建报告模板
        :param request: create_template请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: model.inspection.template_pb2.InspectionTemplate
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.inspection.template.CreateTemplate"
        uri = "/api/v1/inspection/{pluginId}/report-templates".format(
            pluginId=request.pluginId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.inspection_sdk",
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
        rsp = model.inspection.template_pb2.InspectionTemplate()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_template(self, request, org, user, timeout=10):
        # type: (delete_pb2.DeleteTemplateRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        删除报告模板
        :param request: delete_template请求
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
            route_name = "easyops.api.inspection.template.DeleteTemplate"
        uri = "/api/v1/inspection/{pluginId}/report-templates/{templateId}".format(
            pluginId=request.pluginId,
            templateId=request.templateId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.inspection_sdk",
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
    
    def get_template(self, request, org, user, timeout=10):
        # type: (get_pb2.GetTemplateRequest, int, str, int) -> model.inspection.template_pb2.InspectionTemplate
        """
        获取报告模板
        :param request: get_template请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: model.inspection.template_pb2.InspectionTemplate
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.inspection.template.GetTemplate"
        uri = "/api/v1/inspection/{pluginId}/report-templates/{templateId}".format(
            pluginId=request.pluginId,
            templateId=request.templateId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="GET",
            src_name="logic.inspection_sdk",
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
        rsp = model.inspection.template_pb2.InspectionTemplate()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_template(self, request, org, user, timeout=10):
        # type: (list_pb2.ListTemplateRequest, int, str, int) -> list_pb2.ListTemplateResponse
        """
        获取报告模板列表
        :param request: list_template请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: list_pb2.ListTemplateResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.inspection.template.ListTemplate"
        uri = "/api/v1/inspection/{pluginId}/report-templates".format(
            pluginId=request.pluginId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="GET",
            src_name="logic.inspection_sdk",
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
        rsp = list_pb2.ListTemplateResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_template(self, request, org, user, timeout=10):
        # type: (update_pb2.UpdateTemplateRequest, int, str, int) -> model.inspection.template_pb2.InspectionTemplate
        """
        更新报告模板
        :param request: update_template请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: model.inspection.template_pb2.InspectionTemplate
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.inspection.template.UpdateTemplate"
        uri = "/api/v1/inspection/{pluginId}/report-templates/{templateId}".format(
            pluginId=request.pluginId,
            templateId=request.templateId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.inspection_sdk",
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
        rsp = model.inspection.template_pb2.InspectionTemplate()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
