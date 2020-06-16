# -*- coding: utf-8 -*-
import os
import sys


import monitor_sdk.api.alert.get_alert_count_pb2

import monitor_sdk.api.alert.get_alert_event_detail_pb2

import monitor_sdk.api.alert.get_alert_event_list_pb2

import monitor_sdk.api.alert.get_not_recover_alert_event_list_pb2

import monitor_sdk.api.alert.list_alert_range_pb2

import monitor_sdk.utils.http_util
import google.protobuf.json_format


class AlertClient(object):
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

    
    def get_alert_count(self, request, org, user, timeout=10):
        # type: (monitor_sdk.api.alert.get_alert_count_pb2.GetAlertCountRequest, int, str, int) -> monitor_sdk.api.alert.get_alert_count_pb2.GetAlertCountResponse
        """
        获取目标范围内的告警数量统计
        :param request: get_alert_count请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: monitor_sdk.api.alert.get_alert_count_pb2.GetAlertCountResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.monitor.alert.GetAlertCount"
        uri = "/api/v1/alert/count"
        
        requestParam = request
        
        rsp_obj = monitor_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.monitor_sdk",
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
        rsp = monitor_sdk.api.alert.get_alert_count_pb2.GetAlertCountResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_alert_event_detail(self, request, org, user, timeout=10):
        # type: (monitor_sdk.api.alert.get_alert_event_detail_pb2.GetAlertEventDetailRequest, int, str, int) -> monitor_sdk.api.alert.get_alert_event_detail_pb2.GetAlertEventDetailResponse
        """
        获取告警事件详情
        :param request: get_alert_event_detail请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: monitor_sdk.api.alert.get_alert_event_detail_pb2.GetAlertEventDetailResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.monitor.alert.GetAlertEventDetail"
        uri = "/api/v1/alert"
        
        requestParam = request
        
        rsp_obj = monitor_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.monitor_sdk",
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
        rsp = monitor_sdk.api.alert.get_alert_event_detail_pb2.GetAlertEventDetailResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_alert_event_list(self, request, org, user, timeout=10):
        # type: (monitor_sdk.api.alert.get_alert_event_list_pb2.GetAlertEventListRequest, int, str, int) -> monitor_sdk.api.alert.get_alert_event_list_pb2.GetAlertEventListResponse
        """
        获取告警事件列表
        :param request: get_alert_event_list请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: monitor_sdk.api.alert.get_alert_event_list_pb2.GetAlertEventListResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.monitor.alert.GetAlertEventList"
        uri = "/api/v1/alert"
        
        requestParam = request
        
        rsp_obj = monitor_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.monitor_sdk",
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
        rsp = monitor_sdk.api.alert.get_alert_event_list_pb2.GetAlertEventListResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_not_recover_alert_event_list(self, request, org, user, timeout=10):
        # type: (monitor_sdk.api.alert.get_not_recover_alert_event_list_pb2.GetNotRecoverAlertEventListRequest, int, str, int) -> monitor_sdk.api.alert.get_not_recover_alert_event_list_pb2.GetNotRecoverAlertEventListResponse
        """
        获取未恢复告警事件列表
        :param request: get_not_recover_alert_event_list请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: monitor_sdk.api.alert.get_not_recover_alert_event_list_pb2.GetNotRecoverAlertEventListResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.monitor.alert.GetNotRecoverAlertEventList"
        uri = "/api/v1/alert/alert_status_not_recover"
        
        requestParam = request
        
        rsp_obj = monitor_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.monitor_sdk",
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
        rsp = monitor_sdk.api.alert.get_not_recover_alert_event_list_pb2.GetNotRecoverAlertEventListResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_alert_range(self, request, org, user, timeout=10):
        # type: (monitor_sdk.api.alert.list_alert_range_pb2.ListAlertRangeRequest, int, str, int) -> monitor_sdk.api.alert.list_alert_range_pb2.ListAlertRangeResponse
        """
        获取告警状态列表
        :param request: list_alert_range请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: monitor_sdk.api.alert.list_alert_range_pb2.ListAlertRangeResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.monitor.alert.ListAlertRange"
        uri = "/api/v1/alert_range"
        
        requestParam = request
        
        rsp_obj = monitor_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.monitor_sdk",
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
        rsp = monitor_sdk.api.alert.list_alert_range_pb2.ListAlertRangeResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
