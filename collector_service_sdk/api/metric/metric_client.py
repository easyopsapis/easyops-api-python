# -*- coding: utf-8 -*-
import os
import sys


import collector_service_sdk.model.collector_service.aggregate_metric_rule_pb2

import collector_service_sdk.api.metric.create_aggregate_metric_rule_pb2

import collector_service_sdk.api.metric.create_metric_pb2

import collector_service_sdk.api.metric.delete_aggregate_metric_rule_pb2

import google.protobuf.empty_pb2

import collector_service_sdk.api.metric.detail_aggregate_metric_rule_pb2

import collector_service_sdk.api.metric.get_metric_name_detail_pb2

import collector_service_sdk.api.metric.list_aggregate_metric_rule_pb2

import collector_service_sdk.api.metric.list_collector_alias_metric_pb2

import collector_service_sdk.api.metric.list_collector_metric_pb2

import collector_service_sdk.api.metric.list_metric_names_pb2

import collector_service_sdk.api.metric.set_resource_key_metric_pb2

import collector_service_sdk.api.metric.update_aggregate_metric_rule_pb2

import collector_service_sdk.api.metric.update_metric_pb2

import collector_service_sdk.utils.http_util
import google.protobuf.json_format


class MetricClient(object):
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

    
    def create_collector_aggregate_metric_rule(self, request, org, user, timeout=10):
        # type: (collector_service_sdk.model.collector_service.aggregate_metric_rule_pb2.CollectorAggregateMetricRule, int, str, int) -> collector_service_sdk.api.metric.create_aggregate_metric_rule_pb2.CreateCollectorAggregateMetricRuleResponse
        """
        创建聚合指标规则
        :param request: create_collector_aggregate_metric_rule请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: collector_service_sdk.api.metric.create_aggregate_metric_rule_pb2.CreateCollectorAggregateMetricRuleResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.collector_service.metric.CreateCollectorAggregateMetricRule"
        uri = "/api/v1/collector-aggregate-metric-rule"
        
        requestParam = request
        
        rsp_obj = collector_service_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.collector_service_sdk",
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
        rsp = collector_service_sdk.api.metric.create_aggregate_metric_rule_pb2.CreateCollectorAggregateMetricRuleResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def create_collector_metric(self, request, org, user, timeout=10):
        # type: (collector_service_sdk.api.metric.create_metric_pb2.CreateCollectorMetricRequest, int, str, int) -> collector_service_sdk.api.metric.create_metric_pb2.CreateCollectorMetricResponse
        """
        创建指标
        :param request: create_collector_metric请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: collector_service_sdk.api.metric.create_metric_pb2.CreateCollectorMetricResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.collector_service.metric.CreateCollectorMetric"
        uri = "/api/v1/collector-metric"
        
        requestParam = request
        
        rsp_obj = collector_service_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.collector_service_sdk",
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
        rsp = collector_service_sdk.api.metric.create_metric_pb2.CreateCollectorMetricResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_collector_aggregate_metric_rule(self, request, org, user, timeout=10):
        # type: (collector_service_sdk.api.metric.delete_aggregate_metric_rule_pb2.DeleteCollectorAggregateMetricRuleRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        删除聚合指标规则
        :param request: delete_collector_aggregate_metric_rule请求
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
            route_name = "easyops.api.collector_service.metric.DeleteCollectorAggregateMetricRule"
        uri = "/api/v1/collector-aggregate-metric-rule/{instanceId}".format(
            instanceId=request.instanceId,
        )
        requestParam = request
        
        rsp_obj = collector_service_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.collector_service_sdk",
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
    
    def detail_collector_aggregate_metric_rule(self, request, org, user, timeout=10):
        # type: (collector_service_sdk.api.metric.detail_aggregate_metric_rule_pb2.DetailCollectorAggregateMetricRuleRequest, int, str, int) -> collector_service_sdk.model.collector_service.aggregate_metric_rule_pb2.CollectorAggregateMetricRule
        """
        聚合指标规则详情
        :param request: detail_collector_aggregate_metric_rule请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: collector_service_sdk.model.collector_service.aggregate_metric_rule_pb2.CollectorAggregateMetricRule
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.collector_service.metric.DetailCollectorAggregateMetricRule"
        uri = "/api/v1/collector-aggregate-metric-rule/{instanceId}".format(
            instanceId=request.instanceId,
        )
        requestParam = request
        
        rsp_obj = collector_service_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.collector_service_sdk",
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
        rsp = collector_service_sdk.model.collector_service.aggregate_metric_rule_pb2.CollectorAggregateMetricRule()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def detail_collector_metric_name(self, request, org, user, timeout=10):
        # type: (collector_service_sdk.api.metric.get_metric_name_detail_pb2.DetailCollectorMetricNameRequest, int, str, int) -> collector_service_sdk.api.metric.get_metric_name_detail_pb2.DetailCollectorMetricNameResponse
        """
        按模型名称获取采集指标名详情
        :param request: detail_collector_metric_name请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: collector_service_sdk.api.metric.get_metric_name_detail_pb2.DetailCollectorMetricNameResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.collector_service.metric.DetailCollectorMetricName"
        uri = "/api/v1/detail-collector-metric-name"
        
        requestParam = request
        
        rsp_obj = collector_service_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.collector_service_sdk",
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
        rsp = collector_service_sdk.api.metric.get_metric_name_detail_pb2.DetailCollectorMetricNameResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_collector_aggregate_metric_rule(self, request, org, user, timeout=10):
        # type: (collector_service_sdk.api.metric.list_aggregate_metric_rule_pb2.ListCollectorAggregateMetricRuleRequest, int, str, int) -> collector_service_sdk.api.metric.list_aggregate_metric_rule_pb2.ListCollectorAggregateMetricRuleResponse
        """
        获取聚合指标规则
        :param request: list_collector_aggregate_metric_rule请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: collector_service_sdk.api.metric.list_aggregate_metric_rule_pb2.ListCollectorAggregateMetricRuleResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.collector_service.metric.ListCollectorAggregateMetricRule"
        uri = "/api/v1/collector-aggregate-metric-rule"
        
        requestParam = request
        
        rsp_obj = collector_service_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.collector_service_sdk",
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
        rsp = collector_service_sdk.api.metric.list_aggregate_metric_rule_pb2.ListCollectorAggregateMetricRuleResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_collector_alias_metric(self, request, org, user, timeout=10):
        # type: (collector_service_sdk.api.metric.list_collector_alias_metric_pb2.ListCollectorAliasMetricRequest, int, str, int) -> collector_service_sdk.api.metric.list_collector_alias_metric_pb2.ListCollectorAliasMetricResponse
        """
        获取采集指标
        :param request: list_collector_alias_metric请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: collector_service_sdk.api.metric.list_collector_alias_metric_pb2.ListCollectorAliasMetricResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.collector_service.metric.ListCollectorAliasMetric"
        uri = "/api/v1/collector-alias-metric"
        
        requestParam = request
        
        rsp_obj = collector_service_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.collector_service_sdk",
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
        rsp = collector_service_sdk.api.metric.list_collector_alias_metric_pb2.ListCollectorAliasMetricResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_collector_metric(self, request, org, user, timeout=10):
        # type: (collector_service_sdk.api.metric.list_collector_metric_pb2.ListCollectorMetricRequest, int, str, int) -> collector_service_sdk.api.metric.list_collector_metric_pb2.ListCollectorMetricResponse
        """
        获取采集指标
        :param request: list_collector_metric请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: collector_service_sdk.api.metric.list_collector_metric_pb2.ListCollectorMetricResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.collector_service.metric.ListCollectorMetric"
        uri = "/api/v1/collector-metric"
        
        requestParam = request
        
        rsp_obj = collector_service_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.collector_service_sdk",
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
        rsp = collector_service_sdk.api.metric.list_collector_metric_pb2.ListCollectorMetricResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_collector_metric_names(self, request, org, user, timeout=10):
        # type: (collector_service_sdk.api.metric.list_metric_names_pb2.ListCollectorMetricNamesRequest, int, str, int) -> collector_service_sdk.api.metric.list_metric_names_pb2.ListCollectorMetricNamesResponse
        """
        按模型名称获取采集指标名映射列表
        :param request: list_collector_metric_names请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: collector_service_sdk.api.metric.list_metric_names_pb2.ListCollectorMetricNamesResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.collector_service.metric.ListCollectorMetricNames"
        uri = "/api/v1/collector-metric-names"
        
        requestParam = request
        
        rsp_obj = collector_service_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.collector_service_sdk",
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
        rsp = collector_service_sdk.api.metric.list_metric_names_pb2.ListCollectorMetricNamesResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def set_resource_key_metric(self, request, org, user, timeout=10):
        # type: (collector_service_sdk.api.metric.set_resource_key_metric_pb2.SetResourceKeyMetricRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        设置资源关键指标
        :param request: set_resource_key_metric请求
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
            route_name = "easyops.api.collector_service.metric.SetResourceKeyMetric"
        uri = "/api/v1/resource-key-metric/{objectId}".format(
            objectId=request.objectId,
        )
        requestParam = request
        
        rsp_obj = collector_service_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.collector_service_sdk",
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
    
    def update_collector_aggregate_metric_rule(self, request, org, user, timeout=10):
        # type: (collector_service_sdk.api.metric.update_aggregate_metric_rule_pb2.UpdateCollectorAggregateMetricRuleRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        更新聚合指标规则
        :param request: update_collector_aggregate_metric_rule请求
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
            route_name = "easyops.api.collector_service.metric.UpdateCollectorAggregateMetricRule"
        uri = "/api/v1/collector-aggregate-metric-rule/{instanceId}".format(
            instanceId=request.instanceId,
        )
        requestParam = request
        
        rsp_obj = collector_service_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.collector_service_sdk",
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
    
    def update_collector_metric_by_name(self, request, org, user, timeout=10):
        # type: (collector_service_sdk.api.metric.update_metric_pb2.UpdateCollectorMetricByNameRequest, int, str, int) -> collector_service_sdk.api.metric.update_metric_pb2.UpdateCollectorMetricByNameResponse
        """
        依据name更新指标
        :param request: update_collector_metric_by_name请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: collector_service_sdk.api.metric.update_metric_pb2.UpdateCollectorMetricByNameResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.collector_service.metric.UpdateCollectorMetricByName"
        uri = "/api/v1/collector-metric/update-by-name"
        
        requestParam = request
        
        rsp_obj = collector_service_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.collector_service_sdk",
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
        rsp = collector_service_sdk.api.metric.update_metric_pb2.UpdateCollectorMetricByNameResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
