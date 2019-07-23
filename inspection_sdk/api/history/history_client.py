# -*- coding: utf-8 -*-
import os
import sys

current_path = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = os.path.dirname(os.path.dirname(current_path))
if PROJECT_PATH not in sys.path:
    sys.path.append(PROJECT_PATH)


import easy_command_callback_pb2

import google.protobuf.empty_pb2

import get_pb2

import model.inspection.history_pb2

import get_source_data_pb2

import get_statistics_pb2

import list_pb2

import list_abnormal_metrics_pb2

import schduler_callback_pb2

import utils.http_util
import google.protobuf.json_format


class HistoryClient(object):
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

    
    def easy_command_callback(self, request, org, user, timeout=10):
        # type: (easy_command_callback_pb2.EasyCommandCallbackRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        命令通道回调接口
        :param request: easy_command_callback请求
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
            route_name = "easyops.api.inspection.history.EasyCommandCallback"
        uri = "/command/callback/pluginId/{pluginId}/inspectionId/{inspectionTaskId}/jobId/{jobId}".format(
            pluginId=request.pluginId,
            inspectionTaskId=request.inspectionTaskId,
            jobId=request.jobId,
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
        rsp = google.protobuf.empty_pb2.Empty()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_history(self, request, org, user, timeout=10):
        # type: (get_pb2.GetHistoryRequest, int, str, int) -> model.inspection.history_pb2.InspectionHistory
        """
        获取巡检作业历史
        :param request: get_history请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: model.inspection.history_pb2.InspectionHistory
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.inspection.history.GetHistory"
        uri = "/api/v1/inspection/{pluginId}/history/{jobId}".format(
            pluginId=request.pluginId,
            jobId=request.jobId,
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
        rsp = model.inspection.history_pb2.InspectionHistory()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_source_data(self, request, org, user, timeout=10):
        # type: (get_source_data_pb2.GetSourceDataRequest, int, str, int) -> model.inspection.history_pb2.InspectionHistory
        """
        获取巡检作业的原始数据
        :param request: get_source_data请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: model.inspection.history_pb2.InspectionHistory
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.inspection.history.GetSourceData"
        uri = "/api/v1/inspection/{pluginId}/history/{jobId}/source-data".format(
            pluginId=request.pluginId,
            jobId=request.jobId,
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
        rsp = model.inspection.history_pb2.InspectionHistory()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_statistics(self, request, org, user, timeout=10):
        # type: (get_statistics_pb2.GetStatisticsRequest, int, str, int) -> get_statistics_pb2.GetStatisticsResponse
        """
        获取巡检作业的统计数据
        :param request: get_statistics请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: get_statistics_pb2.GetStatisticsResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.inspection.history.GetStatistics"
        uri = "/api/v1/inspection/{pluginId}/history/{jobId}/statistics".format(
            pluginId=request.pluginId,
            jobId=request.jobId,
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
        rsp = get_statistics_pb2.GetStatisticsResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_history(self, request, org, user, timeout=10):
        # type: (list_pb2.ListHistoryRequest, int, str, int) -> list_pb2.ListHistoryResponse
        """
        获取巡检作业历史列表
        :param request: list_history请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: list_pb2.ListHistoryResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.inspection.history.ListHistory"
        uri = "/api/v1/inspection/{pluginId}/history".format(
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
        rsp = list_pb2.ListHistoryResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_abnormal_metrics(self, request, org, user, timeout=10):
        # type: (list_abnormal_metrics_pb2.ListAbnormalMetricsRequest, int, str, int) -> list_abnormal_metrics_pb2.ListAbnormalMetricsResponse
        """
        获取巡检作业历史列表
        :param request: list_abnormal_metrics请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: list_abnormal_metrics_pb2.ListAbnormalMetricsResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.inspection.history.ListAbnormalMetrics"
        uri = "/api/v1/inspection/{pluginId}/history/{jobId}/abnormal-metrics".format(
            pluginId=request.pluginId,
            jobId=request.jobId,
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
        rsp = list_abnormal_metrics_pb2.ListAbnormalMetricsResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def scheduler_callback(self, request, org, user, timeout=10):
        # type: (schduler_callback_pb2.SchedulerCallbackRequest, int, str, int) -> schduler_callback_pb2.SchedulerCallbackResponse
        """
        定时任务回调接口,用于创建easy_command任务
        :param request: scheduler_callback请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: schduler_callback_pb2.SchedulerCallbackResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.inspection.history.SchedulerCallback"
        uri = "/command/callback/pluginId/{pluginId}/inspectionId/{inspectionTaskId}/callback".format(
            pluginId=request.pluginId,
            inspectionTaskId=request.inspectionTaskId,
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
        rsp = schduler_callback_pb2.SchedulerCallbackResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
