# -*- coding: utf-8 -*-
import os
import sys


import data_ops_analysis_sdk.api.model_analysis.create_analysis_setting_pb2

import google.protobuf.empty_pb2

import data_ops_analysis_sdk.api.model_analysis.get_model_analysis_pb2

import data_ops_analysis_sdk.utils.http_util
import google.protobuf.json_format


class ModelAnalysisClient(object):
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

    
    def create_analysis_setting(self, request, org, user, timeout=10):
        # type: (data_ops_analysis_sdk.api.model_analysis.create_analysis_setting_pb2.CreateAnalysisSettingRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        创建模型字段分析设置
        :param request: create_analysis_setting请求
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
            route_name = "easyops.api.data_ops_analysis.model_analysis.CreateAnalysisSetting"
        uri = "/api/data_ops_analysis/v1/model/analysis_setting"
        
        requestParam = request
        
        rsp_obj = data_ops_analysis_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.data_ops_analysis_sdk",
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
    
    def get_model_analysis(self, request, org, user, timeout=10):
        # type: (google.protobuf.empty_pb2.Empty, int, str, int) -> data_ops_analysis_sdk.api.model_analysis.get_model_analysis_pb2.GetModelAnalysisResponse
        """
        获取模型字段分析数据
        :param request: get_model_analysis请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: data_ops_analysis_sdk.api.model_analysis.get_model_analysis_pb2.GetModelAnalysisResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.data_ops_analysis.model_analysis.GetModelAnalysis"
        uri = "/api/data_ops_analysis/v1/model/analysis"
        
        requestParam = request
        
        rsp_obj = data_ops_analysis_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.data_ops_analysis_sdk",
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
        rsp = data_ops_analysis_sdk.api.model_analysis.get_model_analysis_pb2.GetModelAnalysisResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
