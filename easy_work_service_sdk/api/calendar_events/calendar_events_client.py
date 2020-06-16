# -*- coding: utf-8 -*-
import os
import sys


import easy_work_service_sdk.api.calendar_events.create_event_pb2

import easy_work_service_sdk.api.calendar_events.delete_event_pb2

import easy_work_service_sdk.api.calendar_events.get_event_pb2

import easy_work_service_sdk.model.easy_work_service.calendar_events_pb2

import easy_work_service_sdk.api.calendar_events.list_events_pb2

import easy_work_service_sdk.api.calendar_events.update_event_pb2

import easy_work_service_sdk.utils.http_util
import google.protobuf.json_format


class CalendarEventsClient(object):
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

    
    def create_event(self, request, org, user, timeout=10):
        # type: (easy_work_service_sdk.api.calendar_events.create_event_pb2.CreateEventRequest, int, str, int) -> easy_work_service_sdk.api.calendar_events.create_event_pb2.CreateEventResponse
        """
        创建事件
        :param request: create_event请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: easy_work_service_sdk.api.calendar_events.create_event_pb2.CreateEventResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.easy_work_service.calendar_events.CreateEvent"
        uri = "/api/easy_work_service/v1/calendar_events"
        
        requestParam = request
        
        rsp_obj = easy_work_service_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.easy_work_service_sdk",
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
        rsp = easy_work_service_sdk.api.calendar_events.create_event_pb2.CreateEventResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_event(self, request, org, user, timeout=10):
        # type: (easy_work_service_sdk.api.calendar_events.delete_event_pb2.DeleteEventRequest, int, str, int) -> easy_work_service_sdk.api.calendar_events.delete_event_pb2.DeleteEventResponse
        """
        删除日历事件
        :param request: delete_event请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: easy_work_service_sdk.api.calendar_events.delete_event_pb2.DeleteEventResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.easy_work_service.calendar_events.DeleteEvent"
        uri = "/api/easy_work_service/v1/calendar_events/{eventId}".format(
            eventId=request.eventId,
        )
        requestParam = request
        
        rsp_obj = easy_work_service_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.easy_work_service_sdk",
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
        rsp = easy_work_service_sdk.api.calendar_events.delete_event_pb2.DeleteEventResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_event(self, request, org, user, timeout=10):
        # type: (easy_work_service_sdk.api.calendar_events.get_event_pb2.GetEventRequest, int, str, int) -> easy_work_service_sdk.model.easy_work_service.calendar_events_pb2.CalendarEvents
        """
        获取事件详情
        :param request: get_event请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: easy_work_service_sdk.model.easy_work_service.calendar_events_pb2.CalendarEvents
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.easy_work_service.calendar_events.GetEvent"
        uri = "/api/easy_work_service/v1/calendar_events/{eventId}".format(
            eventId=request.eventId,
        )
        requestParam = request
        
        rsp_obj = easy_work_service_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.easy_work_service_sdk",
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
        rsp = easy_work_service_sdk.model.easy_work_service.calendar_events_pb2.CalendarEvents()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_events(self, request, org, user, timeout=10):
        # type: (easy_work_service_sdk.api.calendar_events.list_events_pb2.ListEventsRequest, int, str, int) -> easy_work_service_sdk.api.calendar_events.list_events_pb2.ListEventsResponse
        """
        获取事件列表
        :param request: list_events请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: easy_work_service_sdk.api.calendar_events.list_events_pb2.ListEventsResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.easy_work_service.calendar_events.ListEvents"
        uri = "/api/easy_work_service/v1/calendar_events"
        
        requestParam = request
        
        rsp_obj = easy_work_service_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.easy_work_service_sdk",
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
        rsp = easy_work_service_sdk.api.calendar_events.list_events_pb2.ListEventsResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_event(self, request, org, user, timeout=10):
        # type: (easy_work_service_sdk.api.calendar_events.update_event_pb2.UpdateEventRequest, int, str, int) -> easy_work_service_sdk.model.easy_work_service.calendar_events_pb2.CalendarEvents
        """
        更新事件
        :param request: update_event请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: easy_work_service_sdk.model.easy_work_service.calendar_events_pb2.CalendarEvents
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.easy_work_service.calendar_events.UpdateEvent"
        uri = "/api/easy_work_service/v1/calendar_events/{eventId}".format(
            eventId=request.eventId,
        )
        requestParam = request
        
        rsp_obj = easy_work_service_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.easy_work_service_sdk",
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
        rsp = easy_work_service_sdk.model.easy_work_service.calendar_events_pb2.CalendarEvents()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
