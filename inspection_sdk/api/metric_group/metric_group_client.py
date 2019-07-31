# -*- coding: utf-8 -*-
import os
import sys

current_path = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = os.path.dirname(os.path.dirname(current_path))
if PROJECT_PATH not in sys.path:
    sys.path.append(PROJECT_PATH)


import create_pb2

import model.inspection.metric_group_pb2

import delete_pb2

import google.protobuf.empty_pb2

import get_pb2

import list_pb2

import update_pb2

import utils.http_util
import google.protobuf.json_format


class MetricGroupClient(object):
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

    
    def create_metric_group(self, request, org, user, timeout=10):
        # type: (create_pb2.CreateMetricGroupRequest, int, str, int) -> model.inspection.metric_group_pb2.InspectionMetricGroup
        """
        创建指标组
        :param request: create_metric_group请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: model.inspection.metric_group_pb2.InspectionMetricGroup
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.inspection.metric_group.CreateMetricGroup"
        uri = "/api/v1/inspection/{pluginId}/metric-groups".format(
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
        rsp = model.inspection.metric_group_pb2.InspectionMetricGroup()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_metric_group(self, request, org, user, timeout=10):
        # type: (delete_pb2.DeleteMetricGroupRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        删除指标组
        :param request: delete_metric_group请求
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
            route_name = "easyops.api.inspection.metric_group.DeleteMetricGroup"
        uri = "/api/v1/inspection/{pluginId}/metric-groups/{metricGroupId}".format(
            pluginId=request.pluginId,
            metricGroupId=request.metricGroupId,
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
    
    def get_metric_group(self, request, org, user, timeout=10):
        # type: (get_pb2.GetMetricGroupRequest, int, str, int) -> model.inspection.metric_group_pb2.InspectionMetricGroup
        """
        获取指标组
        :param request: get_metric_group请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: model.inspection.metric_group_pb2.InspectionMetricGroup
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.inspection.metric_group.GetMetricGroup"
        uri = "/api/v1/inspection/{pluginId}/metric-groups/{metricGroupId}".format(
            pluginId=request.pluginId,
            metricGroupId=request.metricGroupId,
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
        rsp = model.inspection.metric_group_pb2.InspectionMetricGroup()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_metric_group(self, request, org, user, timeout=10):
        # type: (list_pb2.ListMetricGroupRequest, int, str, int) -> list_pb2.ListMetricGroupResponse
        """
        获取指标组列表
        :param request: list_metric_group请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: list_pb2.ListMetricGroupResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.inspection.metric_group.ListMetricGroup"
        uri = "/api/v1/inspection/{pluginId}/metric-groups".format(
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
        rsp = list_pb2.ListMetricGroupResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_metric_group(self, request, org, user, timeout=10):
        # type: (update_pb2.UpdateMetricGroupRequest, int, str, int) -> model.inspection.metric_group_pb2.InspectionMetricGroup
        """
        更新指标组
        :param request: update_metric_group请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: model.inspection.metric_group_pb2.InspectionMetricGroup
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.inspection.metric_group.UpdateMetricGroup"
        uri = "/api/v1/inspection/{pluginId}/metric-groups/{metricGroupId}".format(
            pluginId=request.pluginId,
            metricGroupId=request.metricGroupId,
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
        rsp = model.inspection.metric_group_pb2.InspectionMetricGroup()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
