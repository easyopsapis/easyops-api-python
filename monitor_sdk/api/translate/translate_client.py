# -*- coding: utf-8 -*-
import os
import sys


import monitor_sdk.api.translate.list_translate_data_pb2

import monitor_sdk.api.translate.list_translate_rule_pb2

import monitor_sdk.utils.http_util
import google.protobuf.json_format


class TranslateClient(object):
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

    
    def list_translate_data(self, request, org, user, timeout=10):
        # type: (monitor_sdk.api.translate.list_translate_data_pb2.ListTranslateDataRequest, int, str, int) -> monitor_sdk.api.translate.list_translate_data_pb2.ListTranslateDataResponse
        """
        获取翻译规则对应的翻译数据
        :param request: list_translate_data请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: monitor_sdk.api.translate.list_translate_data_pb2.ListTranslateDataResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.monitor.translate.ListTranslateData"
        uri = "/api/v2/translate/storm/data"
        
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
        rsp = monitor_sdk.api.translate.list_translate_data_pb2.ListTranslateDataResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_translate_rule(self, request, org, user, timeout=10):
        # type: (monitor_sdk.api.translate.list_translate_rule_pb2.ListTranslateRuleRequest, int, str, int) -> monitor_sdk.api.translate.list_translate_rule_pb2.ListTranslateRuleResponse
        """
        获取翻译规则列表
        :param request: list_translate_rule请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: monitor_sdk.api.translate.list_translate_rule_pb2.ListTranslateRuleResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.monitor.translate.ListTranslateRule"
        uri = "/api/v1/translate/rule"
        
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
        rsp = monitor_sdk.api.translate.list_translate_rule_pb2.ListTranslateRuleResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
