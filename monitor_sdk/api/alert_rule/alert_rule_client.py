# -*- coding: utf-8 -*-
import os
import sys


import monitor_sdk.model.monitor.alert_rule_pb2

import monitor_sdk.api.alert_rule.create_alert_rule_pb2

import monitor_sdk.api.alert_rule.delete_alert_rule_pb2

import monitor_sdk.api.alert_rule.detail_alert_rule_pb2

import monitor_sdk.api.alert_rule.detail_alert_rule_v4_pb2

import monitor_sdk.api.alert_rule.disable_alert_rule_pb2

import monitor_sdk.api.alert_rule.get_alert_rule_info_pb2

import monitor_sdk.api.alert_rule.get_alert_rule_list_pb2

import monitor_sdk.api.alert_rule.list_alert_rule_all_pb2

import monitor_sdk.api.alert_rule.update_alert_rule_pb2

import monitor_sdk.utils.http_util
import google.protobuf.json_format


class AlertRuleClient(object):
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

    
    def create_alert_rule(self, request, org, user, timeout=10):
        # type: (monitor_sdk.model.monitor.alert_rule_pb2.AlertRule, int, str, int) -> monitor_sdk.api.alert_rule.create_alert_rule_pb2.CreateAlertRuleResponse
        """
        创建告警规则
        :param request: create_alert_rule请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: monitor_sdk.api.alert_rule.create_alert_rule_pb2.CreateAlertRuleResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.monitor.alert_rule.CreateAlertRule"
        uri = "/api/v3/alert_rule/config"
        
        requestParam = request
        
        rsp_obj = monitor_sdk.utils.http_util.do_api_request(
            method="POST",
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
        rsp = monitor_sdk.api.alert_rule.create_alert_rule_pb2.CreateAlertRuleResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_alert_rule(self, request, org, user, timeout=10):
        # type: (monitor_sdk.api.alert_rule.delete_alert_rule_pb2.DeleteAlertRuleRequest, int, str, int) -> monitor_sdk.api.alert_rule.delete_alert_rule_pb2.DeleteAlertRuleResponse
        """
        删除告警规则
        :param request: delete_alert_rule请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: monitor_sdk.api.alert_rule.delete_alert_rule_pb2.DeleteAlertRuleResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.monitor.alert_rule.DeleteAlertRule"
        uri = "/api/v3/alert_rule/config/{id}".format(
            id=request.id,
        )
        requestParam = request
        
        rsp_obj = monitor_sdk.utils.http_util.do_api_request(
            method="DELETE",
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
        rsp = monitor_sdk.api.alert_rule.delete_alert_rule_pb2.DeleteAlertRuleResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def detail_alert_rule(self, request, org, user, timeout=10):
        # type: (monitor_sdk.api.alert_rule.detail_alert_rule_pb2.DetailAlertRuleRequest, int, str, int) -> monitor_sdk.api.alert_rule.detail_alert_rule_pb2.DetailAlertRuleResponse
        """
        获取告警规则详情
        :param request: detail_alert_rule请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: monitor_sdk.api.alert_rule.detail_alert_rule_pb2.DetailAlertRuleResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.monitor.alert_rule.DetailAlertRule"
        uri = "/api/v3/alert_rule/config/{id}".format(
            id=request.id,
        )
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
        rsp = monitor_sdk.api.alert_rule.detail_alert_rule_pb2.DetailAlertRuleResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def detail_alert_rule_v_4(self, request, org, user, timeout=10):
        # type: (monitor_sdk.api.alert_rule.detail_alert_rule_v4_pb2.DetailAlertRuleV4Request, int, str, int) -> monitor_sdk.api.alert_rule.detail_alert_rule_v4_pb2.DetailAlertRuleV4Response
        """
        获取告警规则详情(支持按历史版本搜索)
        :param request: detail_alert_rule_v_4请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: monitor_sdk.api.alert_rule.detail_alert_rule_v4_pb2.DetailAlertRuleV4Response
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.monitor.alert_rule.DetailAlertRuleV4"
        uri = "/api/v4/alert_rule/config/{id}".format(
            id=request.id,
        )
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
        rsp = monitor_sdk.api.alert_rule.detail_alert_rule_v4_pb2.DetailAlertRuleV4Response()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def disable_alert_rule(self, request, org, user, timeout=10):
        # type: (monitor_sdk.api.alert_rule.disable_alert_rule_pb2.DisableAlertRuleRequest, int, str, int) -> monitor_sdk.api.alert_rule.disable_alert_rule_pb2.DisableAlertRuleResponse
        """
        禁/启用告警规则
        :param request: disable_alert_rule请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: monitor_sdk.api.alert_rule.disable_alert_rule_pb2.DisableAlertRuleResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.monitor.alert_rule.DisableAlertRule"
        uri = "/api/v3/alert_rule/disabled/{id}".format(
            id=request.id,
        )
        requestParam = request
        
        rsp_obj = monitor_sdk.utils.http_util.do_api_request(
            method="PUT",
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
        rsp = monitor_sdk.api.alert_rule.disable_alert_rule_pb2.DisableAlertRuleResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def alert_rule_info(self, request, org, user, timeout=10):
        # type: (monitor_sdk.api.alert_rule.get_alert_rule_info_pb2.AlertRuleInfoRequest, int, str, int) -> monitor_sdk.api.alert_rule.get_alert_rule_info_pb2.AlertRuleInfoResponse
        """
        根据告警类型，表名获取相关信息
        :param request: alert_rule_info请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: monitor_sdk.api.alert_rule.get_alert_rule_info_pb2.AlertRuleInfoResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.monitor.alert_rule.AlertRuleInfo"
        uri = "/api/v3/alert_rule/info"
        
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
        rsp = monitor_sdk.api.alert_rule.get_alert_rule_info_pb2.AlertRuleInfoResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_alert_rule_list(self, request, org, user, timeout=10):
        # type: (monitor_sdk.api.alert_rule.get_alert_rule_list_pb2.GetAlertRuleListRequest, int, str, int) -> monitor_sdk.api.alert_rule.get_alert_rule_list_pb2.GetAlertRuleListResponse
        """
        获取告警规则列表
        :param request: get_alert_rule_list请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: monitor_sdk.api.alert_rule.get_alert_rule_list_pb2.GetAlertRuleListResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.monitor.alert_rule.GetAlertRuleList"
        uri = "/api/v3/alert_rule/config"
        
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
        rsp = monitor_sdk.api.alert_rule.get_alert_rule_list_pb2.GetAlertRuleListResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_alert_rule_all(self, request, org, user, timeout=10):
        # type: (monitor_sdk.api.alert_rule.list_alert_rule_all_pb2.ListAlertRuleAllRequest, int, str, int) -> monitor_sdk.api.alert_rule.list_alert_rule_all_pb2.ListAlertRuleAllResponse
        """
        获取全部告警规则列表
        :param request: list_alert_rule_all请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: monitor_sdk.api.alert_rule.list_alert_rule_all_pb2.ListAlertRuleAllResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.monitor.alert_rule.ListAlertRuleAll"
        uri = "/api/v3/alert_rule/config/all"
        
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
        rsp = monitor_sdk.api.alert_rule.list_alert_rule_all_pb2.ListAlertRuleAllResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_alert_rule(self, request, org, user, timeout=10):
        # type: (monitor_sdk.model.monitor.alert_rule_pb2.AlertRule, int, str, int) -> monitor_sdk.api.alert_rule.update_alert_rule_pb2.UpdateAlertRuleResponse
        """
        更新告警规则
        :param request: update_alert_rule请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: monitor_sdk.api.alert_rule.update_alert_rule_pb2.UpdateAlertRuleResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.monitor.alert_rule.UpdateAlertRule"
        uri = "/api/v3/alert_rule/config/{id}".format(
            id=request.id,
        )
        requestParam = request
        
        rsp_obj = monitor_sdk.utils.http_util.do_api_request(
            method="PUT",
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
        rsp = monitor_sdk.api.alert_rule.update_alert_rule_pb2.UpdateAlertRuleResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
