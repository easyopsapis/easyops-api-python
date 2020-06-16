# -*- coding: utf-8 -*-
import os
import sys


import alert_service_sdk.api.alert_event.get_alert_event_detail_pb2

import alert_service_sdk.model.monitor.alert_event_pb2

import alert_service_sdk.api.alert_event.get_alert_event_history_list_pb2

import alert_service_sdk.api.alert_event.get_alert_event_not_recover_list_pb2

import alert_service_sdk.api.alert_event.get_alert_not_recover_group_by_object_pb2

import alert_service_sdk.api.alert_event.get_related_alert_event_history_list_pb2

import alert_service_sdk.api.alert_event.search_alert_event_not_recover_pb2

import alert_service_sdk.utils.http_util
import google.protobuf.json_format


class AlertEventClient(object):
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

    
    def get_alert_event_detail(self, request, org, user, timeout=10):
        # type: (alert_service_sdk.api.alert_event.get_alert_event_detail_pb2.GetAlertEventDetailRequest, int, str, int) -> alert_service_sdk.model.monitor.alert_event_pb2.AlertEvent
        """
        获取告警事件详情
        :param request: get_alert_event_detail请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: alert_service_sdk.model.monitor.alert_event_pb2.AlertEvent
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.alert_service.alert_event.GetAlertEventDetail"
        uri = "/api/v1/alert_event/detail/{id}".format(
            id=request.id,
        )
        requestParam = request
        
        rsp_obj = alert_service_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.alert_service_sdk",
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
        rsp = alert_service_sdk.model.monitor.alert_event_pb2.AlertEvent()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_alert_event_history_list(self, request, org, user, timeout=10):
        # type: (alert_service_sdk.api.alert_event.get_alert_event_history_list_pb2.GetAlertEventHistoryListRequest, int, str, int) -> alert_service_sdk.api.alert_event.get_alert_event_history_list_pb2.GetAlertEventHistoryListResponse
        """
        获取历史告警事件列表
        :param request: get_alert_event_history_list请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: alert_service_sdk.api.alert_event.get_alert_event_history_list_pb2.GetAlertEventHistoryListResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.alert_service.alert_event.GetAlertEventHistoryList"
        uri = "/api/v1/alert_event/history"
        
        requestParam = request
        
        rsp_obj = alert_service_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.alert_service_sdk",
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
        rsp = alert_service_sdk.api.alert_event.get_alert_event_history_list_pb2.GetAlertEventHistoryListResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_alert_event_not_recover_list(self, request, org, user, timeout=10):
        # type: (alert_service_sdk.api.alert_event.get_alert_event_not_recover_list_pb2.GetAlertEventNotRecoverListRequest, int, str, int) -> alert_service_sdk.api.alert_event.get_alert_event_not_recover_list_pb2.GetAlertEventNotRecoverListResponse
        """
        获取未恢复告警事件列表
        :param request: get_alert_event_not_recover_list请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: alert_service_sdk.api.alert_event.get_alert_event_not_recover_list_pb2.GetAlertEventNotRecoverListResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.alert_service.alert_event.GetAlertEventNotRecoverList"
        uri = "/api/v1/alert_event/not_recover"
        
        requestParam = request
        
        rsp_obj = alert_service_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.alert_service_sdk",
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
        rsp = alert_service_sdk.api.alert_event.get_alert_event_not_recover_list_pb2.GetAlertEventNotRecoverListResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_alert_event_not_recover_group_by_object(self, request, org, user, timeout=10):
        # type: (alert_service_sdk.api.alert_event.get_alert_not_recover_group_by_object_pb2.GetAlertEventNotRecoverGroupByObjectRequest, int, str, int) -> alert_service_sdk.api.alert_event.get_alert_not_recover_group_by_object_pb2.GetAlertEventNotRecoverGroupByObjectResponse
        """
        按模型ID获取未恢复告警事件列表
        :param request: get_alert_event_not_recover_group_by_object请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: alert_service_sdk.api.alert_event.get_alert_not_recover_group_by_object_pb2.GetAlertEventNotRecoverGroupByObjectResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.alert_service.alert_event.GetAlertEventNotRecoverGroupByObject"
        uri = "/api/v1/alert_event/not_recover_group_by_object"
        
        requestParam = request
        
        rsp_obj = alert_service_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.alert_service_sdk",
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
        rsp = alert_service_sdk.api.alert_event.get_alert_not_recover_group_by_object_pb2.GetAlertEventNotRecoverGroupByObjectResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_related_alert_event_history_list(self, request, org, user, timeout=10):
        # type: (alert_service_sdk.api.alert_event.get_related_alert_event_history_list_pb2.GetRelatedAlertEventHistoryListRequest, int, str, int) -> alert_service_sdk.api.alert_event.get_related_alert_event_history_list_pb2.GetRelatedAlertEventHistoryListResponse
        """
        获取关联资源的历史告警事件列表
        :param request: get_related_alert_event_history_list请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: alert_service_sdk.api.alert_event.get_related_alert_event_history_list_pb2.GetRelatedAlertEventHistoryListResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.alert_service.alert_event.GetRelatedAlertEventHistoryList"
        uri = "/api/v1/alert_event/related/history"
        
        requestParam = request
        
        rsp_obj = alert_service_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.alert_service_sdk",
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
        rsp = alert_service_sdk.api.alert_event.get_related_alert_event_history_list_pb2.GetRelatedAlertEventHistoryListResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def search_alert_event_not_recover(self, request, org, user, timeout=10):
        # type: (alert_service_sdk.api.alert_event.search_alert_event_not_recover_pb2.SearchAlertEventNotRecoverRequest, int, str, int) -> alert_service_sdk.api.alert_event.search_alert_event_not_recover_pb2.SearchAlertEventNotRecoverResponse
        """
        搜索未恢复告警事件列表
        :param request: search_alert_event_not_recover请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: alert_service_sdk.api.alert_event.search_alert_event_not_recover_pb2.SearchAlertEventNotRecoverResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.alert_service.alert_event.SearchAlertEventNotRecover"
        uri = "/api/v1/alert_event/not_recover/_search"
        
        requestParam = request
        
        rsp_obj = alert_service_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.alert_service_sdk",
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
        rsp = alert_service_sdk.api.alert_event.search_alert_event_not_recover_pb2.SearchAlertEventNotRecoverResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
