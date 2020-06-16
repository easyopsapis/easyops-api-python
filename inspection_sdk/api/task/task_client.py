# -*- coding: utf-8 -*-
import os
import sys


import inspection_sdk.api.task.create_pb2

import inspection_sdk.api.task.delete_pb2

import google.protobuf.empty_pb2

import inspection_sdk.api.task.get_pb2

import inspection_sdk.model.inspection.task_pb2

import inspection_sdk.api.task.list_pb2

import inspection_sdk.api.task.update_pb2

import inspection_sdk.utils.http_util
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

    
    def create_task(self, request, org, user, timeout=10):
        # type: (inspection_sdk.api.task.create_pb2.CreateTaskRequest, int, str, int) -> inspection_sdk.api.task.create_pb2.CreateTaskResponse
        """
        创建巡检任务
        :param request: create_task请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: inspection_sdk.api.task.create_pb2.CreateTaskResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.inspection.task.CreateTask"
        uri = "/api/v1/inspection/{pluginId}/task".format(
            pluginId=request.pluginId,
        )
        requestParam = request
        
        rsp_obj = inspection_sdk.utils.http_util.do_api_request(
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
        rsp = inspection_sdk.api.task.create_pb2.CreateTaskResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_task(self, request, org, user, timeout=10):
        # type: (inspection_sdk.api.task.delete_pb2.DeleteTaskRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        删除巡检任务
        :param request: delete_task请求
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
            route_name = "easyops.api.inspection.task.DeleteTask"
        uri = "/api/v1/inspection/{pluginId}/task/{inspectionTaskId}".format(
            pluginId=request.pluginId,
            inspectionTaskId=request.inspectionTaskId,
        )
        requestParam = request
        
        rsp_obj = inspection_sdk.utils.http_util.do_api_request(
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
    
    def get_task(self, request, org, user, timeout=10):
        # type: (inspection_sdk.api.task.get_pb2.GetTaskRequest, int, str, int) -> inspection_sdk.model.inspection.task_pb2.InspectionTask
        """
        获取巡检任务
        :param request: get_task请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: inspection_sdk.model.inspection.task_pb2.InspectionTask
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.inspection.task.GetTask"
        uri = "/api/v1/inspection/{pluginId}/task/{inspectionTaskId}".format(
            pluginId=request.pluginId,
            inspectionTaskId=request.inspectionTaskId,
        )
        requestParam = request
        
        rsp_obj = inspection_sdk.utils.http_util.do_api_request(
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
        rsp = inspection_sdk.model.inspection.task_pb2.InspectionTask()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_inspection_info(self, request, org, user, timeout=10):
        # type: (inspection_sdk.api.task.list_pb2.ListInspectionInfoRequest, int, str, int) -> inspection_sdk.api.task.list_pb2.ListInspectionInfoResponse
        """
        获取巡检套件列表
        :param request: list_inspection_info请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: inspection_sdk.api.task.list_pb2.ListInspectionInfoResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.inspection.task.ListInspectionInfo"
        uri = "/api/v1/inspection/{pluginId}/task".format(
            pluginId=request.pluginId,
        )
        requestParam = request
        
        rsp_obj = inspection_sdk.utils.http_util.do_api_request(
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
        rsp = inspection_sdk.api.task.list_pb2.ListInspectionInfoResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_inspection_info(self, request, org, user, timeout=10):
        # type: (inspection_sdk.api.task.update_pb2.UpdateInspectionInfoRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        更新巡检套件
        :param request: update_inspection_info请求
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
            route_name = "easyops.api.inspection.task.UpdateInspectionInfo"
        uri = "/api/v1/inspection/{pluginId}/task/{inspectionTaskId}".format(
            pluginId=request.pluginId,
            inspectionTaskId=request.inspectionTaskId,
        )
        requestParam = request
        
        rsp_obj = inspection_sdk.utils.http_util.do_api_request(
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
        rsp = google.protobuf.empty_pb2.Empty()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
