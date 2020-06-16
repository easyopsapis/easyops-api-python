# -*- coding: utf-8 -*-
import os
import sys


import flowable_service_sdk.api.form_schema_version.delete_pb2

import google.protobuf.empty_pb2

import flowable_service_sdk.api.form_schema_version.get_pb2

import flowable_service_sdk.api.form_schema_version.list_pb2

import flowable_service_sdk.api.form_schema_version.set_main_version_pb2

import flowable_service_sdk.api.form_schema_version.update_pb2

import flowable_service_sdk.utils.http_util
import google.protobuf.json_format


class FormSchemaVersionClient(object):
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

    
    def delete_form_schema_version(self, request, org, user, timeout=10):
        # type: (flowable_service_sdk.api.form_schema_version.delete_pb2.DeleteFormSchemaVersionRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        删除表单版本
        :param request: delete_form_schema_version请求
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
            route_name = "easyops.api.flowable_service.form_schema_version.DeleteFormSchemaVersion"
        uri = "/api/flowable_service/v1/form/{formId}/version/{versionIds}".format(
            formId=request.formId,
            versionIds=request.versionIds,
        )
        requestParam = request
        
        rsp_obj = flowable_service_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.flowable_service_sdk",
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
    
    def get_form_schema_version(self, request, org, user, timeout=10):
        # type: (flowable_service_sdk.api.form_schema_version.get_pb2.GetFormSchemaVersionRequest, int, str, int) -> flowable_service_sdk.api.form_schema_version.get_pb2.GetFormSchemaVersionResponse
        """
        获取表单版本详情
        :param request: get_form_schema_version请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: flowable_service_sdk.api.form_schema_version.get_pb2.GetFormSchemaVersionResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.flowable_service.form_schema_version.GetFormSchemaVersion"
        uri = "/api/flowable_service/v1/form/{formId}/version/{versionId}".format(
            formId=request.formId,
            versionId=request.versionId,
        )
        requestParam = request
        
        rsp_obj = flowable_service_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.flowable_service_sdk",
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
        rsp = flowable_service_sdk.api.form_schema_version.get_pb2.GetFormSchemaVersionResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_form_schema_version(self, request, org, user, timeout=10):
        # type: (flowable_service_sdk.api.form_schema_version.list_pb2.ListFormSchemaVersionRequest, int, str, int) -> flowable_service_sdk.api.form_schema_version.list_pb2.ListFormSchemaVersionResponse
        """
        获取表单版本列表
        :param request: list_form_schema_version请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: flowable_service_sdk.api.form_schema_version.list_pb2.ListFormSchemaVersionResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.flowable_service.form_schema_version.ListFormSchemaVersion"
        uri = "/api/flowable_service/v1/form/{formId}/version".format(
            formId=request.formId,
        )
        requestParam = request
        
        rsp_obj = flowable_service_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.flowable_service_sdk",
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
        rsp = flowable_service_sdk.api.form_schema_version.list_pb2.ListFormSchemaVersionResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def set_form_schema_main_version(self, request, org, user, timeout=10):
        # type: (flowable_service_sdk.api.form_schema_version.set_main_version_pb2.SetFormSchemaMainVersionRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        设置表单主版本
        :param request: set_form_schema_main_version请求
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
            route_name = "easyops.api.flowable_service.form_schema_version.SetFormSchemaMainVersion"
        uri = "/api/flowable_service/v1/form/{formId}/version/{versionId}".format(
            formId=request.formId,
            versionId=request.versionId,
        )
        requestParam = request
        
        rsp_obj = flowable_service_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.flowable_service_sdk",
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
    
    def update_form_schema_version(self, request, org, user, timeout=10):
        # type: (flowable_service_sdk.api.form_schema_version.update_pb2.UpdateFormSchemaVersionRequest, int, str, int) -> flowable_service_sdk.api.form_schema_version.update_pb2.UpdateFormSchemaVersionResponse
        """
        编辑表单对应版本
        :param request: update_form_schema_version请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: flowable_service_sdk.api.form_schema_version.update_pb2.UpdateFormSchemaVersionResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.flowable_service.form_schema_version.UpdateFormSchemaVersion"
        uri = "/api/flowable_service/v1/form/{formId}/version/{versionId}".format(
            formId=request.formId,
            versionId=request.versionId,
        )
        requestParam = request
        
        rsp_obj = flowable_service_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.flowable_service_sdk",
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
        rsp = flowable_service_sdk.api.form_schema_version.update_pb2.UpdateFormSchemaVersionResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
