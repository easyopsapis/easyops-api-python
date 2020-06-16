# -*- coding: utf-8 -*-
import os
import sys


import google.protobuf.empty_pb2

import metadata_center_sdk.api.stream.create_storage_retention_policies_pb2

import metadata_center_sdk.api.stream.list_aggregate_states_pb2

import metadata_center_sdk.api.stream.list_alert_states_pb2

import metadata_center_sdk.api.stream.list_metric_states_pb2

import metadata_center_sdk.api.stream.list_metrics_states_pb2

import metadata_center_sdk.api.stream.list_storage_retention_policies_pb2

import metadata_center_sdk.api.stream.list_translate_states_pb2

import metadata_center_sdk.api.stream.replace_aggregate_states_pb2

import metadata_center_sdk.api.stream.replace_alert_states_pb2

import metadata_center_sdk.api.stream.replace_metric_states_pb2

import metadata_center_sdk.api.stream.replace_metrics_states_pb2

import metadata_center_sdk.api.stream.replace_translate_states_pb2

import metadata_center_sdk.utils.http_util
import google.protobuf.json_format


class StreamClient(object):
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

    
    def create_storage_retention_policies(self, request, org, user, timeout=10):
        # type: (google.protobuf.empty_pb2.Empty, int, str, int) -> metadata_center_sdk.api.stream.create_storage_retention_policies_pb2.CreateStorageRetentionPoliciesResponse
        """
        全量创建采集任务关联的RetentionPolicies
        :param request: create_storage_retention_policies请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: metadata_center_sdk.api.stream.create_storage_retention_policies_pb2.CreateStorageRetentionPoliciesResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.metadata_center.stream.CreateStorageRetentionPolicies"
        uri = "/api/v1/stream/storage/retention_policy"
        
        requestParam = request
        
        rsp_obj = metadata_center_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.metadata_center_sdk",
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
        rsp = metadata_center_sdk.api.stream.create_storage_retention_policies_pb2.CreateStorageRetentionPoliciesResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_aggregate_states(self, request, org, user, timeout=10):
        # type: (google.protobuf.empty_pb2.Empty, int, str, int) -> metadata_center_sdk.api.stream.list_aggregate_states_pb2.ListAggregateStatesResponse
        """
        获取所有聚合规则数据
        :param request: list_aggregate_states请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: metadata_center_sdk.api.stream.list_aggregate_states_pb2.ListAggregateStatesResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.metadata_center.stream.ListAggregateStates"
        uri = "/api/v1/stream/aggregate/states"
        
        requestParam = request
        
        rsp_obj = metadata_center_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.metadata_center_sdk",
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
        rsp = metadata_center_sdk.api.stream.list_aggregate_states_pb2.ListAggregateStatesResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_alert_states(self, request, org, user, timeout=10):
        # type: (google.protobuf.empty_pb2.Empty, int, str, int) -> metadata_center_sdk.api.stream.list_alert_states_pb2.ListAlertStatesResponse
        """
        获取所有告警规则数据
        :param request: list_alert_states请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: metadata_center_sdk.api.stream.list_alert_states_pb2.ListAlertStatesResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.metadata_center.stream.ListAlertStates"
        uri = "/api/v1/stream/alert/states"
        
        requestParam = request
        
        rsp_obj = metadata_center_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.metadata_center_sdk",
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
        rsp = metadata_center_sdk.api.stream.list_alert_states_pb2.ListAlertStatesResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_metric_states(self, request, org, user, timeout=10):
        # type: (google.protobuf.empty_pb2.Empty, int, str, int) -> metadata_center_sdk.api.stream.list_metric_states_pb2.ListMetricStatesResponse
        """
        获取所有指标项数据
        :param request: list_metric_states请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: metadata_center_sdk.api.stream.list_metric_states_pb2.ListMetricStatesResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.metadata_center.stream.ListMetricStates"
        uri = "/api/v1/stream/metric/states"
        
        requestParam = request
        
        rsp_obj = metadata_center_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.metadata_center_sdk",
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
        rsp = metadata_center_sdk.api.stream.list_metric_states_pb2.ListMetricStatesResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_metrics_states(self, request, org, user, timeout=10):
        # type: (google.protobuf.empty_pb2.Empty, int, str, int) -> metadata_center_sdk.api.stream.list_metrics_states_pb2.ListMetricsStatesResponse
        """
        获取所有指标表数据
        :param request: list_metrics_states请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: metadata_center_sdk.api.stream.list_metrics_states_pb2.ListMetricsStatesResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.metadata_center.stream.ListMetricsStates"
        uri = "/api/v1/stream/metrics/states"
        
        requestParam = request
        
        rsp_obj = metadata_center_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.metadata_center_sdk",
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
        rsp = metadata_center_sdk.api.stream.list_metrics_states_pb2.ListMetricsStatesResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_storage_retention_policies(self, request, org, user, timeout=10):
        # type: (google.protobuf.empty_pb2.Empty, int, str, int) -> metadata_center_sdk.api.stream.list_storage_retention_policies_pb2.ListStorageRetentionPoliciesResponse
        """
        获取所有采集关联的RetentionPolicies
        :param request: list_storage_retention_policies请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: metadata_center_sdk.api.stream.list_storage_retention_policies_pb2.ListStorageRetentionPoliciesResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.metadata_center.stream.ListStorageRetentionPolicies"
        uri = "/api/v1/stream/storage/retention_policy"
        
        requestParam = request
        
        rsp_obj = metadata_center_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.metadata_center_sdk",
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
        rsp = metadata_center_sdk.api.stream.list_storage_retention_policies_pb2.ListStorageRetentionPoliciesResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_translate_states(self, request, org, user, timeout=10):
        # type: (google.protobuf.empty_pb2.Empty, int, str, int) -> metadata_center_sdk.api.stream.list_translate_states_pb2.ListTranslateStatesResponse
        """
        获取所有翻译规则数据
        :param request: list_translate_states请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: metadata_center_sdk.api.stream.list_translate_states_pb2.ListTranslateStatesResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.metadata_center.stream.ListTranslateStates"
        uri = "/api/v1/stream/translate/states"
        
        requestParam = request
        
        rsp_obj = metadata_center_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.metadata_center_sdk",
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
        rsp = metadata_center_sdk.api.stream.list_translate_states_pb2.ListTranslateStatesResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def replace_aggregate_states(self, request, org, user, timeout=10):
        # type: (google.protobuf.empty_pb2.Empty, int, str, int) -> metadata_center_sdk.api.stream.replace_aggregate_states_pb2.ReplaceAggregateStatesResponse
        """
        全量更新流系统的聚合状态数据
        :param request: replace_aggregate_states请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: metadata_center_sdk.api.stream.replace_aggregate_states_pb2.ReplaceAggregateStatesResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.metadata_center.stream.ReplaceAggregateStates"
        uri = "/api/v1/stream/aggregate/states"
        
        requestParam = request
        
        rsp_obj = metadata_center_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.metadata_center_sdk",
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
        rsp = metadata_center_sdk.api.stream.replace_aggregate_states_pb2.ReplaceAggregateStatesResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def replace_alert_states(self, request, org, user, timeout=10):
        # type: (google.protobuf.empty_pb2.Empty, int, str, int) -> metadata_center_sdk.api.stream.replace_alert_states_pb2.ReplaceAlertStatesResponse
        """
        全量更新流系统的告警状态数据
        :param request: replace_alert_states请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: metadata_center_sdk.api.stream.replace_alert_states_pb2.ReplaceAlertStatesResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.metadata_center.stream.ReplaceAlertStates"
        uri = "/api/v1/stream/alert/states"
        
        requestParam = request
        
        rsp_obj = metadata_center_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.metadata_center_sdk",
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
        rsp = metadata_center_sdk.api.stream.replace_alert_states_pb2.ReplaceAlertStatesResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def replace_metric_states(self, request, org, user, timeout=10):
        # type: (google.protobuf.empty_pb2.Empty, int, str, int) -> metadata_center_sdk.api.stream.replace_metric_states_pb2.ReplaceMetricStatesResponse
        """
        全量更新流系统的指标项状态数据
        :param request: replace_metric_states请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: metadata_center_sdk.api.stream.replace_metric_states_pb2.ReplaceMetricStatesResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.metadata_center.stream.ReplaceMetricStates"
        uri = "/api/v1/stream/metric/states"
        
        requestParam = request
        
        rsp_obj = metadata_center_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.metadata_center_sdk",
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
        rsp = metadata_center_sdk.api.stream.replace_metric_states_pb2.ReplaceMetricStatesResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def replace_metrics_states(self, request, org, user, timeout=10):
        # type: (google.protobuf.empty_pb2.Empty, int, str, int) -> metadata_center_sdk.api.stream.replace_metrics_states_pb2.ReplaceMetricsStatesResponse
        """
        全量更新流系统的指标表状态数据
        :param request: replace_metrics_states请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: metadata_center_sdk.api.stream.replace_metrics_states_pb2.ReplaceMetricsStatesResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.metadata_center.stream.ReplaceMetricsStates"
        uri = "/api/v1/stream/metrics/states"
        
        requestParam = request
        
        rsp_obj = metadata_center_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.metadata_center_sdk",
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
        rsp = metadata_center_sdk.api.stream.replace_metrics_states_pb2.ReplaceMetricsStatesResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def replace_translate_states(self, request, org, user, timeout=10):
        # type: (google.protobuf.empty_pb2.Empty, int, str, int) -> metadata_center_sdk.api.stream.replace_translate_states_pb2.ReplaceTranslateStatesResponse
        """
        全量更新流系统的翻译状态数据
        :param request: replace_translate_states请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: metadata_center_sdk.api.stream.replace_translate_states_pb2.ReplaceTranslateStatesResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.metadata_center.stream.ReplaceTranslateStates"
        uri = "/api/v1/stream/translate/states"
        
        requestParam = request
        
        rsp_obj = metadata_center_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.metadata_center_sdk",
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
        rsp = metadata_center_sdk.api.stream.replace_translate_states_pb2.ReplaceTranslateStatesResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
