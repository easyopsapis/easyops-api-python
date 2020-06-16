# -*- coding: utf-8 -*-
import os
import sys


import inspection_sdk.api.history.easy_command_callback_pb2

import google.protobuf.empty_pb2

import inspection_sdk.api.history.get_pb2

import inspection_sdk.model.inspection.history_pb2

import inspection_sdk.api.history.get_source_data_pb2

import inspection_sdk.api.history.get_statistics_pb2

import inspection_sdk.api.history.list_pb2

import inspection_sdk.api.history.list_abnormal_metrics_pb2

import inspection_sdk.api.history.schduler_callback_pb2

import inspection_sdk.utils.http_util
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
        # type: (inspection_sdk.api.history.easy_command_callback_pb2.EasyCommandCallbackRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
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
        uri = "/api/v1/inspection/{pluginId}/inspectionId/{inspectionTaskId}/jobId/{jobId}/callback".format(
            pluginId=request.pluginId,
            inspectionTaskId=request.inspectionTaskId,
            jobId=request.jobId,
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
        rsp = google.protobuf.empty_pb2.Empty()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_history(self, request, org, user, timeout=10):
        # type: (inspection_sdk.api.history.get_pb2.GetHistoryRequest, int, str, int) -> inspection_sdk.model.inspection.history_pb2.InspectionHistory
        """
        获取巡检作业历史
        :param request: get_history请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: inspection_sdk.model.inspection.history_pb2.InspectionHistory
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
        rsp = inspection_sdk.model.inspection.history_pb2.InspectionHistory()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_source_data(self, request, org, user, timeout=10):
        # type: (inspection_sdk.api.history.get_source_data_pb2.GetSourceDataRequest, int, str, int) -> inspection_sdk.model.inspection.history_pb2.InspectionHistory
        """
        获取巡检作业的原始数据
        :param request: get_source_data请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: inspection_sdk.model.inspection.history_pb2.InspectionHistory
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
        rsp = inspection_sdk.model.inspection.history_pb2.InspectionHistory()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_statistics(self, request, org, user, timeout=10):
        # type: (inspection_sdk.api.history.get_statistics_pb2.GetStatisticsRequest, int, str, int) -> inspection_sdk.api.history.get_statistics_pb2.GetStatisticsResponse
        """
        获取巡检作业的统计数据
        :param request: get_statistics请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: inspection_sdk.api.history.get_statistics_pb2.GetStatisticsResponse
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
        rsp = inspection_sdk.api.history.get_statistics_pb2.GetStatisticsResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_history(self, request, org, user, timeout=10):
        # type: (inspection_sdk.api.history.list_pb2.ListHistoryRequest, int, str, int) -> inspection_sdk.api.history.list_pb2.ListHistoryResponse
        """
        获取巡检作业历史列表
        :param request: list_history请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: inspection_sdk.api.history.list_pb2.ListHistoryResponse
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
        rsp = inspection_sdk.api.history.list_pb2.ListHistoryResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_abnormal_metrics(self, request, org, user, timeout=10):
        # type: (inspection_sdk.api.history.list_abnormal_metrics_pb2.ListAbnormalMetricsRequest, int, str, int) -> inspection_sdk.api.history.list_abnormal_metrics_pb2.ListAbnormalMetricsResponse
        """
        获取巡检作业异常指标列表
        :param request: list_abnormal_metrics请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: inspection_sdk.api.history.list_abnormal_metrics_pb2.ListAbnormalMetricsResponse
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
        rsp = inspection_sdk.api.history.list_abnormal_metrics_pb2.ListAbnormalMetricsResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def scheduler_callback(self, request, org, user, timeout=10):
        # type: (inspection_sdk.api.history.schduler_callback_pb2.SchedulerCallbackRequest, int, str, int) -> inspection_sdk.api.history.schduler_callback_pb2.SchedulerCallbackResponse
        """
        定时任务回调接口,用于创建easy_command任务
        :param request: scheduler_callback请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: inspection_sdk.api.history.schduler_callback_pb2.SchedulerCallbackResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.inspection.history.SchedulerCallback"
        uri = "/api/v1/inspection/{pluginId}/task/{inspectionTaskId}/callback".format(
            pluginId=request.pluginId,
            inspectionTaskId=request.inspectionTaskId,
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
        rsp = inspection_sdk.api.history.schduler_callback_pb2.SchedulerCallbackResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
