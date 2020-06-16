# -*- coding: utf-8 -*-
import os
import sys


import resource_manage_sdk.model.resource_manage.filter_strategy_pb2

import resource_manage_sdk.api.datafilter.create_strategy_pb2

import resource_manage_sdk.api.datafilter.delete_strategy_pb2

import google.protobuf.empty_pb2

import resource_manage_sdk.api.datafilter.execute_strategy_pb2

import resource_manage_sdk.api.datafilter.get_strategy_pb2

import resource_manage_sdk.api.datafilter.get_strategy_execute_instance_pb2

import resource_manage_sdk.api.datafilter.get_strategy_overview_pb2

import resource_manage_sdk.api.datafilter.list_strategy_pb2

import resource_manage_sdk.api.datafilter.query_strategy_execute_instance_pb2

import resource_manage_sdk.api.datafilter.toggle_strategy_pb2

import resource_manage_sdk.api.datafilter.update_strategy_pb2

import resource_manage_sdk.utils.http_util
import google.protobuf.json_format


class DatafilterClient(object):
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

    
    def create_strategy(self, request, org, user, timeout=10):
        # type: (resource_manage_sdk.model.resource_manage.filter_strategy_pb2.FilterStrategy, int, str, int) -> resource_manage_sdk.api.datafilter.create_strategy_pb2.CreateStrategyResponse
        """
        创建数据违规检查规则
        :param request: create_strategy请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: resource_manage_sdk.api.datafilter.create_strategy_pb2.CreateStrategyResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.resource_manage.datafilter.CreateStrategy"
        uri = "/api/v1/filter/strategy"
        
        requestParam = request
        
        rsp_obj = resource_manage_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.resource_manage_sdk",
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
        rsp = resource_manage_sdk.api.datafilter.create_strategy_pb2.CreateStrategyResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_strategy(self, request, org, user, timeout=10):
        # type: (resource_manage_sdk.api.datafilter.delete_strategy_pb2.DeleteStrategyRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        删除数据违规检查规则
        :param request: delete_strategy请求
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
            route_name = "easyops.api.resource_manage.datafilter.DeleteStrategy"
        uri = "/api/v1/filter/strategy/{instanceId}".format(
            instanceId=request.instanceId,
        )
        requestParam = request
        
        rsp_obj = resource_manage_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.resource_manage_sdk",
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
    
    def execute_strategy(self, request, org, user, timeout=10):
        # type: (resource_manage_sdk.api.datafilter.execute_strategy_pb2.ExecuteStrategyRequest, int, str, int) -> resource_manage_sdk.api.datafilter.execute_strategy_pb2.ExecuteStrategyResponse
        """
        立即执行规则检查
        :param request: execute_strategy请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: resource_manage_sdk.api.datafilter.execute_strategy_pb2.ExecuteStrategyResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.resource_manage.datafilter.ExecuteStrategy"
        uri = "/api/v1/filter/instance/execute"
        
        requestParam = request
        
        rsp_obj = resource_manage_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.resource_manage_sdk",
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
        rsp = resource_manage_sdk.api.datafilter.execute_strategy_pb2.ExecuteStrategyResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_strategy(self, request, org, user, timeout=10):
        # type: (resource_manage_sdk.api.datafilter.get_strategy_pb2.GetStrategyRequest, int, str, int) -> resource_manage_sdk.model.resource_manage.filter_strategy_pb2.FilterStrategy
        """
        获取数据违规检查规则详情
        :param request: get_strategy请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: resource_manage_sdk.model.resource_manage.filter_strategy_pb2.FilterStrategy
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.resource_manage.datafilter.GetStrategy"
        uri = "/api/v1/filter/strategy/{instanceId}".format(
            instanceId=request.instanceId,
        )
        requestParam = request
        
        rsp_obj = resource_manage_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.resource_manage_sdk",
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
        rsp = resource_manage_sdk.model.resource_manage.filter_strategy_pb2.FilterStrategy()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_strategy_execute_instance(self, request, org, user, timeout=10):
        # type: (resource_manage_sdk.api.datafilter.get_strategy_execute_instance_pb2.GetStrategyExecuteInstanceRequest, int, str, int) -> resource_manage_sdk.api.datafilter.get_strategy_execute_instance_pb2.GetStrategyExecuteInstanceResponse
        """
        获取数据违规检查执行规则详情
        :param request: get_strategy_execute_instance请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: resource_manage_sdk.api.datafilter.get_strategy_execute_instance_pb2.GetStrategyExecuteInstanceResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.resource_manage.datafilter.GetStrategyExecuteInstance"
        uri = "/api/v1/filter/instance/{execId}".format(
            execId=request.execId,
        )
        requestParam = request
        
        rsp_obj = resource_manage_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.resource_manage_sdk",
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
        rsp = resource_manage_sdk.api.datafilter.get_strategy_execute_instance_pb2.GetStrategyExecuteInstanceResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_strategy_overview(self, request, org, user, timeout=10):
        # type: (resource_manage_sdk.api.datafilter.get_strategy_overview_pb2.GetStrategyOverviewRequest, int, str, int) -> resource_manage_sdk.api.datafilter.get_strategy_overview_pb2.GetStrategyOverviewResponse
        """
        获取规则总览
        :param request: get_strategy_overview请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: resource_manage_sdk.api.datafilter.get_strategy_overview_pb2.GetStrategyOverviewResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.resource_manage.datafilter.GetStrategyOverview"
        uri = "/api/v1/filter/strategy/overview"
        
        requestParam = request
        
        rsp_obj = resource_manage_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.resource_manage_sdk",
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
        rsp = resource_manage_sdk.api.datafilter.get_strategy_overview_pb2.GetStrategyOverviewResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_strategy(self, request, org, user, timeout=10):
        # type: (resource_manage_sdk.api.datafilter.list_strategy_pb2.ListStrategyRequest, int, str, int) -> resource_manage_sdk.api.datafilter.list_strategy_pb2.ListStrategyResponse
        """
        批量获取数据违规检查规则
        :param request: list_strategy请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: resource_manage_sdk.api.datafilter.list_strategy_pb2.ListStrategyResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.resource_manage.datafilter.ListStrategy"
        uri = "/api/v1/filter/strategy/search"
        
        requestParam = request
        
        rsp_obj = resource_manage_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.resource_manage_sdk",
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
        rsp = resource_manage_sdk.api.datafilter.list_strategy_pb2.ListStrategyResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def push_message(self, request, org, user, timeout=10):
        # type: (google.protobuf.empty_pb2.Empty, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        消息推送
        :param request: push_message请求
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
            route_name = "easyops.api.resource_manage.datafilter.PushMessage"
        uri = "/api/v1/filter/message"
        
        requestParam = request
        
        rsp_obj = resource_manage_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.resource_manage_sdk",
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
    
    def query_strategy_execute_instance(self, request, org, user, timeout=10):
        # type: (resource_manage_sdk.api.datafilter.query_strategy_execute_instance_pb2.QueryStrategyExecuteInstanceRequest, int, str, int) -> resource_manage_sdk.api.datafilter.query_strategy_execute_instance_pb2.QueryStrategyExecuteInstanceResponse
        """
        查询数据违规检查执行历史
        :param request: query_strategy_execute_instance请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: resource_manage_sdk.api.datafilter.query_strategy_execute_instance_pb2.QueryStrategyExecuteInstanceResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.resource_manage.datafilter.QueryStrategyExecuteInstance"
        uri = "/api/v1/filter/instance/search"
        
        requestParam = request
        
        rsp_obj = resource_manage_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.resource_manage_sdk",
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
        rsp = resource_manage_sdk.api.datafilter.query_strategy_execute_instance_pb2.QueryStrategyExecuteInstanceResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def toggle_strategy(self, request, org, user, timeout=10):
        # type: (resource_manage_sdk.api.datafilter.toggle_strategy_pb2.ToggleStrategyRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        启用/禁用数据违规检查规则
        :param request: toggle_strategy请求
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
            route_name = "easyops.api.resource_manage.datafilter.ToggleStrategy"
        uri = "/api/v1/filter/strategy-enable/{instanceId}".format(
            instanceId=request.instanceId,
        )
        requestParam = request
        
        rsp_obj = resource_manage_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.resource_manage_sdk",
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
    
    def update_strategy(self, request, org, user, timeout=10):
        # type: (resource_manage_sdk.api.datafilter.update_strategy_pb2.UpdateStrategyRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        更新数据违规检查规则
        :param request: update_strategy请求
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
            route_name = "easyops.api.resource_manage.datafilter.UpdateStrategy"
        uri = "/api/v1/filter/strategy/{instanceId}".format(
            instanceId=request.instanceId,
        )
        requestParam = request.strategy
        
        rsp_obj = resource_manage_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.resource_manage_sdk",
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
    
