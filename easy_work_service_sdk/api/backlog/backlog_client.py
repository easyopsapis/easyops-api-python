# -*- coding: utf-8 -*-
import os
import sys


import easy_work_service_sdk.api.backlog.delete_backlog_pb2

import google.protobuf.empty_pb2

import easy_work_service_sdk.api.backlog.get_backlog_statistics_pb2

import easy_work_service_sdk.model.easy_work_service.backlog_statistics_pb2

import easy_work_service_sdk.api.backlog.import_backlog_pb2

import easy_work_service_sdk.api.backlog.list_backlog_data_pb2

import easy_work_service_sdk.api.backlog.list_backlog_view_pb2

import easy_work_service_sdk.utils.http_util
import google.protobuf.json_format


class BacklogClient(object):
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

    
    def delete_backlog(self, request, org, user, timeout=10):
        # type: (easy_work_service_sdk.api.backlog.delete_backlog_pb2.DeleteBacklogRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        根据id和分类删除统一门户的事务
        :param request: delete_backlog请求
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
            route_name = "easyops.api.easy_work_service.backlog.DeleteBacklog"
        uri = "/api/easy_work_service/v1/backlog/delete/{category}/id/{id}".format(
            category=request.category,
            id=request.id,
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
        rsp = google.protobuf.empty_pb2.Empty()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_backlog_statistics(self, request, org, user, timeout=10):
        # type: (easy_work_service_sdk.api.backlog.get_backlog_statistics_pb2.GetBacklogStatisticsRequest, int, str, int) -> easy_work_service_sdk.model.easy_work_service.backlog_statistics_pb2.BacklogStatistics
        """
        根据搜索条件统计事务数据
        :param request: get_backlog_statistics请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: easy_work_service_sdk.model.easy_work_service.backlog_statistics_pb2.BacklogStatistics
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.easy_work_service.backlog.GetBacklogStatistics"
        uri = "/api/easy_work_service/v1/backlog/statistics"
        
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
        rsp = easy_work_service_sdk.model.easy_work_service.backlog_statistics_pb2.BacklogStatistics()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def import_backlog(self, request, org, user, timeout=10):
        # type: (easy_work_service_sdk.api.backlog.import_backlog_pb2.ImportBacklogRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        根据id和分类导入(创建或更新)统一门户的事务
        :param request: import_backlog请求
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
            route_name = "easyops.api.easy_work_service.backlog.ImportBacklog"
        uri = "/api/easy_work_service/v1/backlog/import/{category}/id/{id}".format(
            category=request.category,
            id=request.id,
        )
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
        rsp = google.protobuf.empty_pb2.Empty()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_backlog_data(self, request, org, user, timeout=10):
        # type: (easy_work_service_sdk.api.backlog.list_backlog_data_pb2.ListBacklogDataRequest, int, str, int) -> easy_work_service_sdk.api.backlog.list_backlog_data_pb2.ListBacklogDataResponse
        """
        获取事务数据
        :param request: list_backlog_data请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: easy_work_service_sdk.api.backlog.list_backlog_data_pb2.ListBacklogDataResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.easy_work_service.backlog.ListBacklogData"
        uri = "/api/easy_work_service/v1/backlog/data"
        
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
        rsp = easy_work_service_sdk.api.backlog.list_backlog_data_pb2.ListBacklogDataResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_backlog_view(self, request, org, user, timeout=10):
        # type: (easy_work_service_sdk.api.backlog.list_backlog_view_pb2.ListBacklogViewRequest, int, str, int) -> easy_work_service_sdk.api.backlog.list_backlog_view_pb2.ListBacklogViewResponse
        """
        获取事务视图
        :param request: list_backlog_view请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: easy_work_service_sdk.api.backlog.list_backlog_view_pb2.ListBacklogViewResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.easy_work_service.backlog.ListBacklogView"
        uri = "/api/easy_work_service/v1/backlog/view"
        
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
        rsp = easy_work_service_sdk.api.backlog.list_backlog_view_pb2.ListBacklogViewResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
